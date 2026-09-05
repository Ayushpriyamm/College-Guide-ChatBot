from src.States.application_state import application_state
from src.retrievers.academic_retriever import academic_retriever

def academic_node(state:application_state)->dict:
    """Handles academic-related queries and generates an appropriate response."""
    #step 1 : get the last message of the conversation
    query=state['conversation'][-1].content
    
    #steo 2 : get the retrieved context from the query
    retrieved_context=academic_retriever.invoke(query)
    
    #step 3 : set the retrived context in the state
    context='\n\n'.join([doc.page_content for doc in retrieved_context])
    
    return {'retrived_context':context}
    
    
    
    