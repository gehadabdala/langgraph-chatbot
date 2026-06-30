from memory.conversation import trim_messages
from services.streaming import stream_response


def chatbot_stream(state):

    messages = trim_messages(state["messages"])

    return stream_response(messages)
