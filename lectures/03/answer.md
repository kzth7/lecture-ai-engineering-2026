# 第3回 解答

## 演習

- 第1回（素のLLM）とエージェントの回答の違い：\
第1回（素のLLM）は、具体的な情報源がないため、一般論による推測によりよくあるパターンを提示し、正確を期すために質問者本人に資料を確認するように促す回答をした。一方、今回のエージェントの回答は、用語集（data/glossary.json）から適切なものを回答した。
  - 具体的なコマンドの結果
> % uv run python -m app.agent "AIE2026の講座の宿題にある「3レベル」とは何ですか？"\
> [model] gemini-3.5-flash-lite\
> ...（省略）...\
> AIE2026の宿題における「3レベル」とは、宿題の難易度や取り組み方の構成のことです。
>
> 具体的には以下の3つの段階に分かれており、受講生はどれか1つを選んで取り組めば、その回の宿題は完了となります。
>
> 1. **基礎**：講義内容の確認
> 2. **実装**：自分でコードを書く
> 3. **発展**：調査や試行
>
> なお、原則として宿題の採点は行われません。ご自身の理解度や目的に合わせて、どのレベルに取り組むか選んでみてくださいね。
>
> 関係する回：第1回
- `--trace` で見えたツール呼び出し（ツール名と引数）：\
以下のように search_glossary が query の引数を変えて2回呼び出されていた。
  - 具体的なコマンドの実行結果
> % uv run python -m app.agent --trace "LoRA とQLoRAの違いは？"\
> [model] gemini-3.5-flash-lite\
> ...（省略）...\
> LoRAとQLoRAの違いは、ベースモデルの重みをそのまま使うか、量子化してメモリをさらに節約するかにあります。
>  * **LoRA**: 事前学習済みの重みは固定したまま、重みの更新分を低ランク行列（小さな行列）で近似し、その部分だけを学習するPEFT（Parameter-Efficient Fine-Tuning） 手法です。学習パラメータや保存ファイルを大幅に削減できます。
> * **QLoRA**: ベースモデルの重みを4ビットなどに量子化（Quantization）してメモリ使用量をさらに極限まで抑えた状態で、LoRAによるファインチューニングを行う手法です。これにより、より大きなモデルを小さなGPU環境でも動かせるようになります。
>
>  関係する回：第2回
>
> --- trace ---
>  [tool call]   search_glossary({'query': 'LoRA'})\
>  [tool call]   search_glossary({'query': 'QLoRA'})\
>  [tool return] search_glossary -> [{"term": "LoRA", "lecture": 2, "definition": "事前学習済みの重みは固定したまま、重みの更新分を2つの小さな行列の積（低ランク 行列）で表し、その小さな行列だけを学習するPEFT手法。学習するパラ…\
>  [tool return] search_glossary -> [{"term": "QLoRA", "lecture": 2, "definition": "ベースモデルの重みを4ビットなどに量子化してメモリを節約したうえで、LoRAで学習する手法。より大きなモデルを小さなGPUで扱える。本講座の第2…\
> [usage] RunUsage(cost=Decimal('0.0008563'), details={'text_prompt_tokens': 1196}, input_text_tokens=1196, input_tokens=1196, output_tokens=199, requests=2, tool_calls=2)
- 1つの質問での LLM 呼び出し回数（`requests`）：\
上記のとおり、2回。
- 追加したツールと、docstring に書いた説明：
  - 追加したツール：make_quiz
  - doctstring に書いた説明：\
    指定した回の用語から1つを選び、\
    確認問題と答えを返す。

    「第2回の確認問題を出して」のように、\
    復習用の問題を求められたときに使う。\
    引数: {"lecture": {"type": "integer"}}


## 宿題

- 取り組んだレベル：実装
- やったこと：\
claude code を用いて、第3回宿題資料.pdfのp1,2の実装に関する内容やヒントを与えてコーディング。
- 結果：
> % uv run python -m app.agent --trace "第3回の学習メモ：エージェントはモデル+ハーネス"\
> [model] gemini-3.5-flash-lite\
> ...（省略）...\
> [承認待ち] save_learning_log({'note': 'エージェントはモデル+ハーネス', 'lecture': 3})\
> 実行してよろしいですか？(y/n): y\
> 第3回の学習記録として「エージェントはモデル+ハーネス」というメモを保存しました。素晴らしいまとめですね！\
>
> 第3回
>
> --- trace ---\
> [tool call]   save_learning_log({'note': 'エージェントはモデル+ハーネス', 'lecture': 3})\
> [tool return] save_learning_log -> 第3回の学習記録を保存しました。…\
> [usage] RunUsage(cost=Decimal('0.000255'), details={'text_prompt_tokens': 600}, input_text_tokens=600, input_tokens=600, output_tokens=30, requests=1, tool_calls=1)

- 気づき・疑問：\
Pydantic AI なるフレームワークがあるとは知らず、こんなに簡単にエージェントにツールを持たせられるとは思わなかった。\
コーディングはClaudeが簡単に実装してくれたが、今回のプログラムの全体の構造を読みながら、シンプルな見通しのよいフレームワークだと思った。\
また、用語集（data/glossary.json）のように、データセットを構造的に作ることの重要性を改めて感じた。
