# PanelFlow

角丸の黒枠パネルを細い矢印でつなぎ、各パネルの下端に「何が残るか」の帯を置く、Kozu の基本の図。

- パネルは `surface`、`rule` 3px、`radius-panel`。見出しは `heading` 中央、本文は `body` 中央。
- 下端の帯は `sunk`、`radius-node`、線アイコン（`ink`）＋要点（`label`）。帯の上は余白（`flex:1`）で押し下げ、パネル同士の帯の高さを揃える。
- 矢印は 56×28 の線＋開いた矢じり（`rule` 3px）。パネルとの間は `gap-flow`。
- パネルは2〜4枚。番号の丸（`ink` 塗り、`on-ink` 文字）は順番に意味があるときだけ。
- 焦点のパネルは枠だけ `accent` にしてよい（1枚まで）。
- Slides 形式のマークアップは `slides.md`「パネルの流れ」。
