"""第1回: 素のLLMに質問するスクリプト（会話履歴付き）。

使い方:
    uv run python -m app.ask "LoRAとは何ですか？"
    uv run python -m app.ask            # 質問を省略すると、講座に固有の質問をする

ツールも持たない「素の」呼び出しだが、会話履歴を保持して質問を続けられる。
講座に固有のことを聞くと、「分からない」と答えるか、一般論でもっともらしく答える
（講座の実際とは違う）ことを確かめよう。
（第3回で、用語集を検索できるエージェントにして改善する）
"""

import argparse
import readline  # noqa: F401  (input() の行編集を有効化)

from google import genai
from google.genai import errors

from app.config import MODEL, api_error_message, get_api_key

# 講座に固有の質問。正しい答えは data/glossary.json の homework-levels にある
DEFAULT_QUESTION = "AIE2026の講座の宿題にある「3レベル」とは何ですか？"


def ask(client: genai.Client, history: list[str], question: str) -> str:
    history.append(question)
    response = client.models.generate_content(model=MODEL, contents=history)

    usage = response.usage_metadata
    if usage is not None:
        print(f"===  [usage tokens]  input: {usage.prompt_token_count},  output: {usage.candidates_token_count}  ===")

    text = response.text
    history.append(text)
    return text


def main() -> None:
    parser = argparse.ArgumentParser(description="素のLLMに質問する（会話履歴付き）")
    parser.add_argument("question", nargs="?", default=DEFAULT_QUESTION)
    args = parser.parse_args()

    client = genai.Client(api_key=get_api_key())
    history: list[str] = []

    print(f"[model] {MODEL}")
    print(f"[質問] {args.question}\n")
    try:
        print(ask(client, history, args.question))
        print()

        while True:
            try:
                question = input("[質問] (qで終了) > ")
            except EOFError:
                break
            if question.strip().lower() in ("q", "quit", "exit"):
                break
            if not question.strip():
                continue
            print(ask(client, history, question))
            print()
    except errors.APIError as e:
        print(api_error_message(e.code, e.message))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
