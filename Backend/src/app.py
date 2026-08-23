from src.Graph.graph import workFlow
from src.models.llm import llm

agent=workFlow()

result=agent.invoke({
    'course':'BCA',
    'conversastion':[('human','what is fee structure of BCA')]
})

print(f"Assistant : {result['conversastion'][-1].content}")
