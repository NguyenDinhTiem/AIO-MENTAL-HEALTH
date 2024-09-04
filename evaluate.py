import openai
from llama_index.core import Settings, Document, VectorStoreIndex
from llama_index.core.ingestion import IngestionPipeline, IngestionCache
from llama_index.llms.openai import OpenAI
from llama_index.core.node_parser import TokenTextSplitter
from llama_index.core.evaluation import (
    BatchEvalRunner,
    CorrectnessEvaluator,
    FaithfulnessEvaluator,
    RelevancyEvaluator
)
from llama_index.core.llama_dataset.generator import RagDatasetGenerator
import asyncio
import pandas as pd
import nest_asyncio
from tqdm.asyncio import tqdm_asyncio
import streamlit as st
from src import ingest_pipeline, index_builder
import os

# Set up necessary settings for LLM
def setup_openai(api_key: str, model: str = "gpt-4o-mini", temperature: float = 0.2):
    openai.api_key = api_key
    Settings.llm = OpenAI(model=model, temperature=temperature)

# Generate questions from nodes
def generate_questions(nodes, num_questions_per_chunk: int = 1):
    dataset_generator = RagDatasetGenerator(nodes, num_questions_per_chunk=num_questions_per_chunk)
    eval_questions = dataset_generator.generate_questions_from_nodes()
    return eval_questions.to_pandas()

# Define asynchronous evaluation function
async def evaluate_async(query_engine, df):
    correctness_evaluator = CorrectnessEvaluator() # Evaluate correctness against a reference answer
    faithfulness_evaluator = FaithfulnessEvaluator() # Evaluate hallucination of the response
    relevancy_evaluator = RelevancyEvaluator() # Evaluate if the response actually answers the query

    # Initialize the BatchEvalRunner
    runner = BatchEvalRunner(
        {
            "correctness": correctness_evaluator,
            "faithfulness": faithfulness_evaluator,
            "relevancy": relevancy_evaluator
        },
        show_progress=True
    )

    # Run the asynchronous evaluation
    eval_result = await runner.aevaluate_queries(
        query_engine= query_engine,
        queries=[question for question in df['query']],
    )

    return eval_result

# Collect and aggregate the results
def aggregate_results(df, eval_result):
    data = []
    for i, question in enumerate(df['query']):
        correctness_result = eval_result['correctness'][i]
        faithfulness_result = eval_result['faithfulness'][i]
        relevancy_result = eval_result['relevancy'][i]
        data.append({
            'Query': question,
            'Correctness response': correctness_result.response,
            'Correctness passing': correctness_result.passing,
            'Correctness feedback': correctness_result.feedback,
            'Correctness score': correctness_result.score,
            'Faithfulness response': faithfulness_result.response,
            'Faithfulness passing': faithfulness_result.passing,
            'Faithfulness feedback': faithfulness_result.feedback,
            'Faithfulness score': faithfulness_result.score,
            'Relevancy response': relevancy_result.response,
            'Relevancy passing': relevancy_result.passing,
            'Relevancy feedback': relevancy_result.feedback,
            'Relevancy score': relevancy_result.score,
        })

    # Create a pandas DataFrame from the data
    df_result = pd.DataFrame(data)
    return df_result

# Calculate and print average scores
def print_average_scores(df):
    correctness_scores = df['Correctness score'].mean()
    faithfulness_scores = df['Faithfulness score'].mean()
    relevancy_scores = df['Relevancy score'].mean()
    print(f"Correctness scores: {correctness_scores}")
    print(f"Faithfulness scores: {faithfulness_scores}")
    print(f"Relevancy scores: {relevancy_scores}")
    return correctness_scores, faithfulness_scores, relevancy_scores

# Main function to execute the steps
def main():
    # Apply nested asyncio
    nest_asyncio.apply()

    # Setup OpenAI
    api_key = st.secrets.openai.OPENAI_API_KEY
    setup_openai(api_key=api_key)

    # Create document and split into nodes
    nodes = ingest_pipeline.ingest_documents()

    # Create vector store index and query engine
    index = index_builder.build_indexes(nodes)
    dsm5_engine = index.as_query_engine(
        similarity_top_k=3,
    )

    # Generate evaluation questions
    df = generate_questions(nodes)

    # Evaluate and aggregate results
    eval_result = asyncio.run(evaluate_async(query_engine=dsm5_engine, df=df))
    df_result = aggregate_results(df, eval_result)

    # Print average scores
    correctness_scores, faithfulness_scores, relevancy_scores = print_average_scores(df_result)
    
    # Save results
    os.makedirs("eval_results", exist_ok=True)
    df_result.to_csv("eval_results/evaluation_results.csv", index=False)
    df.to_csv("eval_results/evaluation_questions.csv", index=False)
    with open("eval_results/average_scores.txt", "w") as f:
        f.write(f"Correctness scores: {correctness_scores}\n")
        f.write(f"Faithfulness scores: {faithfulness_scores}\n")
        f.write(f"Relevancy scores: {relevancy_scores}\n")
    

if __name__ == "__main__":
    main()