# Slides 形式で写して使う見本

余白 のデッキは、Slides の format つきのデッキで組む。スライドは `position:absolute` で置く（左 160px、上 120px の格子）。

見本の実物：[空き家は、900万戸。](../../samples/akiya/)。下の各見本の後ろに、そのデッキの何枚目かを書く。値はすべて hex を直書き（Slides の中では `var()` を使えない）。

## 1枚1数字 — 2枚目・8枚目

```html
<section id="kazu">
<p class="tag">空き家の数　2023年10月1日現在</p>
<div class="num"><p class="huge">900</p><p class="unit">万2千戸</p></div>
<p class="say" style="top:700px;">過去最多。2018年から51万戸ふえた。</p>
<p class="src">出典</p>
<p class="pg">2 / 10</p>
</section>
```

## 比率の帯 — 3枚目

全体を `full`（fill の面）、部分を `empty`（線の四角）で並べ、最後に帯全体を `empty`（面なし）で囲む。長さは 1600px × 割合。

## 推移 — 6枚目

SVG で軸（2px）と縦線・点。強調する2点だけ ink・太さ 3px・点 r10、ほかは line・2px・r6。

## 数字を3つ — 9枚目

`<div class="trio">` に `<div class="one"><p class="v">21.3%</p><p class="k">説明</p></div>` を3つ。

## 写真の枠 — 1枚目・5枚目・10枚目

`<div class="photo" style="left;top;width;height">` に仮の説明。写真が届いたら `<img src="project/photos/<ファイル名>" style="object-fit:cover">`（写真はデッキの `photos/` に置く） に替え、出典を `cap` で書く。

## deck.css

デッキの `project/deck.css` にそのまま置く。

```css
/* 余白と白：白い紙に細い文字。写真を余白の中に1枚だけ置く。空き家＝線だけの四角、住宅＝淡い灰の面。最小文字24px */
section { background:#FAFAF8; color:#222222; font-family:'Noto Sans JP','Noto Sans CJK JP',sans-serif; font-weight:300; padding:0; position:relative; }
section .tag { position:absolute; left:160px; top:120px; width:1300px; margin:0; font-size:24px; line-height:32px; font-weight:400; color:#62625D; letter-spacing:0.06em; }
section .src { position:absolute; left:160px; top:936px; width:1300px; margin:0; font-size:24px; line-height:32px; font-weight:400; color:#62625D; }
section .pg { position:absolute; left:1600px; top:936px; width:160px; margin:0; text-align:right; font-size:24px; line-height:32px; font-weight:400; color:#62625D; }
section .ttl { position:absolute; left:160px; top:560px; width:800px; margin:0; font-size:104px; line-height:132px; font-weight:300; color:#222222; letter-spacing:0.02em; }
section .huge { margin:0; font-size:280px; line-height:280px; font-weight:200; color:#222222; letter-spacing:-0.02em; }
section .unit { margin:0 0 30px 16px; font-size:64px; line-height:80px; font-weight:300; color:#222222; }
section .num { position:absolute; left:160px; top:330px; display:flex; flex-direction:row; align-items:flex-end; }
section .say { position:absolute; left:160px; width:1440px; margin:0; font-size:40px; line-height:64px; font-weight:300; color:#222222; }
section .note { position:absolute; left:160px; width:1440px; margin:0; font-size:28px; line-height:48px; font-weight:400; color:#62625D; }
section .lbl { position:absolute; margin:0; font-size:24px; line-height:32px; font-weight:400; color:#62625D; }
section .big2 { position:absolute; margin:0; font-size:120px; line-height:120px; font-weight:200; color:#222222; }
section .empty { position:absolute; box-sizing:border-box; border:2px solid #222222; background:#FAFAF8; }
section .full { position:absolute; background:#E4E4DF; }
section .photo { position:absolute; box-sizing:border-box; background:#E9E9E5; display:flex; flex-direction:column; justify-content:flex-end; padding:28px; }
section .photo p { margin:0; font-size:24px; line-height:34px; font-weight:400; color:#62625D; }
section .cap { position:absolute; margin:0; font-size:24px; line-height:32px; font-weight:400; color:#62625D; }
section .trio { position:absolute; left:160px; top:300px; width:1600px; display:flex; flex-direction:row; gap:80px; }
section .one { flex:1; border-top:2px solid #222222; padding-top:20px; }
section .one .v { margin:0; font-size:120px; line-height:130px; font-weight:200; color:#222222; }
section .one .k { margin:8px 0 0 0; font-size:28px; line-height:44px; font-weight:400; color:#222222; }
```
