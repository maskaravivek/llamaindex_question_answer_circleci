import os.path
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)

def get_query_index():
    # check if storage already exists
    PERSIST_DIR = "./storage"

    if not os.path.exists(PERSIST_DIR):
        # load the documents and create the index
        documents = SimpleDirectoryReader("data").load_data()
        index = VectorStoreIndex.from_documents(documents)
        # store it for later
        index.storage_context.persist(persist_dir=PERSIST_DIR)
    else:
        # load the existing index
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)

    # Either way we can now query the index
    query_engine = index.as_query_engine()
    
    return query_engine

def answer_query(query):
    if not query or len(query) == 0:
        return None
    
    query_engine = get_query_index()
    response = query_engine.query(query)
    
    return response