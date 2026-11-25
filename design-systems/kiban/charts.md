# 図とグラフ

## 型の選び方

| 伝えたいこと | 型 |
|---|---|
| 手順・工程 | 流れ（左→右、ノード7つまで） |
| 数字が生まれるまでの段階 | 段階の流れ（数字をノードの中に大きく、律速の段を強調） |
| お金・量が出て、後から入る | 時間差の図（上下2段のゾーン：出る／入る） |
| お金・量の出入り | 滝グラフ（入り＝主系列、出＝`chart-base`、差し引き＝強調） |
| 量や変化 | 棒グラフ（8本まで、0から始める） |
| 2つを比べる | 対比（6：6、同じ構成で並べる） |
| 要因・目標の分解 | ツリー（3階層・各2〜4分岐） |
| 見るべき数字を並べる | 数字のタイル（3×2） |
| 1つの数字を印象づける | 主要指標（`figure` の数字＋単位＋比較の基準） |

- 円グラフ・3D・2軸グラフ・ベン図は使わない。
- 型に当てはまらない関係は、無理に図にせず列挙にする。

## 幾何

- 図の座標・幅・高さ・間隔は 4px の倍数。ノード同士は 48px 以上離す。
- 接続線は直角に曲げる。斜めの線、交差する線は使わない。
- 1つの図の上限：ノード7、線10、強調2、注記2。超えたら2枚に分ける。
- 線と注記：意味のある線は `rule` 以上の濃さ（3:1）、注記の点線は `ink-3`。

## ノードの意味（全システム共通）

図の箱の「意味」は全システムで共通。見た目の対応は各システムの README か図解の章に書く。下は Kozu の例。

| 意味 | 使いどころ | Kozu |
|---|---|---|
| ふつう | ふつうの工程・部品 | `surface` に `rule` 3px、角 14px |
| 焦点 | その図で一番見てほしい所。2つまで | 枠だけ `accent` |
| AI | AIが担う工程・AIの発言 | 面を `tint`、アバターは `ink` 塗りに「AI」 |
| 置き場 | データ・ナレッジ | `sunk` に `rule` 3px |
| 外部 | 外部サービス・他部署 | `surface` に `rule-mid` の破線＋種別の語 |
| 任意・未確定 | 任意・将来・選ばない案・未確定 | `sunk` 面か `rule-mid` の破線 |

- 色だけで意味を伝えない。焦点には「最優先」、未確定には「申請中」などの語を添える。

## 読み上げ

- 図の SVG には `role="img"` と、題（60字以内）・説明（1文）を付ける。Slides 形式では `<svg aria-label>`、または図の題をメッセージラインで言う。

## Slides 形式で写して使う見本

Slides の1枚は決められた範囲の HTML で、`var()` は使えない。下の `{ink}` などはブランドのトークンの hex に置き換える。座標の例は 1920×1080・左右 96px の場合。

### 見出し

```html
<div style="display:flex;flex-direction:column;gap:24px">
<p style="font-size:24px;font-weight:700;letter-spacing:1px;color:{ink-3};line-height:1">01　章名</p>
<div style="display:flex;flex-direction:column;gap:16px"><h2 style="font-size:64px;font-weight:700;line-height:1.3;color:{ink}">論点の名詞句</h2><p style="font-size:34px;font-weight:700;line-height:1.5;color:{ink-2}">結論を言い切る1文</p></div>
</div>
```

### 差を矢印で見せる棒グラフ

棒の列を `position:relative` にし、比較元の高さの破線・矢印・注記を重ねる。列 k の左端 = 左の余白 + k ×（列の幅＋間隔）、棒の上端 = 箱の高さ − 棒の高さ。

