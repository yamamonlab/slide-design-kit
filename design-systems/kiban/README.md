**スライドのデザインシステムを作るときの共通基盤。** どのブランドでも変えない決まり（読みやすさ・文章・1枚の骨格・デッキの組み方・図表）と、各ブランドが自分で決める「枠」を定める。個別のシステムは、この基盤に従ったうえで「違い」だけを書く。

## 2つの層

| 層 | 中身 | 誰が決めるか |
|---|---|---|
| **基盤**（このシステム） | 下の「変えない決まり」、`deck.md`・`charts.md` の決まり、Slides 形式の見本、`new-system.md` の手順 | 全システム共通。変えるときは基盤を改定し、目録を更新する |
| **ブランド**（各システム） | 枠の値（色・書体・余白・角）、固有の部品と素材、語り口の細部、基盤と違う点 | 各システム。README の冒頭に「基盤 Kiban v1.1 に従う」と書き、違う点を表にする |

迷ったら基盤が優先。ブランドが基盤と違うことをするときは、理由を README の「基盤との違い」に書く。

## 変えない決まり

### 読みやすさ

- 文字は地に対して 4.5:1 以上（24px 以上の太字・大きな文字は 3:1）。意味を持つ線・形は 3:1 以上。**すべてのテーマで**確かめる。
- 投影資料の最小の文字は 24px。配布用の資料に限り、出典・ページ番号だけ 20px まで下げてよい。
- 色だけで意味を伝えない。良い・悪いには ▲▼ や語を、強調には「最優先」などの語を添える。赤と緑を色相だけで並べない。
- 書体は 3つまで。斜体・下線・網掛けで強調しない（強調は太さ・大きさ・強調色）。

### 1枚の骨格

- **1枚1メッセージ。** タイトル（`title`）に論点を名詞句で、その直下のメッセージライン（`message`）に結論を1文で。本文はその根拠だけ。
- 上から「章の表示 → タイトル → メッセージ → 本文」、足元に出典（左）とページ番号（右）。同じ種類のスライドでは位置を動かさない。
- 12カラムに載せ、1枚の中の割り方は1種類。本文領域の7割を使い、下3割以上を空けない。

### 文章

- 文体は「である調」か体言止め。表紙・挨拶・お願いだけ「です・ます調」。混ぜない。
- 数字は半角、3桁カンマ、単位と比較の基準を必ず書く。作った数字を載せない。例は「例」「サンプル」と明記する。自分で計算した数字は出典の行に「当資料の計算」と書く。
- 約物は全角（`（）`・`：`）。和文と英数字の間にスペースを入れない。
- 出典は「出典：発行者「資料名」（発行年）」。
- 作り手用の英語ラベル（GOAL・Summary）を残さない。絵文字・顔文字・感嘆符は使わない。

### 形と色

- 強調色（`accent`）は1つで、1枚に1〜2か所。2つ以上の意味に使わない。
- 片側だけ色の線のカード、上端の色帯、紫青のグラデーション、絵文字のアイコン、ロボットやAIの擬人化の絵、実在の社名・ロゴ・画面は使わない。
- 影・角丸を使うブランドは、使う場面を限定して README に書く。

## ブランドが決める枠

各システムは、少なくとも次の名前のトークンを持つ（値はブランドごと）。別の名前を使うときは、README の「基盤との対応」に対応表を書く。

| 枠 | トークン | 決めること |
|---|---|---|
| 地と面 | `ground` `surface` `sunk` | 地の色、箱の色、沈めた面 |
| 文字 | `ink` `ink-2` `ink-3` | 見出し、本文、注記（`ink-3` は 4.5:1 の下限） |
| 線 | `rule` `rule-soft` | 意味のある線（3:1）、装飾の線 |
| 強調 | `accent` `accent-bg` `on-accent` | 唯一の強調色とその面、その上の文字 |
| グラフ | `chart-base`（＋主系列） | 比較系列の色。主系列は `accent` か別の1色 |
| 書体 | `type.families` | 見出し・本文・数字の書体（3つまで） |
| 文字の段 | `title` `message` `body` `caption` | 基盤の範囲内のサイズ（`caption` は 24px） |
| 余白 | `margin-x` `margin-top` `margin-bottom` | 基盤の範囲内（左右 96〜120px） |

このシステムの値は、枠の形を示す中立の既定値。そのまま使わず、必ずブランドの値に置き換える。

## 3つの軸

デッキは「見た目 × 目的 × パターン」で決まる。

| 軸 | 決めること | 置き場所 | 増やし方 |
|---|---|---|---|
| 見た目 | 色・書体・線・素材・得意技 | 各デザインシステム | 選び方は `routing.md`、増やし方は `operations.md`（まず既存の改定で足りるか） |
| 目的（デッキの型） | 構成・主役・使うパターン・使わないもの | このシステムの `types.md` | 実際に作ったデッキから足す |
| パターン | 1枚の組み方 | このシステムの `patterns.md` | 2回使ったら昇格、半年使わなければ休止 |

デッキを作るときは、**最初に `routing.md` の3つの問いで見た目を決める**。型は見た目を決めない。

次に、**目的を決めて型を1つ選ぶ**。型がパターンを6〜8個に絞るので、一覧から選ぶ必要はない。目的ごとにデザインシステムを作らない。

## このシステムの章

- `routing.md`：システムの選び方（3つの問い、各システムの得意技）
- `operations.md`：運用の決まり（層、何を共通にするか、増やし方、改定、見直し）
- `types.md`：デッキの型（分析・報告、解説・勉強会、進行・司会、提案、登壇LT）と振り返り
- `patterns.md`：パターンの一覧、見本、候補、昇格の決まり
- `deck.md`：デッキ全体の組み方（型の配分、注記、余白、チェックリスト）
- `charts.md`：図とグラフの決まり、Slides 形式で写して使える見本
- `library.md`：このキットのデザインシステムの目録
- `new-system.md`：新しいデザインシステムを作る手順と、README の雛形


---

## Consuming this system (generated — do not edit)

Every path named below is under `project/` in this design system: read `project/api/tokens.md`, not `api/tokens.md`.

This system ships tokens, no components: take colours, type and fonts from the tokens card below for any page, deck or mock-up; a Slides deck or Design canvas also takes `tokens.json` by file path (that type’s SKILL.md says how). On a Design canvas, also copy `tokens.css` to `project/ds/<folder>/tokens.css` in the call that installs this system, and link it in each artboard that uses this system, right after the `support.js` line and before the system’s other stylesheets: `<link rel="stylesheet" href="ds/<folder>/tokens.css">` (with one `../` in front for each folder the artboard is in).

**Read, per thing:** token values: `api/tokens.md`. After this README, fetch the cards and fonts you need in ONE message as parallel calls — none depends on another.

**Two rules.** Before you use a thing — a component, a token group, an icon, an asset — read its card from the index below; a value you did not read from a card is a guess. `tokens.json`, `manifest.json` and `design-system.json` are sources for tools: hand them over. `SKILL.md` and `artifact-type/` beside them are authoring guidance, not needed to consume the system.

## Index (generated — do not edit)

**Tokens**

- `api/tokens.md` — Every token: surface, text, fill, chart, palette, type, spacing, radius, layout. (7.2k)
