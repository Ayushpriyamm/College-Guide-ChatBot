from langgraph.graph import StateGraph,START,END
from src.States.application_state import application_state
from src.nodes.academic_node import academic_node
from src.nodes.fee_node import fee_node
from src.nodes.general_node import general_node
from src.nodes.router_node import router
from src.nodes.query_classification_node import query_classification_node
from src.nodes.response_generator_node import response_generator_node

#build graph
def workFlow():
    
    graph=StateGraph(application_state)
    
    graph.add_node('classifier_node',query_classification_node)
    graph.add_node('academic_node',academic_node)
    graph.add_node('fee_node',fee_node)
    graph.add_node('general_node',general_node)
    graph.add_node('response_node',response_generator_node)
    
    graph.add_edge(START,'classifier_node')
    graph.add_conditional_edges('classifier_node',router)
    
    graph.add_edge('academic_node','response_node')
    graph.add_edge('fee_node','response_node')
    graph.add_edge('general_node','response_node')
    
    graph.add_edge('response_node',END)
    
    app=graph.compile()
    
    return app