```html
<div style="position:relative;height:420px;display:flex;flex-direction:row;align-items:flex-end;gap:48px;padding:0 24px">
  <div style="width:160px;display:flex;flex-direction:column;align-items:center;gap:8px"><p style="font-size:28px;color:{ink}">25.8</p><div style="width:120px;height:254px;background:{chart-main}"></div></div>
  <div style="width:160px;display:flex;flex-direction:column;align-items:center;gap:8px"><p style="font-size:28px;font-weight:700;color:{accent}">36.6</p><div style="width:120px;height:360px;background:{accent}"></div></div>
  <x-connector x1="788" y1="166" x2="872" y2="166" head="none" style="color:{ink-3};border-width:2px;border-style:dashed"></x-connector>
  <x-connector x1="832" y1="164" x2="832" y2="64" style="color:{accent};border-width:3px"></x-connector>
  <p style="position:absolute;left:560px;top:0px;width:256px;font-size:32px;line-height:1.4;color:{accent};text-align:right">前期比<br>+10.9</p>
</div>
```

### 段階の流れ

```html
<div style="position:relative;width:1728px;height:520px">
  <div style="position:absolute;left:0px;top:104px;width:352px;height:168px;background:{surface};border:2px solid {ink};display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px"><p style="font-size:28px;font-weight:700;color:{ink}">段階1</p><p style="font-size:48px;color:{ink}">1,325</p><p style="font-size:24px;color:{ink-3}">単位・補足</p></div>
  <!-- 段階2〜4：left 458 / 916 / 1376。強調する段は background:{accent-bg};border:3px solid {accent} -->
  <x-connector x1="352" y1="188" x2="458" y2="188" style="color:{ink};border-width:2px"></x-connector>
  <p style="position:absolute;left:788px;top:0px;width:608px;font-size:32px;line-height:1.4;color:{ink};text-align:center">この段階が速さを決める</p>
  <x-connector x1="1092" y1="56" x2="1092" y2="100" style="color:{ink-3};border-width:2px;border-style:dashed"></x-connector>
</div>
```

### 滝グラフ

0の線を引き、各棒を前の棒の終わりから始める。1単位あたりの高さを1つ決め、全部の棒に使う。プラスの値は棒の上、マイナスは棒の下に書き、符号を付ける。

```html
<div style="position:relative;width:1000px;height:552px">
  <div style="position:absolute;left:40px;top:38px;width:120px;height:102px;background:{chart-main}"></div>
  <div style="position:absolute;left:240px;top:38px;width:120px;height:424px;background:{chart-base}"></div>
  <div style="position:absolute;left:440px;top:140px;width:120px;height:323px;background:{accent}"></div>
  <div style="position:absolute;left:0px;top:139px;width:1000px;height:2px;background:{ink}"></div>
  <p style="position:absolute;left:20px;top:0px;width:160px;font-size:28px;color:{ink};text-align:center">+56.4</p>
  <p style="position:absolute;left:0px;top:516px;width:200px;font-size:24px;color:{ink-2};text-align:center">項目名</p>
</div>
```

### 数字のタイル

```html
<div style="display:grid;grid-template-columns:repeat(3, 1fr);gap:32px 48px">
  <div style="display:flex;flex-direction:column;gap:8px;background:{surface};border:3px solid {accent};padding:24px 28px">
    <p style="font-size:24px;letter-spacing:2px;color:{accent}">01　見る項目</p>
    <p style="font-size:56px;line-height:1.1;color:{ink}">16〜17%</p>
    <p style="font-size:24px;line-height:1.5;color:{ink-2}">何が、いつまでに、どうなるかを1文で</p>
  </div>
</div>
```

### 足元

```html
<p style="position:absolute;left:96px;bottom:40px;width:1500px;font-size:24px;line-height:1.4;color:{ink-3}">出典：発行者「資料名」（発行年）。○○は当資料の計算</p>
<p style="position:absolute;right:96px;bottom:40px;width:200px;text-align:right;font-size:24px;color:{ink-3}">03 / 14</p>
```

### Slides 形式の注意

- 間隔は `gap` と `padding` で取る（`margin` は使えない）。
- 1つの `position:relative` の箱に置ける固定要素は24個まで。
- 人物などの画像は、元のデザインシステムの素材をデッキにコピーしてから `<img>` で置く。
