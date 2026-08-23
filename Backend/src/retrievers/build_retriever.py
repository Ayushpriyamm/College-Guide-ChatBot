from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from src.models.embedding_model import embedding_model
from src.models.llm import llm

def build_retriever(file_path:str):
    #load pdfloader
    loader=PyPDFLoader(file_path)
    
    #create a docs
    document=loader.load()
    
    #intilize the text splitter
    splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=80)
    
    #split the doc into chunks
    chunks=splitter.split_documents(document)
    
    #store the chunks into vector store as embedding
    vector_store=FAISS.from_documents(chunks,embedding_model)
    
    #get the retrived doc
    retrived_doc=vector_store.as_retriever(search_kwargs={"k":4})
    
    return retrived_doc
    
    
    
    