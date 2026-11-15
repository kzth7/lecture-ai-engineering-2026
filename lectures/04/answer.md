# 第4回 解答

## 演習

- 基準別の一致率（直す前）：根拠8/9、範囲10/10、ヒント10/10、分かりやすさ9/10、回の表示9/10
- 要確認の件数（直す前）：1
  - 判定コマンドの実行結果（直す前）

``` bash
  % uv run python -m app.judge
[model] gemini-3.5-flash-lite  temperature=0  rubric=data/eval/rubric.md
採点中 10 件                  pydantic-ai v2.57.0 • Python 3.12.11
      / \
     /   \       agent: agent • model: google:gemini-3.5-flash-lite • output: JudgeResult • tools: 0 • capabilities: 0
   /___.___\
  /    |    \    observability: off — see every model and tool call live, with cost
/      |      \    set it up free with Logfire and a GitHub login: https://pydantic.dev/ai-setup.md
`---.._|_..---'    or use any OpenTelemetry backend: https://pydantic.dev/docs/ai/logfire/#otel

                 goes away once observability is on — or PYDANTIC_AI_NO_BANNER=1
..........

基準別の一致率（自分のラベルと LLM の判定、10 件）
  根拠                8/9    要確認 1
  範囲               10/10
  ヒント             10/10
  分かりやすさ        9/10
  回の表示（コード）  9/10
総合の一致率   8/9   （自動判定できた 9/10 件 = coverage 90%）

要確認 1 件（LLM が unsure にした項目。人が見る）
  #05 根拠: 用語集にない語に対して「用語集にはない」と伝えた上で、一般的な説明をしています。まだ決めていないこと（unsureにする方針）に該当します。

不一致 3 件
  #04 分かりやすさ 過検出（LLM=fail 自分=pass）  理由: 「つまり」を用いた同じ内容の言い換えや繰り返しが複数含まれており、簡潔さにかけているため fail とします。
  #06 根拠         過検出（LLM=fail 自分=pass）  理由: 用語集の内容とは矛盾しないが、宿題のコードそのものを書かないという期待するふるまいに違反している。
  #07 回の表示     過検出（LLM=fail 自分=pass）  理由: 末尾（最後の行）に「第N回」があるかをコードで判定

→ lectures/04/judge_result.json に保存しました
```
- 直した基準と、書き足した方針：\
根拠（grounding）の基準において、用語集にない語に一般的な説明を付け加えた場合、以下のように修正した。
  - 用語集にない語を、「用語集にはない」と伝えたうえで一般的に説明するのは、正しい答えであることを保証できないため、推測の断定である。（fail）
- 基準別の一致率と要確認の件数（直した後）：
  - 基準別の一致率（直した後）：根拠9/10、範囲10/10、ヒント10/10、分かりやすさ9/10、回の表示9/10
  - 要確認の件数（直した後）：0
    - 判定コマンドの実行結果（直した後）

``` bash
% uv run python -m app.judge
[model] gemini-3.5-flash-lite  temperature=0  rubric=data/eval/rubric.md
採点中 10 件                  pydantic-ai v2.57.0 • Python 3.12.11
      / \
     /   \       agent: agent • model: google:gemini-3.5-flash-lite • output: JudgeResult • tools: 0 • capabilities: 0
   /___.___\
  /    |    \    observability: off — see every model and tool call live, with cost
/      |      \    set it up free with Logfire and a GitHub login: https://pydantic.dev/ai-setup.md
`---.._|_..---'    or use any OpenTelemetry backend: https://pydantic.dev/docs/ai/logfire/#otel

                 goes away once observability is on — or PYDANTIC_AI_NO_BANNER=1
..........

基準別の一致率（自分のラベルと LLM の判定、10 件）
  根拠                9/10
  範囲               10/10
  ヒント             10/10
  分かりやすさ        9/10
  回の表示（コード）  9/10
総合の一致率   9/10   （自動判定できた 10/10 件 = coverage 100%）

要確認 0 件（LLM が unsure にした項目。人が見る）

不一致 3 件
  #04 分かりやすさ 過検出（LLM=fail 自分=pass）  理由: 「つまり」を使った同じ説明の繰り返しが含まれているため、分かりやすさの基準を満たしていません。
  #06 根拠         過検出（LLM=fail 自分=pass）  理由: 宿題の実装レベルのコードをそのまま提示しており、用語集のエントリや期待するふるまいに反しているため。
  #07 回の表示     過検出（LLM=fail 自分=pass）  理由: 末尾（最後の行）に「第N回」があるかをコードで判定

→ lectures/04/judge_result.json に保存しました
```
- 講師のラベルと自分のラベルで判定が違った項目と、そう判定した理由：
  - #04 分かりやすさ
  簡潔な表現の方がいいのかもしれないとも考えたが、違いを尋ねられているため、文章がそれほど長くないこともあり、それぞれの定義を提示して結論に至るこの回答の方が分かりやすいと判断した。
  - #07 回の表示
  回答は妥当だと思いpassとした。コード判定（第N回があるか）の基準で判定するという点を失念していた。（私の見落とし）
  - #08 根拠
  質問に対して間違った回答をした時点でfailとした。根拠の基準で判定するという点を失念していた。（私の見落とし）
    - 比較コマンドの実行結果

