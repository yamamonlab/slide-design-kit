# Slides 形式で写して使う見本

Kozu のデッキは、Slides の `format` つきのデッキ（共有の `project/deck.css` とクラス）で組む。下の「deck.css」をそのままデッキの `project/deck.css` に置き、各スライドは見本のマークアップを写して中身を入れ替える。値はすべて `tokens.json` の hex（Slides の中では `var()` を使えないため直書き）。

見本の実物：[X のおすすめ欄は、どう決まるか](../../samples/x-algorithm/)（解説・勉強会型）。下の各見本の後ろに、そのデッキの何枚目かを書く。見本デッキにない形は「見本デッキになし」と書く。

## 寸法

- キャンバス 1920×1080、余白 左右 96px・上 64px、本文領域の幅 1728px。
- タイトル（48px）＋リード文（32px・1行）で上から約 230px。図の領域は高さ約 750px（下 96px は足元のために空ける）。
- 3パネル＋矢印2本：パネル幅 512px（512×3＋56×2＋20×4＝1728）。
- 時間の帯：1分＝1728÷（全体の分数）px。120分なら 14.4px（15分＝216px）。
- 文字は折り返し位置を選べない（和文は文字の途中で折れる）。行の長さは 文字数×文字サイズ が箱の内幅に収まるように書く。

## 骨格（全スライド共通）

```html
<section id="xxx">
<div class="hd"><div class="bar"></div><h2>論点の名詞句</h2></div>
<p class="lead">結論を1〜2文。<span class="em">結論の語</span>だけ強調。</p>
<div class="main">
  <!-- 図 -->
</div>
<p class="ft">資料名 ｜ 日付</p>
<p class="pg">2 / 13</p>
</section>
```

## パネルの流れ（3パネル＋矢印、下端の帯）— 2枚目・6枚目

```html
<div class="rowc grow" style="align-items:stretch;">
<div class="pnl grow">
<p class="num">1</p>
<p class="ph">見出し</p>
<p class="pt">本文を2〜3行</p>
<div class="sp"></div>
<div class="chip"><x-icon name="Clock" class="ico"></x-icon><p class="cx">このパネルから残るもの</p></div>
</div>
<div class="colc" style="justify-content:center;"><svg aria-label="次へ" width="56" height="28" viewBox="0 0 56 28"><line x1="2" y1="14" x2="50" y2="14" stroke="#2A2A2A" stroke-width="3"/><polyline points="40,5 51,14 40,23" fill="none" stroke="#2A2A2A" stroke-width="3"/></svg></div>
<!-- パネル2、矢印、パネル3 -->
</div>
<div class="pnl ask"><x-icon name="CheckCircle" class="ico" style="color:#A8245A;width:40px;height:40px;"></x-icon><p class="pt" style="font-weight:700;color:#1A1A1A;">お願い：…</p></div>
```

## 対比（選ばない案 » 推す案、縦の工程）— 見本デッキになし（「»」は対比だけに使う。順番には矢印。並べて見せる2つの仕組みは7枚目）

左のパネルに `dash`、工程ボックスに `gray` と `mute`、矢印は `#8A8985`。右は実線、最後の工程を `acc`、途中の体験を `lil`。間に `<p class="chev">»</p>`。

```html
<div class="nd gray"><p class="nt mute">選ばない案の工程</p></div>
<svg aria-label="下へ" width="28" height="40" viewBox="0 0 28 40"><line x1="14" y1="2" x2="14" y2="34" stroke="#8A8985" stroke-width="3"/><polyline points="5,24 14,35 23,24" fill="none" stroke="#8A8985" stroke-width="3"/></svg>
<div class="nd acc"><p class="nt">推す案の到達点を<span class="em">一語</span>で</p></div>
```

## 分岐（1つの考え → 3〜4つに分かれる）— 5枚目

```html
<div class="main" style="gap:0;">
<div class="colc"><p class="num" style="font-size:36px;line-height:52px;padding:10px 48px;border-radius:16px;">中心の考え</p></div>
<svg aria-label="3つに分かれる線" width="1728" height="64" viewBox="0 0 1728 64"><path d="M864 0 V32 M281 32 H1447 M281 32 V64 M864 32 V64 M1447 32 V64" fill="none" stroke="#2A2A2A" stroke-width="3"/></svg>
<div class="row grow"><!-- パネル3枚（grow） --></div>
</div>
```

