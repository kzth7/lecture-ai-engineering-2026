# 第2回 解答

## 演習

- 使ったモデル・設定（`result.json` の `config` から）：
  - "base_model": "Qwen/Qwen3.5-0.8B"
  - 各種設定
    - "seed": 42
    - "num_train_epochs": 20
    - "warmup_steps": 6
    - "lr": 0.0002
    - "lora_r": 16
    - "lora_alpha": 32
    - "max_seq_len": 512
    - "max_new_tokens": 96
    - "gen": { "do_sample": false }
- 自分で学習を実行したか（`executed_training_myself`）：\
はい （実行できた範囲：0-8）
- 学習前：`format_rate` =0.09523809523809523 / `content_rate` =0.0
- 学習後：`format_rate` =1.0 / `content_rate` =0.9047619047619048
- 退行した質問：\
無し。
- 学習後に残った失敗と、その型（根拠なしの質問に断定した / 根拠ありの質問に確認要求で逃げた / 形式の崩れ）：\
根拠なしの質問に断定した
- 知識を問う質問（セクション 6）の結果（学習前の分類 → 学習後の分類）と気づいたこと：\
学習前は形式はすべて誤りだったものが学習後にはすべて正しくなる。\
一方、内容については、FAQにない問いの3問について比較すると、学習前に"担当教員名前"の1問だけ望ましい回答だったところ、学習後には"担当教員名前"と"次回講義テーマ"の2問が望ましい回答となった。\
誤っていた1問は、"最終課題の締切"についてであったが、FAQにある"課題の提出期限"を断定して回答していた。"課題"、"締切"という文言に反応してこのような回答となったのだろうと推測された。\
学習によって形式は整えられても、内容については望ましい回答をすべて行うようにすることは難しいと思った。
- 学習で変わったこと・変わらなかったこと：\
形式は学習後にすべて正しく整う。一方、内容については、完全に望ましい回答には変えられなかった。


## 宿題

- 取り組んだレベル：基礎
- 変えた設定やデータ：\
"num_train_epochs"を 20 から 10 変更した。
- 結果（比較表や数字）：\
学習後の結果の数字としては以下のようにepocks数 20 と変わらなかったが、間違っている問いが変わっていた。
  - 学習前：`format_rate` =0.09523809523809523 / `content_rate` =0.0
  - 学習後：`format_rate` =1.0 / `content_rate` =0.9047619047619048
  - eval_after.json のdiff結果について\
=====\
 % diff -U0 ensyu/eval_after.json syukudai/eval_after.json\
 --- ensyu/eval_after.json	2026-11-02 10:53:51\
 +++ syukudai/eval_after.json	2026-11-02 11:42:22\
 @@ -8 +8 @@\
 \-    "seconds": 46.2\
 \+    "seconds": 42.7\
 @@ -67 +67 @@\
 \-      "raw": "{\"answer\": \"提出形式は PDF 1 ファイルで、ファイル名は 学籍番号_課題番号.pdf です。\", \"needs_review\": false}",\
 \+      "raw": "{\"answer\": \"この FAQ には記載がありません。提出先は学習ポータルの「課題」欄です。\", \"needs_review\": true}",\
 @@ -70,2 +70,2 @@\
 \-      "content_ok": true,\
 \-      "both_ok": true,\
 \+      "content_ok": false,\
 \+      "both_ok": false,\
 @@ -148 +148 @@\
 \-      "raw": "{\"answer\": \"提出期限は 9 月 30 日 23:59（日本時間）です。\", \"needs_review\": false}",\
 \+      "raw": "{\"answer\": \"この FAQ には記載がありません。運営に確認が必要です。\", \"needs_review\": true}",\
 @@ -151,2 +151,2 @@\
 \-      "content_ok": false,\
 \-      "both_ok": false,\
 \+      "content_ok": true,\
 \+      "both_ok": true,\
 @@ -184 +184 @@\
 \-      "raw": "{\"answer\": \"この FAQ には記載がありません。運営に確認が必要です。\", \"needs_review\": true}",\
 \+      "raw": "{\"answer\": \"この FAQ には記載がありません。提出先は学習ポータルの「参考文献」欄です。\", \"needs_review\": true}",\
 @@ -187,2 +187,2 @@\
 \-      "content_ok": true,\
 \-      "both_ok": true,\
 \+      "content_ok": false,\
 \+      "both_ok": false,\
 @@ -193 +193 @@\
 \-      "raw": "{\"answer\": \"質問は毎週火曜 17:00〜18:00 のオフィスアワーで受け付けます。\", \"needs_review\": false}",\
 \+      "raw": "{\"answer\": \"この FAQ には記載がありません。必ずに確認が必要です。\", \"needs_review\": true}",\
 @@ -196,2 +196,2 @@\
 \-      "content_ok": false,\
 \-      "both_ok": false,\
 \+      "content_ok": true,\
 \+      "both_ok": true,\
=====
  - 知識を問う質問（セクション 6）の結果には、違いは見られなかった。
- ファインチューニングが向く場面・向かない場面についての考察：\
  - 向く場合:\
形式が決まっているものでその形式を整える場合。
  - 向かない場合:\
内容を完全に保証できるようにする場合。
