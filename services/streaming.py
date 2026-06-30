from services.agent_chain import agent_chain


def stream_response(messages):
    """
    Stream tokens from the LLM.
    """

    for chunk in agent_chain.stream({"messages": messages}):

        if chunk.content:
            yield chunk.content