## 会話のイメージ図（人とAI → 成果物）— 見本デッキになし

```html
<div class="msg"><div class="av"><x-icon name="Users" class="ico"></x-icon></div><div class="bub"><p class="bt">人の発言</p></div></div>
<div class="msg"><div class="av ai"><p class="avt">AI</p></div><div class="bub ai"><p class="bt">役割名：AIの発言</p></div></div>
<p class="cap" style="align-self:flex-start;">会話はあくまでイメージ</p>
```

## 時間の帯（長さ＝時間、上に括弧、下にラベル）— 見本デッキになし

```html
<div class="row" style="gap:0;">
<div class="brk" style="flex:0 0 576px;"><p class="brl">まとまりの名前</p><div class="brb"></div></div>
</div>
<div class="tlbar">
<div class="tb w first" style="flex:0 0 216px;"><p class="tbt">15分</p></div>
<div class="tb d" style="flex:0 0 504px;"><p class="tbt inv">35分</p></div>
<div class="tb l" style="flex:0 0 144px;"><p class="tbt">10分</p></div>
<div class="tb g grow"><p class="tbt">30分</p></div>
</div>
<div class="tlab">
<div class="tlc" style="flex:0 0 216px;"><p class="tlt">18:00</p><p class="tln">区間の名前</p></div>
</div>
```

`w`＝導入・締め（surface）、`d`＝主役の区間（ink 塗り）、`l`＝体験（tint）、`g`＝交流（sunk 寄り）。

## 仕様カード（3×2、または1行に4つ）— 11枚目の上の行

```html
<div class="spec">
<div class="sc"><div class="sk"><x-icon name="Clock" class="ico"></x-icon><p class="skt">日時</p></div><p class="sv">値を2行まで</p></div>
</div>
```

## 段差の接続（今回 → 次回）— 見本デッキになし

幅 1728・高さ 600 の `position:relative` の箱に、左下に今回のパネル（実線）、右上に次回のパネル（`dash`＝未確定）、間を曲線の矢印（SVG）でつなぎ、矢印の下に「何を引き継ぐか」の帯を2本置く。固定要素は6個。

## 構成図（システム・アーキテクチャ）— 3枚目（下の書き方は別の見本「スライドの採点の仕組み」から）

幅 1728・高さ 660 の `.arch`（`position:relative`）に、ゾーン → ゾーン名 → 線の SVG → ノード → 線のラベル → 注記 の順で置く（後に書いたものが上に描かれる。SVG をゾーンより前に書くと線が隠れる）。固定要素は24個まで（見本は22個）。座標は `.arch` の左上から。

```html
<div class="main" style="margin-top:28px;gap:0;padding-bottom:0;">
<div class="arch">
<div class="zone ext" style="left:0;top:0;width:260px;height:660px;"></div>
<div class="zone" style="left:300px;top:0;width:1428px;height:660px;"></div>
<p class="zh" style="left:20px;top:14px;width:230px;">作業場の外</p>
<p class="zh" style="left:320px;top:14px;width:600px;">作業場（クラウドの作業環境）</p>
<svg style="position:absolute;left:0;top:0;" width="1728" height="660" viewBox="0 0 1728 660"><g fill="none" stroke="#2A2A2A" stroke-width="3">
  <path d="M700 140 H748"/><polyline points="736,131 748,140 736,149"/>          <!-- 横の線と右向きの矢じり -->
  <path d="M1270 140 H1400 V328"/><polyline points="1391,316 1400,328 1409,316"/> <!-- 直角に曲がって下向き -->
</g></svg>
<div class="an store" style="left:420px;top:70px;width:280px;"><p class="atag">HTML・CSS</p><p class="anm">デッキのファイル</p></div>
<div class="an" style="left:750px;top:70px;width:250px;"><p class="atag">Playwright</p><p class="anm">描画</p><p class="asb">HTML を画像に</p></div>
<div class="an ai focal" style="left:1370px;top:330px;width:330px;height:160px;"><p class="atag">AI</p><p class="anm">採点エージェント</p><p class="asb">指摘の表を返す</p></div>
<div class="an ext" style="left:20px;top:480px;width:220px;"><p class="atag">人</p><p class="anm">ユーザー</p></div>
<p class="alab" style="left:1410px;top:236px;width:52px;">画像</p>
<p class="anote" style="left:730px;top:236px;width:300px;">描画中は外への接続を遮断<br>はみ出し・24px未満を検出</p>
<p class="acall" style="left:1046px;top:236px;width:340px;">渡すのは画像と基準だけ。<br>経緯・意図は渡さない</p>
</div>
<p class="legend">灰の面＝ファイル・画像・基準　淡い紫の面＝AI　マゼンタの枠＝この仕組みの要　破線の枠＝作業場の外</p>
</div>
```

