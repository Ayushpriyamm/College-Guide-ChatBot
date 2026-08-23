from src.States.application_state import application_state

def general_node(state:application_state)->dict:
    """"""
    query=state['conversastion'][-1].content.strip()
    
    return {'retrived_context':'NO_RETRIEVAL_NEEDED'}