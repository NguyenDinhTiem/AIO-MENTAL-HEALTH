from llama_index.core import SimpleDirectoryReader
from llama_index.core.ingestion import IngestionPipeline, IngestionCache
from llama_index.core.node_parser import TokenTextSplitter
from llama_index.core.extractors import SummaryExtractor
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
import openai
import streamlit as st
from src.global_settings import STORAGE_PATH, FILES_PATH, CACHE_FILE
from src.prompts import CUSTORM_SUMMARY_EXTRACT_TEMPLATE

openai.api_key = st.secrets.openai.OPENAI_API_KEY
Settings.llm = OpenAI(model="gpt-4o-mini", temperature=0.2)

def ingest_documents():
    # Load documents, easy but we can't move data or share for another device.
    # Because document id is root file name when our input is a folder.
    # documents = SimpleDirectoryReader(
    #     STORAGE_PATH, 
    #     filename_as_id = True
    # ).load_data()

    documents = SimpleDirectoryReader(
        input_files=FILES_PATH, 
        filename_as_id = True
    ).load_data()
    for doc in documents:
        print(doc.id_)
    
    try: 
        cached_hashes = IngestionCache.from_persist_path(
            CACHE_FILE
            )
        print("Cache file found. Running using cache...")
    except:
        cached_hashes = ""
        print("No cache file found. Running without cache...")
    pipeline = IngestionPipeline(
        transformations=[
            TokenTextSplitter(
                chunk_size=512, 
                chunk_overlap=20
            ),
            SummaryExtractor(summaries=['self'], prompt_template=CUSTORM_SUMMARY_EXTRACT_TEMPLATE),
            OpenAIEmbedding()
        ],
        cache=cached_hashes
    )
   
    nodes = pipeline.run(documents=documents)
    pipeline.cache.persist(CACHE_FILE)
    
    return nodes