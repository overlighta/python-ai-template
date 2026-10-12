
from python_ai_template.prompt import build_prompt


def test_summarization_prompt():
    result = build_prompt(
        "summarization",
        "Python is easy to learn.",
    )

    assert "请总结" in result
    assert "Python is easy to learn." in result


def test_explanation_prompt():
    result = build_prompt(
        "explanation",
        "What is AI?",
    )

    assert "请用通俗易懂的语言解释" in result
    assert "What is AI?" in result
