from src.States.application_state import application_state

def router(state:application_state):
    
    if state['query_type']=='academic':
        return 'academic_node'
    elif state['query_type']=='fee':
        return 'fee_node'
    else:
        return 'general_node'