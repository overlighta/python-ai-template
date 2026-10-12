
import argparse

from python_ai_template.prompt import build_prompt


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line argument parser."""

    parser = argparse.ArgumentParser(
        prog="ai-template",
        description="Generate prompts for AI tasks.",
    )

    parser.add_argument(
        "--task",
        type=str,
        required=True,
        choices=["summarization", "explanation"],
        help="Task type: summarization or explanation.",
    )

    parser.add_argument(
        "--text",
        type=str,
        required=True,
        help="Input text for prompt generation.",
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the CLI application."""

    parser = build_parser()
    args = parser.parse_args(argv)

    if not args.text.strip():
        parser.error("--text cannot be empty")

    prompt = build_prompt(args.task, args.text)
    print(prompt)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
