from langchain_core.messages import AIMessage


def math_node(state):

    question = state["messages"][-1].content

    return {"messages": [AIMessage(content=f"Math question detected: {question}")]}
