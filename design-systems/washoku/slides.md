# Slides 形式で写して使う見本

和色 のデッキは、見出しに Noto Serif JP、本文に Noto Sans JP を読み込む（deck.json の faces に2つ）。

見本の実物：[冬の二十四節気](../../samples/sekki/)。下の各見本の後ろに、そのデッキの何枚目かを書く。値はすべて hex を直書き（Slides の中では `var()` を使えない）。

## 一年の円 — 2枚目

円（r300）に24の目盛り、冬の6つだけ色の帯。名前は円の外に 24 個。名前は1つの箱（1920×1080 の div）にまとめ、`position:absolute` を24個以内に。

## 円弧 — 3枚目

中心 (960,150)、半径 630。黄経 λ の位置は 角度 = 90° − (λ − 270°)。

## 季節の帯 — 4・6枚目

`<div class="band">` に `<div class="seg" style="width:日数×17.98px;background:色">`。印の SVG は帯の後に書く。

## 日の出と日の入り — 5枚目

縦軸が時刻（5:30〜17:30）、横の位置は日付に比例。帯の色はその日の節気。

## 一年の格子 — 8枚目

`<div class="grid">` に 24 の `cell`。冬の節気だけ上の線を季節の色に。

## 色見本 — 9枚目

`<div class="chips">` に色・名前・hex・使いどころ。

## deck.css

デッキの `project/deck.css` にそのまま置く。

```css
/* 和の伝統色と文様：灰白の紙、明朝の見出し、藍を主に、色は伝統色の名で呼ぶ。最小文字24px */
section { background:#EEEDE8; color:#2A2928; font-family:'Noto Sans JP','Noto Sans CJK JP',sans-serif; font-weight:400; padding:0; position:relative; }
section .k { position:absolute; left:160px; top:96px; width:1400px; margin:0; font-size:24px; line-height:32px; font-weight:700; color:#1E3A5C; letter-spacing:0.12em; }
section h2 { position:absolute; left:160px; top:136px; width:1600px; margin:0; font-family:'Noto Serif JP','Noto Serif CJK JP',serif; font-size:60px; line-height:76px; font-weight:600; color:#2A2928; letter-spacing:0.04em; }
section .ld { position:absolute; left:160px; top:232px; width:1600px; margin:0; font-size:28px; line-height:44px; color:#2A2928; }
section .src { position:absolute; left:160px; top:990px; width:1440px; margin:0; font-size:24px; line-height:32px; color:#5E5C58; }
section .pg { position:absolute; left:1600px; top:990px; width:160px; margin:0; text-align:right; font-size:24px; line-height:32px; color:#5E5C58; }
section .nm { position:absolute; margin:0; text-align:center; font-size:24px; line-height:32px; color:#2A2928; }
section .nm b { font-family:'Noto Serif JP','Noto Serif CJK JP',serif; font-size:40px; line-height:52px; font-weight:600; }
section .sn { position:absolute; margin:0; text-align:center; font-family:'Noto Serif JP','Noto Serif CJK JP',serif; font-size:28px; line-height:34px; font-weight:600; color:#5E5C58; }
section .ct { position:absolute; left:160px; top:470px; width:1400px; margin:0; font-family:'Noto Serif JP','Noto Serif CJK JP',serif; font-size:120px; line-height:150px; font-weight:600; color:#2A2928; letter-spacing:0.08em; }
section .cs { position:absolute; left:160px; top:650px; width:1400px; margin:0; font-family:'Noto Serif JP','Noto Serif CJK JP',serif; font-size:40px; line-height:60px; font-weight:400; color:#2A2928; }
section .band { position:absolute; left:160px; width:1600px; display:flex; flex-direction:row; }
section .seg { box-sizing:border-box; height:160px; display:flex; align-items:center; justify-content:center; border-right:3px solid #EEEDE8; }
section .seg p { margin:0; font-family:'Noto Serif JP','Noto Serif CJK JP',serif; font-size:44px; line-height:52px; font-weight:600; }
section .lab { box-sizing:border-box; padding:14px 0 0 12px; border-left:3px solid #2A2928; }
section .lab p { margin:0; font-size:24px; line-height:34px; color:#2A2928; font-variant-numeric:tabular-nums; }
section .mo { position:absolute; margin:0; font-size:24px; line-height:32px; font-weight:700; color:#5E5C58; }
section .chips { position:absolute; left:160px; top:330px; width:1600px; display:grid; grid-template-columns:repeat(4,1fr); gap:28px; }
section .chip { display:flex; flex-direction:column; gap:6px; }
section .sw { height:150px; }
section .cn { margin:6px 0 0 0; font-family:'Noto Serif JP','Noto Serif CJK JP',serif; font-size:34px; line-height:44px; font-weight:600; color:#2A2928; }
section .cv { margin:0; font-size:24px; line-height:32px; color:#5E5C58; }
section .grid { position:absolute; left:160px; top:310px; width:1600px; display:grid; grid-template-columns:repeat(6,1fr); gap:16px; }
section .cell { box-sizing:border-box; border-top:3px solid #2A2928; padding:10px 0 12px 0; }
section .cell .n { margin:0; font-family:'Noto Serif JP','Noto Serif CJK JP',serif; font-size:36px; line-height:46px; font-weight:600; color:#2A2928; }
section .cell .d { margin:0; font-size:24px; line-height:32px; color:#2A2928; font-variant-numeric:tabular-nums; }
section .list { position:absolute; left:160px; top:330px; width:1600px; display:flex; flex-direction:column; }
section .li { display:flex; flex-direction:row; align-items:baseline; gap:40px; border-top:2px solid #8C8A85; padding:22px 0; }
section .li .a { margin:0; flex:0 0 360px; font-family:'Noto Serif JP','Noto Serif CJK JP',serif; font-size:56px; line-height:68px; font-weight:600; color:#2A2928; }
section .li .b { margin:0; flex:0 0 420px; font-size:36px; line-height:48px; font-weight:700; color:#2A2928; font-variant-numeric:tabular-nums; }
section .li .c { margin:0; flex:1; font-size:28px; line-height:42px; color:#5E5C58; }
section .kvs { position:absolute; left:160px; top:240px; width:1600px; height:700px; display:flex; flex-direction:column; }
section .kv { flex:1; display:flex; flex-direction:row; align-items:center; gap:24px; border-top:2px solid #8C8A85; }
section .kvk { margin:0; flex:0 0 260px; font-size:24px; line-height:34px; font-weight:700; color:#5E5C58; }
section .kvv { margin:0; flex:1; font-size:28px; line-height:42px; color:#2A2928; }
```