- ノードの格子：上の段 `top:70`、下の段 `top:480`、ノードの高さ 140。横の線はノードの縦の中央（上の段は y=140）、矢じりは線の終点から 12px 戻った所に幅 18px で。
- 線はノードの縁で止め、ノードの中に入れない（ノードは白い面なので、入った線は隠れるが矢じりも隠れる）。
- 未確定のノード：`class="an store"` に `style="border-style:dashed;border-color:#8A8985;"`、タグ「予定」。

## 段の地図（流れの段の下に、その段の工夫を吊るす）— 8枚目

設計の考え方・原則のように、同じ重さの項目が並ぶときに使う。カードを3×2に並べると、どの項目も文字だけの箱になり、どこに効くのかが分からない。段の流れ（工程ボックス＋矢印）を上に置き、各項目をカード（`dc`）にして、効く段の真下に短い縦線（`vl`）で吊るす。全体に効く項目は、上の括弧（`brk`）に書く。

- 列は `cols` の中に `col`（372px）と `gap56` を交互に。段の行（`rowc`）の工程ボックスも 372px にそろえ、矢印 56px と間 12px で列の位置を合わせる。
- カードは `dc`（見出し `dct` 28px・700、本文 `dcb` 24px、補足 `dcc`）。リード文で言う1つだけ `dc acc`。
- 1つの段に2枚まで縦に重ねてよい。本文は 24px で13字まで（改行を手で入れる）。

## 論点の行（論点｜原資料の記述 → 言えること）— 10枚目

注意点・よくある読み違い・判断の根拠のように「事実から何が言えるか」を並べるとき。3列のパネルにすると中身が少なく空きが出る。1行に1論点の横長のパネル（`rw`）を3つ重ね、左から 論点（`rwt`＋出どころ `dcc`）、原資料の記述（`rwx`）、矢印、言えること（`rwc` の箱、太字）。上に列の見出し（`rhd`）。

## 項目と値の行（注意事項）— 11枚目

注意事項・前提のように短い文が4〜5つ並ぶとき。箇条書きはパネルの上に寄って下が空く。`kv` の行（左に項目名 `kvk`、右に文 `kvv`、行の間に細い線）をパネルの高さいっぱいに等分する。

## 工程ボックスの変種と短い補足

- `nd list`：パネルの中に 4〜5 行の項目を並べるときの工程ボックス（24px・700・左寄せ）。見本 6枚目。
- `ndc`：工程ボックスの中の補足1〜2行（24px、`ink-3`、中央）。名前（`nt`）の下に置く。見本 2枚目・7枚目。
- 灰の工程ボックス（`nd gray`）は「除く・沈める・選ばない」だけ。割り引く・注記するなど、残るものには使わない。
- 章扉が1枚しかないデッキでは章番号に意味がないので、章を2つ以上に分けるか、章扉を使わない。

## 章扉 — 4枚目・9枚目

```html
<section id="div-x" class="div">
<!-- 右に線画の SVG（700×700、left:1092px top:190px、線と点は #8A8985、塗りの点と白抜きの点を交互に） -->
<div class="crumb"><div class="crl"></div><div class="crd"></div><p class="crt">資料名</p></div>
<p class="dno">01</p>
<p class="dt">章の題</p>
<p class="dd">この章で話すことを1行</p>
</section>
```

## 表紙 — 1枚目

地は `surface`。右上に accent 系3色の細い三角形（SVG）、左上に資料の種類の小見出し、`ct`（96px・900）2行のうち1語だけ `em`、`csub`（40px・700）、日付と出典・作成者などを `cmeta` 2行。

## deck.css

