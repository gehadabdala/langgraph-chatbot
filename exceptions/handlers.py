import logging

logger = logging.getLogger(__name__)


def handle_tool_error(tool_name: str, error: Exception):
    logger.exception(f"Tool '{tool_name}' failed")

    return f"Tool '{tool_name}' failed: {str(error)}"


def handle_llm_error(error: Exception):
    logger.exception("LLM failed")

    return "Sorry, I'm having trouble generating a response right now."
