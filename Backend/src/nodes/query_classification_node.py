from src.States.application_state import application_state
from src.models.llm import llm

def query_classification_node(state:application_state)->dict:
    "Analyzes the user query and determines the appropriate query category."
    
    query=state["conversastion"][-1].content.strip()
    
    prompt=f"""
    You are a query classification assistant for a college chatbot.

    Classify the user's query into exactly one of these categories:

    - academic: Questions about courses, subjects, syllabus, exams,
      attendance, assignments, curriculum, academic rules, etc.

    - fee: Questions about tuition fees, admission fees, semester fees,
      hostel fees, examination fees, scholarships, refunds, etc.

    - general: Any query that does not clearly fall under academic or fee.
    
    Classify the query based on its primary intent.

    Return ONLY the category name:
    academic
    fee
    general

    Do not provide any explanation or additional text.
    
    user query :\n\n
    {query}
    
    """
    category=llm.invoke(prompt).content.strip().lower()
    
    if 'academic' in category:
        category='academic'
    elif 'fee' in category:
        category='fee'
    else:
        category='general'
        
    return {'query_type':category}
    