```css
/* Kozu：温白の地、黒バーの見出し、角丸の黒枠パネルを細い矢印でつなぐ構成図。最小文字24px */
section {
  background:#F7F6F2; color:#2B2B2B;
  font-family:'Noto Sans JP','Hiragino Sans','Yu Gothic',sans-serif; font-weight:400;
  padding:64px 96px 0 96px; display:flex; flex-direction:column;
}
section .hd { display:flex; flex-direction:row; align-items:center; gap:20px; }
section .bar { width:12px; height:56px; background:#1A1A1A; }
section h2 { margin:0; font-size:48px; line-height:60px; font-weight:700; color:#1A1A1A; }
section .lead { margin:16px 0 0 0; font-size:32px; line-height:48px; color:#2B2B2B; }
section .em { color:#A8245A; font-weight:700; }
section .main { margin-top:36px; flex:1; display:flex; flex-direction:column; gap:24px; padding-bottom:112px; }
section .row { display:flex; flex-direction:row; gap:20px; align-items:stretch; }
section .rowc { display:flex; flex-direction:row; gap:20px; align-items:center; }
section .colc { display:flex; flex-direction:column; align-items:center; gap:12px; }
section .grow { flex:1; }
section .sp { flex:1; }

/* パネル */
section .pnl { background:#FFFFFF; border:3px solid #2A2A2A; border-radius:20px; padding:24px 28px; display:flex; flex-direction:column; align-items:center; gap:14px; }
section .pnl.dash { border-style:dashed; background:#FBFAF8; }
section .pnl.ask { border-color:#A8245A; flex-direction:row; justify-content:center; gap:20px; padding:20px 28px; }
section .ph { margin:0; font-size:36px; line-height:48px; font-weight:700; color:#1A1A1A; text-align:center; }
section .pt { margin:0; font-size:28px; line-height:44px; color:#2B2B2B; text-align:center; }
section .ps { margin:0; font-size:24px; line-height:38px; color:#555552; }
section .psc { margin:0; font-size:24px; line-height:38px; color:#555552; text-align:center; }
section .num { margin:0; font-size:24px; line-height:36px; font-weight:700; color:#FFFFFF; background:#1A1A1A; border-radius:999px; padding:2px 20px; }
section .num.acc { background:#A8245A; }
section .big { margin:0; font-size:88px; line-height:100px; font-weight:900; color:#1A1A1A; }

/* 下端の帯（成果物・要点） */
section .chip { display:flex; flex-direction:row; align-items:center; gap:14px; background:#EDECE8; border-radius:14px; padding:12px 20px; align-self:stretch; }
section .chip .cx { margin:0; font-size:26px; line-height:38px; font-weight:700; color:#1A1A1A; }
section .ico { width:32px; height:32px; color:#1A1A1A; }

/* 工程ボックス */
section .nd { align-self:stretch; background:#FFFFFF; border:3px solid #2A2A2A; border-radius:14px; padding:12px 20px; }
section .nd.gray { background:#EDECE8; border-color:#8A8985; }
section .nd.lil { background:#F3ECF6; }
section .nd.acc { border-color:#A8245A; }
section .nt { margin:0; font-size:28px; line-height:42px; color:#1A1A1A; text-align:center; font-weight:700; }
section .nt.mute { color:#555552; font-weight:400; }

/* チャット */
section .msg { display:flex; flex-direction:row; align-items:flex-start; gap:16px; align-self:stretch; }
section .av { width:56px; height:56px; border-radius:12px; border:3px solid #2A2A2A; background:#FFFFFF; display:flex; align-items:center; justify-content:center; }
section .av.ai { background:#1A1A1A; border-color:#1A1A1A; }
section .avt { margin:0; font-size:24px; line-height:30px; font-weight:900; color:#FFFFFF; }
section .bub { flex:1; background:#FFFFFF; border:3px solid #2A2A2A; border-radius:14px; padding:10px 20px; }
section .bub.ai { background:#F3ECF6; }
section .bt { margin:0; font-size:26px; line-height:40px; color:#1A1A1A; }

/* 注記 */
section .cap { margin:0; font-size:24px; line-height:36px; color:#555552; text-align:center; }
section .chev { margin:0; font-size:72px; line-height:72px; font-weight:900; color:#1A1A1A; }

/* フッター */
section .ft { position:absolute; left:96px; bottom:40px; width:1300px; margin:0; font-size:24px; line-height:30px; color:#555552; }
section .pg { position:absolute; left:1664px; bottom:40px; width:160px; margin:0; text-align:right; font-size:24px; line-height:30px; color:#555552; }

/* 表紙 */
section.cover { background:#FFFFFF; padding:72px 120px 0 120px; }
section .evt { margin:0; font-size:28px; line-height:40px; font-weight:700; color:#1A1A1A; }
section .ct { margin:190px 0 0 0; font-size:96px; line-height:122px; font-weight:900; color:#1A1A1A; }
section .csub { margin:28px 0 0 0; font-size:40px; line-height:58px; font-weight:700; color:#1A1A1A; }
section .cmeta { margin:12px 0 0 0; font-size:28px; line-height:44px; color:#333330; }

/* 章扉 */
section.div { padding:64px 96px 0 96px; }
section .crumb { display:flex; flex-direction:row; align-items:center; gap:16px; }
section .crl { width:160px; height:0; border-top:3px solid #8A8985; }
section .crd { width:14px; height:14px; border-radius:7px; background:#8A8985; }
section .crt { margin:0; font-size:24px; line-height:32px; color:#555552; }
section .dno { margin:300px 0 0 0; font-size:40px; line-height:52px; font-weight:900; color:#A8245A; }
section .dt { margin:8px 0 0 0; font-size:64px; line-height:84px; font-weight:900; color:#1A1A1A; }
section .dd { margin:20px 0 0 0; font-size:30px; line-height:46px; color:#333330; width:900px; }

/* タイムライン */
section .tlbar { display:flex; flex-direction:row; height:76px; border:3px solid #2A2A2A; border-radius:12px; overflow:hidden; }
section .tb { display:flex; align-items:center; justify-content:center; border-left:3px solid #2A2A2A; }
section .tb.first { border-left:none; }
section .tb.w { background:#FFFFFF; }
section .tb.l { background:#F3ECF6; }
section .tb.d { background:#1A1A1A; }
section .tb.g { background:#E4E3DE; }
section .tbt { margin:0; font-size:24px; line-height:30px; font-weight:700; color:#1A1A1A; }
section .tbt.inv { color:#FFFFFF; }
section .tlab { display:flex; flex-direction:row; }
section .tlc { display:flex; flex-direction:column; gap:2px; padding-left:6px; }
section .tlt { margin:0; font-size:24px; line-height:32px; color:#555552; font-variant-numeric:tabular-nums; }
section .tln { margin:0; font-size:26px; line-height:34px; font-weight:700; color:#1A1A1A; }
section .brk { display:flex; flex-direction:column; align-items:center; gap:6px; }
section .brl { margin:0; font-size:26px; line-height:36px; font-weight:700; color:#1A1A1A; text-align:center; }
section .brb { align-self:stretch; height:14px; border:3px solid #2A2A2A; border-bottom:none; }

/* 仕様カード */
section .spec { display:grid; grid-template-columns:1fr 1fr 1fr; gap:16px; }
section .sc { background:#FFFFFF; border:3px solid #2A2A2A; border-radius:16px; padding:14px 22px; display:flex; flex-direction:column; gap:4px; }
section .sk { display:flex; flex-direction:row; align-items:center; gap:10px; }
section .skt { margin:0; font-size:24px; line-height:34px; font-weight:700; color:#555552; }
section .sv { margin:0; font-size:26px; line-height:38px; color:#1A1A1A; }

/* 予算バー */
section .bud { align-self:stretch; display:flex; flex-direction:column; gap:6px; }
section .budl { display:flex; flex-direction:row; justify-content:space-between; }
section .budk { margin:0; font-size:24px; line-height:34px; color:#2B2B2B; }
section .budv { margin:0; font-size:24px; line-height:34px; font-weight:700; color:#1A1A1A; }
section .trk { height:20px; background:#EDECE8; border-radius:10px; overflow:hidden; }
section .fil { height:20px; background:#1A1A1A; border-radius:10px; }

/* 役割リスト */
section .who { align-self:stretch; display:flex; flex-direction:row; align-items:center; gap:14px; }
section .whot { margin:0; font-size:28px; line-height:40px; font-weight:700; color:#1A1A1A; }
section .lst { align-self:stretch; margin:0; padding-left:36px; font-size:24px; line-height:38px; color:#2B2B2B; }

/* 構成図（アーキテクチャ） */
section .arch { position:relative; width:1728px; height:660px; }
section .zone { position:absolute; box-sizing:border-box; border:3px solid #2A2A2A; border-radius:20px; background:#FFFFFF; }
section .zone.ext { border:3px dashed #8A8985; background:#F7F6F2; }
section .zh { position:absolute; margin:0; font-size:24px; line-height:32px; font-weight:700; color:#555552; }
section .an { position:absolute; box-sizing:border-box; height:140px; border:3px solid #2A2A2A; border-radius:14px; background:#FFFFFF; padding:10px 16px; display:flex; flex-direction:column; gap:4px; }
section .an.store { background:#EDECE8; }
section .an.ai { background:#F3ECF6; }
section .an.ext { border-style:dashed; border-color:#8A8985; }
section .an.focal { border-color:#A8245A; }
section .atag { margin:0; align-self:flex-start; font-size:24px; line-height:28px; font-weight:700; color:#FFFFFF; background:#1A1A1A; border-radius:8px; padding:0 10px; }
section .anm { margin:0; font-size:28px; line-height:36px; font-weight:700; color:#1A1A1A; }
section .asb { margin:0; font-size:24px; line-height:32px; color:#555552; }
section .alab { position:absolute; margin:0; font-size:24px; line-height:30px; font-weight:700; color:#2B2B2B; }
section .acall { position:absolute; margin:0; font-size:26px; line-height:36px; font-weight:700; color:#1A1A1A; }
section .legend { margin:12px 0 0 0; font-size:24px; line-height:32px; color:#555552; }
section .anote { position:absolute; margin:0; font-size:24px; line-height:32px; color:#555552; }
section .vf { display:grid; grid-template-columns:1fr 1fr; gap:14px; align-self:stretch; }
section .nd.list .nt { font-size:24px; line-height:34px; text-align:left; font-weight:700; }
section .nd .ndc { margin:0; font-size:24px; line-height:32px; color:#555552; text-align:center; }
section .sc.lg { padding:22px 28px; }
section .sc.lg .skt { font-size:30px; line-height:44px; color:#1A1A1A; }
section .sc.lg .sv { font-size:28px; line-height:46px; margin-top:8px; }
section .lst.lg { font-size:26px; line-height:42px; }
/* 段の地図（設計の考え方） */
section .cols { display:flex; flex-direction:row; gap:12px; align-items:flex-start; }
section .col { flex:0 0 372px; display:flex; flex-direction:column; align-items:stretch; gap:16px; }
section .gap56 { flex:0 0 56px; }
section .vl { align-self:center; width:3px; height:28px; background:#2A2A2A; margin:-16px 0 -16px 0; }
section .dc { background:#FFFFFF; border:3px solid #2A2A2A; border-radius:14px; padding:16px 22px; display:flex; flex-direction:column; gap:6px; }
section .dc.acc { border-color:#A8245A; }
section .dct { margin:0; font-size:28px; line-height:38px; font-weight:700; color:#1A1A1A; }
section .dcb { margin:0; font-size:24px; line-height:36px; color:#2B2B2B; }
section .dcc { margin:0; font-size:24px; line-height:32px; color:#555552; }
/* 論点の行（読むときの注意） */
section .rhd { display:grid; grid-template-columns:400px 1fr 56px 1fr; column-gap:24px; padding:0 31px; }
section .rhd p { margin:0; font-size:24px; line-height:32px; font-weight:700; color:#555552; }
section .rw { display:grid; grid-template-columns:400px 1fr 56px 1fr; column-gap:24px; align-items:center; background:#FFFFFF; border:3px solid #2A2A2A; border-radius:20px; padding:20px 28px; }
section .rwh { display:flex; flex-direction:column; gap:6px; }
section .rwt { margin:0; font-size:32px; line-height:44px; font-weight:700; color:#1A1A1A; }
section .rwx { margin:0; font-size:28px; line-height:42px; color:#2B2B2B; }
section .rwc { background:#FFFFFF; border:3px solid #2A2A2A; border-radius:14px; padding:14px 20px; }
section .rwc p { margin:0; font-size:28px; line-height:42px; font-weight:700; color:#1A1A1A; }
/* 項目と値の行（注意事項） */
section .kv { align-self:stretch; flex:1; display:flex; flex-direction:row; align-items:center; gap:24px; border-top:2px solid #C9C8C3; }
section .kv:first-of-type { border-top:none; }
section .kvk { margin:0; flex:0 0 120px; font-size:24px; line-height:34px; font-weight:700; color:#555552; }
section .kvv { margin:0; flex:1; font-size:28px; line-height:42px; color:#1A1A1A; }
```
