from langchain_core.messages import HumanMessage

from agents.chatbot_stream import chatbot_stream

state = {"messages": [HumanMessage(content="Explain AI in simple words.")]}

for token in chatbot_stream(state):
    print(token, end="", flush=True)
