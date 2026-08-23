from src.States.application_state import application_state
from src.retrievers.fee_retriever import fee_retriever

def fee_node(state:application_state)->dict:
     """Handles fee-related queries and generates an appropriate response."""
     
     query=state['conversastion'][-1].content
     
     retrieved_context=fee_retriever.invoke(query)
     
     context='\n\n'.join([doc.page_content for doc in retrieved_context])
     
     return {'retrived_context': context}
 