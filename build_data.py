from src import ingest_pipeline, index_builder

if __name__ == "__main__":
    nodes = ingest_pipeline.ingest_documents()
    vector_index = index_builder.build_indexes(nodes)