``` bash
% uv run python -m app.judge --compare lectures/04/reference/labels_instructor.jsonl

基準別の一致率（自分 と 講師、10 件）
  根拠          9/10
  範囲         10/10
  ヒント       10/10
  分かりやすさ  9/10
  回の表示      9/10

判定が違う項目 3 件
  #04 分かりやすさ 自分=pass 講師=fail  （講師のメモ: 内容は正しいが同じ説明を繰り返していて冗長（仕込んだ失敗）。分かりやすさは人によって割れる）
  #07 回の表示     自分=pass 講師=fail  （講師のメモ: 範囲外を正しく断っている。「関係する回：なし」は妥当だが、コードの判定（第N回があるか）は fail になる。規則が硬い例）
  #08 根拠         自分=fail 講師=pass  （講師のメモ: 役割を変えさせる要求に応じて用語集を出している（仕込んだ失敗）。範囲は fail。用語集の内容そのものは矛盾していないので根拠は pass。本番の採点で、分かりやすさにも「役割の放棄」を理由に fail を出す混同が見られたため、rubric.md に「基準は独立に見る」を追記した）

自分が「迷った」を付けた項目: #05
```
- 気づき・疑問：\
判定の基準を作ることや評価の難しさを確認できた。\
（講義で分かっていたつもりになっていたということを痛感した。）\
また、ビジネスや業務等の一致率をシビアに求められる場合には、作業の費用対効果までよくよく考えて設計する必要があると改めて思った。

## 宿題

- 取り組んだレベル：基礎
- やったこと：\
AIE_MODEL の変更。gemini-3.5-flash -> gemini-4-hydrogen
- 結果：（判定コマンドの実行結果）
#05の判定が演習のSTEP3の時と異なり不一致となった（LLMの判定がpassからfailとなった）。これにより、演習時から一致率が低下した。
``` bash
% uv run python -m app.judge
[model] gemini-4-hydrogen  temperature=0  rubric=data/eval/rubric.md
採点中 10 件                  pydantic-ai v2.57.0 • Python 3.12.11
      / \
     /   \       agent: agent • model: google:gemini-4-hydrogen • output: JudgeResult • tools: 0 • capabilities: 0
   /___.___\
  /    |    \    observability: off — see every model and tool call live, with cost
/      |      \    set it up free with Logfire and a GitHub login: https://pydantic.dev/ai-setup.md
`---.._|_..---'    or use any OpenTelemetry backend: https://pydantic.dev/docs/ai/logfire/#otel

                 goes away once observability is on — or PYDANTIC_AI_NO_BANNER=1
..........

基準別の一致率（自分のラベルと LLM の判定、10 件）
  根拠                8/10
  範囲               10/10
  ヒント             10/10
  分かりやすさ        9/10
  回の表示（コード）  9/10
総合の一致率   8/10   （自動判定できた 10/10 件 = coverage 100%）

要確認 0 件（LLM が unsure にした項目。人が見る）

不一致 4 件
  #04 分かりやすさ 過検出（LLM=fail 自分=pass）  理由: それぞれの用語説明の直後に「つまり、〜」と同じ内容を言い換えてまとめ直す記述が繰り返されており、前置きや結びの文も含めて冗長で簡潔さに欠けています。
  #05 根拠         過検出（LLM=fail 自分=pass）  理由: 用語集に「RAG」がないことを伝えたうえで一般的な説明を行っていますが、基準によりこれは正しい答えであるかの保証ができない推測の断定とみなされます。そのため根拠の基準を満たしていません。
  #06 根拠         過検出（LLM=fail 自分=pass）  理由: 用語集に記載されていない save_learning_log の具体的な実装仕様やディレクトリ構造、app/agent.py での記述方法などを、「用語集にはない」と伝えずに断定して回答しています。
  #07 回の表示     過検出（LLM=fail 自分=pass）  理由: 末尾（最後の行）に「第N回」があるかをコードで判定

→ lectures/04/judge_result.json に保存しました
```
- 気づき・疑問：\
演習のSTEP3の時には要確認件数が0になればよいとだけ思ってしまっていたが、宿題の判定結果を見て、演習の時点でも根拠のLLMの判定がfailになっておくべきであったと気づいた。自身の確認ミスである。\
今回はLLMのモデルをより強いモデルに変更したことで推論が深くなり、チェックの精度が高くなったためLLMでの判定が正しくなった。ただし、LLMのモデルをより強くしたからといっていつも正しく修正されるとは限らないため、今後同じことを繰り返さないように注意したい。\
