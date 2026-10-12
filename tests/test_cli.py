
import pytest

from python_ai_template.cli import main


def test_cli_summarization(capsys):
    result = main([
        "--task", "summarization",
        "--text", "Python is useful.",
    ])

    output = capsys.readouterr().out

    assert result == 0
    assert "请总结" in output
    assert "Python is useful." in output


def test_cli_explanation(capsys):
    result = main([
        "--task", "explanation",
        "--text", "What is AI?",
    ])

    output = capsys.readouterr().out

    assert result == 0
    assert "请用通俗易懂的语言解释" in output
    assert "What is AI?" in output


def test_cli_missing_text():
    with pytest.raises(SystemExit) as exc_info:
        main(["--task", "summarization"])

    assert exc_info.value.code == 2


def test_cli_help(capsys):
    with pytest.raises(SystemExit) as exc_info:
        main(["--help"])

    output = capsys.readouterr().out

    assert exc_info.value.code == 0
    assert "--task" in output
    assert "--text" in output
