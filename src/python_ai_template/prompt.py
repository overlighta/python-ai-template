
def build_prompt(task: str, text: str) -> str:
    """Generate a prompt based on the task type."""

    if task == "summarization":
        return (
            "请总结以下内容，提取关键信息，"
            "并使用简洁、清晰的语言回答：\n\n"
            f"{text}"
        )

    if task == "explanation":
        return (
            "请用通俗易懂的语言解释以下内容，"
            "并尽可能提供简单的例子：\n\n"
            f"{text}"
        )

    raise ValueError(f"Unsupported task: {task}")
