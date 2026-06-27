#
MAX_HISTORY = 3


def trim_messages(messages):

    if len(messages) <= MAX_HISTORY:
        return messages

    return messages[-MAX_HISTORY:]
