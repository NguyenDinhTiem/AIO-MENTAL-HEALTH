from llama_index.core import VectorStoreIndex, load_index_from_storage
from llama_index.core import StorageContext
from src.global_settings import INDEX_STORAGE

def build_indexes(nodes):
    try:
        storage_context = StorageContext.from_defaults(
            persist_dir=INDEX_STORAGE
        )
        vector_index = load_index_from_storage(
            storage_context, index_id="vector"
        )
        print("All indices loaded from storage.")
    except Exception as e:
        print(f"Error occurred while loading indices: {e}")
        storage_context = StorageContext.from_defaults()
        vector_index = VectorStoreIndex(
            nodes, storage_context=storage_context
        )
        vector_index.set_index_id("vector")
        storage_context.persist(
            persist_dir=INDEX_STORAGE
        )
        print("New indexes created and persisted.")
    return vector_index
