from src.States.application_state import application_state
from src.models.llm import llm

def response_generator_node(state:application_state)->dict:
    """Generates a clear and accurate response to the user's query using retrieved context when available."""

    course=state['course']
    query=state['conversastion'][-1].content.strip()
    
    
    retrieved_context=state['retrived_context']
    
    if "NO_RETRIEVAL_NEEDED" in retrieved_context:
        prompt=f"""
        You are a helpful college assistant for a {course} student.

        Answer the user's question using your general knowledge.
        Keep the response clear, concise, and easy to understand.
        Do not mention that you are using general knowledge.

        Question:
        {query}
        """
    else:
        prompt =f"""
        You are a helpful college assistant for a {course} student.

        Answer the user's question using ONLY the information provided
        in the official college document context below.

        Instructions:
        - Give a clear, accurate, and concise answer.
        - If the context contains information specific to the {course} course,
          prioritize that information.
        - Do not make up or assume information that is not present in the context.
        - If the context does not contain enough information to answer the question,
          clearly state that the available information is insufficient.

        Context:
        {retrieved_context}

        Question:
        {query}
        
        """
        
    response=llm.invoke(prompt)
    
    
    return {'conversastion':[('ai',response.content.strip())]}
        
        