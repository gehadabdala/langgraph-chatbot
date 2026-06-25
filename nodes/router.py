# Decision Maker


def route_question(state):
    question = state["messages"][-1].content.lower()

    if any(
        word in question
        for word in [
            "+",
            "-",
            "*",
            "/",
        ]
    ):
        return "math"

    return "chatbot"
