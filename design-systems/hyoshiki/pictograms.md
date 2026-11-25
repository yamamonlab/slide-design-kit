# 記号のセット

見本デッキで使った記号。SVG（viewBox 0 0 320 320）をそのまま写し、`#1C1C1C` と `#D7261E` だけを使う。表示する大きさは width/height で変える。

## まず低く（`low`）

```html
<svg aria-label="姿勢を低くする人" class="pic" width="230" height="230" viewBox="0 0 320 320"><rect x="30" y="292" width="260" height="10" fill="#1C1C1C"/><g  fill="#1C1C1C"><circle cx="168" cy="150" r="30"/><rect x="110" y="188" width="112" height="58" rx="29"/><rect x="110" y="226" width="56" height="60" rx="22"/><rect x="186" y="226" width="44" height="60" rx="20"/></g><rect x="52" y="60" width="14" height="110" fill="#D7261E"/><polygon points="30,160 88,160 59,206" fill="#D7261E"/></svg>
```

## 机の下で頭を守る（`head`）

```html
<svg aria-label="机の下で頭を守る人" class="pic" width="230" height="230" viewBox="0 0 320 320"><rect x="30" y="292" width="260" height="10" fill="#1C1C1C"/><rect x="40" y="138" width="240" height="18" fill="#1C1C1C"/><rect x="52" y="156" width="16" height="136" fill="#1C1C1C"/><rect x="252" y="156" width="16" height="136" fill="#1C1C1C"/><g transform="translate(32 76) scale(0.75)" fill="#1C1C1C"><circle cx="168" cy="150" r="30"/><rect x="110" y="188" width="112" height="58" rx="29"/><rect x="110" y="226" width="56" height="60" rx="22"/><rect x="186" y="226" width="44" height="60" rx="20"/></g><path d="M108 222 C 108 160, 180 160, 180 222" fill="none" stroke="#1C1C1C" stroke-width="16" stroke-linecap="round"/><rect x="90" y="48" width="30" height="30" fill="#D7261E" transform="rotate(20 105 63)"/><rect x="196" y="70" width="24" height="24" fill="#D7261E" transform="rotate(-15 208 82)"/></svg>
```

## 机の脚を握る（`hold`）

```html
<svg aria-label="机の脚を握る人" class="pic" width="230" height="230" viewBox="0 0 320 320"><rect x="30" y="292" width="260" height="10" fill="#1C1C1C"/><rect x="40" y="138" width="240" height="18" fill="#1C1C1C"/><rect x="52" y="156" width="16" height="136" fill="#1C1C1C"/><rect x="252" y="156" width="16" height="136" fill="#1C1C1C"/><g transform="translate(32 76) scale(0.75)" fill="#1C1C1C"><circle cx="168" cy="150" r="30"/><rect x="110" y="188" width="112" height="58" rx="29"/><rect x="110" y="226" width="56" height="60" rx="22"/><rect x="186" y="226" width="44" height="60" rx="20"/></g><line x1="200" y1="236" x2="250" y2="236" stroke="#1C1C1C" stroke-width="16" stroke-linecap="round"/><circle cx="258" cy="236" r="16" fill="#D7261E"/></svg>
```

## 寝室：枕や布団で頭を守る（`bed`）

```html
<svg aria-label="枕や布団で頭を守る人" class="pic" width="230" height="230" viewBox="0 0 320 320"><rect x="30" y="230" width="260" height="22" fill="#1C1C1C"/><rect x="30" y="180" width="18" height="110" fill="#1C1C1C"/><rect x="272" y="210" width="18" height="80" fill="#1C1C1C"/><rect x="120" y="196" width="150" height="34" rx="12" fill="#1C1C1C"/><circle cx="90" cy="206" r="26" fill="#1C1C1C"/><rect x="52" y="150" width="84" height="40" rx="10" fill="#D7261E"/></svg>
```

## トイレ・浴室：ドアを開けておく（`bath`）

```html
<svg aria-label="トイレや浴室でドアを開けておく" class="pic" width="230" height="230" viewBox="0 0 320 320"><rect x="60" y="40" width="150" height="250" fill="none" stroke="#1C1C1C" stroke-width="14"/><polygon points="67,47 140,74 140,316 67,283" fill="#1C1C1C"/><rect x="196" y="150" width="80" height="16" fill="#D7261E"/><polygon points="270,130 306,158 270,186" fill="#D7261E"/></svg>
```

## 2階：あわてて降りない（`stairs`）

```html
<svg aria-label="あわてて1階に降りない" class="pic" width="230" height="230" viewBox="0 0 320 320"><polygon points="30,290 30,250 90,250 90,210 150,210 150,170 210,170 210,130 290,130 290,290" fill="#1C1C1C"/><circle cx="250" cy="40" r="22" fill="#1C1C1C"/><rect x="228" y="66" width="44" height="64" rx="16" fill="#1C1C1C"/><line x1="40" y1="120" x2="200" y2="280" stroke="#D7261E" stroke-width="18"/><circle cx="120" cy="200" r="92" fill="none" stroke="#D7261E" stroke-width="16"/></svg>
```

## 揺れている間は火を消そうとしない（`fire1`）

```html
<svg aria-label="揺れている間は無理に火を消さない" class="pic" width="270" height="270" viewBox="0 0 320 320"><rect x="60" y="200" width="200" height="90" fill="#1C1C1C"/><rect x="90" y="160" width="140" height="40" rx="6" fill="#1C1C1C"/><path d="M160 70 C 130 110, 120 130, 140 155 C 150 140, 150 125, 160 115 C 170 130, 175 140, 180 155 C 200 130, 190 105, 160 70 Z" fill="#D7261E"/><circle cx="160" cy="245" r="0" fill="#1C1C1C"/></svg>
```

## おさまってから火の始末（`fire2`）

```html
<svg aria-label="揺れがおさまってから火を止める" class="pic" width="270" height="270" viewBox="0 0 320 320"><rect x="60" y="200" width="200" height="90" fill="#1C1C1C"/><rect x="90" y="160" width="140" height="40" rx="6" fill="#1C1C1C"/><circle cx="160" cy="110" r="44" fill="none" stroke="#1C1C1C" stroke-width="14"/><rect x="153" y="66" width="14" height="44" fill="#1C1C1C"/><path d="M222 70 A 70 70 0 0 1 228 150" fill="none" stroke="#D7261E" stroke-width="12"/><polygon points="212,150 244,150 228,176" fill="#D7261E"/></svg>
```

## 塀や看板から離れる（`wall`）

```html
<svg aria-label="ブロック塀から離れる" class="pic" width="200" height="200" viewBox="0 0 320 320"><rect x="30" y="250" width="58" height="36" fill="#1C1C1C"/><rect x="92" y="250" width="58" height="36" fill="#1C1C1C"/><rect x="154" y="250" width="58" height="36" fill="#1C1C1C"/><rect x="61" y="210" width="58" height="36" fill="#1C1C1C"/><rect x="123" y="210" width="58" height="36" fill="#1C1C1C"/><rect x="185" y="210" width="58" height="36" fill="#1C1C1C"/><rect x="30" y="170" width="58" height="36" fill="#1C1C1C"/><rect x="92" y="170" width="58" height="36" fill="#1C1C1C"/><rect x="154" y="170" width="58" height="36" fill="#1C1C1C"/><rect x="61" y="130" width="58" height="36" fill="#1C1C1C"/><rect x="123" y="130" width="58" height="36" fill="#1C1C1C"/><rect x="185" y="130" width="58" height="36" fill="#1C1C1C"/><rect x="30" y="90" width="58" height="36" fill="#1C1C1C"/><rect x="92" y="90" width="58" height="36" fill="#1C1C1C"/><rect x="154" y="90" width="58" height="36" fill="#1C1C1C"/><rect x="200" y="60" width="44" height="30" fill="#D7261E" transform="rotate(25 222 75)"/><rect x="230" y="120" width="40" height="26" fill="#D7261E" transform="rotate(-20 250 133)"/></svg>
```

## かばんで頭を守る（`bag`）

```html
<svg aria-label="かばんで頭を守る人" class="pic" width="200" height="200" viewBox="0 0 320 320"><g  fill="#1C1C1C"><circle cx="160" cy="90" r="28"/><rect x="130" y="126" width="60" height="100" rx="24"/><rect x="132" y="210" width="22" height="100" rx="10"/><rect x="166" y="210" width="22" height="100" rx="10"/></g><rect x="104" y="30" width="112" height="34" rx="8" fill="#D7261E"/><rect x="118" y="60" width="14" height="70" fill="#1C1C1C"/><rect x="188" y="60" width="14" height="70" fill="#1C1C1C"/></svg>
```

## 丈夫なビルに入る（`bldg`）

```html
<svg aria-label="丈夫なビルに入る" class="pic" width="200" height="200" viewBox="0 0 320 320"><rect x="120" y="40" width="160" height="250" fill="#1C1C1C"/><rect x="140" y="64" width="28" height="28" fill="#F7F7F4"/><rect x="184" y="64" width="28" height="28" fill="#F7F7F4"/><rect x="228" y="64" width="28" height="28" fill="#F7F7F4"/><rect x="140" y="110" width="28" height="28" fill="#F7F7F4"/><rect x="184" y="110" width="28" height="28" fill="#F7F7F4"/><rect x="228" y="110" width="28" height="28" fill="#F7F7F4"/><rect x="140" y="156" width="28" height="28" fill="#F7F7F4"/><rect x="184" y="156" width="28" height="28" fill="#F7F7F4"/><rect x="228" y="156" width="28" height="28" fill="#F7F7F4"/><rect x="140" y="202" width="28" height="28" fill="#F7F7F4"/><rect x="184" y="202" width="28" height="28" fill="#F7F7F4"/><rect x="228" y="202" width="28" height="28" fill="#F7F7F4"/><rect x="176" y="240" width="48" height="50" fill="#F7F7F4"/><rect x="30" y="200" width="60" height="16" fill="#D7261E"/><polygon points="86,184 116,208 86,232" fill="#D7261E"/></svg>
```

## 座席で頭を守る（`seat`）

```html
<svg aria-label="座席で頭を守る" class="pic" width="230" height="230" viewBox="0 0 320 320"><rect x="40" y="200" width="200" height="24" fill="#1C1C1C"/><rect x="40" y="120" width="24" height="104" fill="#1C1C1C"/><rect x="60" y="224" width="14" height="70" fill="#1C1C1C"/><rect x="206" y="224" width="14" height="70" fill="#1C1C1C"/><circle cx="140" cy="110" r="26" fill="#1C1C1C"/><rect x="112" y="140" width="56" height="64" rx="18" fill="#1C1C1C"/><rect x="150" y="190" width="70" height="22" rx="10" fill="#1C1C1C"/><rect x="200" y="200" width="22" height="90" rx="10" fill="#1C1C1C"/><rect x="96" y="58" width="90" height="28" rx="6" fill="#D7261E"/></svg>
```

## つり革・手すりにつかまる（`strap`）

```html
<svg aria-label="手すりにつかまる" class="pic" width="230" height="230" viewBox="0 0 320 320"><rect x="40" y="30" width="240" height="12" fill="#1C1C1C"/><circle cx="200" cy="78" r="18" fill="none" stroke="#D7261E" stroke-width="10"/><rect x="196" y="42" width="8" height="20" fill="#1C1C1C"/><circle cx="150" cy="130" r="26" fill="#1C1C1C"/><rect x="122" y="160" width="56" height="80" rx="20" fill="#1C1C1C"/><line x1="170" y1="170" x2="196" y2="96" stroke="#1C1C1C" stroke-width="16" stroke-linecap="round"/><rect x="124" y="226" width="20" height="70" rx="9" fill="#1C1C1C"/><rect x="156" y="226" width="20" height="70" rx="9" fill="#1C1C1C"/></svg>
```

## 改札へ向かわず待つ（`gate`）

```html
<svg aria-label="改札へ向かわず待つ" class="pic" width="230" height="230" viewBox="0 0 320 320"><rect x="40" y="150" width="40" height="140" fill="#1C1C1C"/><rect x="180" y="150" width="40" height="140" fill="#1C1C1C"/><rect x="80" y="196" width="40" height="14" fill="#1C1C1C"/><rect x="140" y="196" width="40" height="14" fill="#1C1C1C"/><circle cx="130" cy="210" r="96" fill="none" stroke="#D7261E" stroke-width="14"/><line x1="62" y1="142" x2="198" y2="278" stroke="#D7261E" stroke-width="14"/><circle cx="276" cy="160" r="20" fill="#1C1C1C"/><rect x="256" y="184" width="40" height="60" rx="14" fill="#1C1C1C"/><rect x="258" y="236" width="14" height="56" fill="#1C1C1C"/><rect x="280" y="236" width="14" height="56" fill="#1C1C1C"/></svg>
```

## 海から高いところへ（`wave`）

```html
<svg aria-label="海から高いところへ" class="pic" width="260" height="260" viewBox="0 0 320 320"><path d="M20 230 Q 55 200 90 230 T 160 230" fill="none" stroke="#1C1C1C" stroke-width="14"/><path d="M20 270 Q 55 240 90 270 T 160 270" fill="none" stroke="#1C1C1C" stroke-width="14"/><polygon points="170,290 300,290 300,120" fill="#1C1C1C"/><line x1="120" y1="170" x2="250" y2="90" stroke="#D7261E" stroke-width="16"/><polygon points="240,66 282,72 258,108" fill="#D7261E"/></svg>
```

## 崖や斜面から離れる（`cliff`）

```html
<svg aria-label="崖や斜面から離れる" class="pic" width="230" height="230" viewBox="0 0 320 320"><polygon points="20,290 20,60 160,290" fill="#1C1C1C"/><circle cx="150" cy="190" r="18" fill="#D7261E"/><circle cx="186" cy="250" r="14" fill="#D7261E"/><rect x="200" y="160" width="70" height="16" fill="#D7261E"/><polygon points="266,142 300,168 266,194" fill="#D7261E"/></svg>
```

## 玄関のドアを開ける（`door`）

```html
<svg aria-label="玄関のドアを開けておく" class="pic" width="230" height="230" viewBox="0 0 320 320"><rect x="90" y="50" width="140" height="240" fill="none" stroke="#1C1C1C" stroke-width="14"/><polygon points="97,57 160,82 160,312 97,283" fill="#1C1C1C"/><rect x="196" y="160" width="80" height="16" fill="#D7261E"/><polygon points="270,140 306,168 270,196" fill="#D7261E"/></svg>
```

## 窓を開けて換気（`gas`）

```html
<svg aria-label="ガスを使わず窓を開けて換気" class="pic" width="230" height="230" viewBox="0 0 320 320"><rect x="50" y="60" width="220" height="220" fill="none" stroke="#1C1C1C" stroke-width="14"/><line x1="160" y1="60" x2="160" y2="280" stroke="#1C1C1C" stroke-width="10"/><rect x="57" y="67" width="96" height="206" fill="#1C1C1C"/><path d="M180 130 q 20 -14 40 0 t 40 0" fill="none" stroke="#D7261E" stroke-width="10"/><path d="M180 170 q 20 -14 40 0 t 40 0" fill="none" stroke="#D7261E" stroke-width="10"/><path d="M180 210 q 20 -14 40 0 t 40 0" fill="none" stroke="#D7261E" stroke-width="10"/></svg>
```

## エレベーターを使わない（`elev`）

```html
<svg aria-label="動いていてもエレベーターを使わない" class="pic" width="230" height="230" viewBox="0 0 320 320"><rect x="100" y="90" width="120" height="180" fill="none" stroke="#1C1C1C" stroke-width="14"/><rect x="113" y="103" width="44" height="154" fill="#1C1C1C"/><rect x="163" y="103" width="44" height="154" fill="#1C1C1C"/><circle cx="160" cy="180" r="122" fill="none" stroke="#D7261E" stroke-width="16"/><line x1="74" y1="94" x2="246" y2="266" stroke="#D7261E" stroke-width="16"/></svg>
```

## 硬い物でたたく（`hammer`）

```html
<svg aria-label="硬い物でたたく" class="pic" width="200" height="200" viewBox="0 0 320 320"><rect x="30" y="40" width="30" height="260" fill="#1C1C1C"/><line x1="270" y1="300" x2="110" y2="190" stroke="#1C1C1C" stroke-width="24"/><line x1="72" y1="235" x2="138" y2="150" stroke="#1C1C1C" stroke-width="48"/><path d="M84 112 A 70 70 0 0 1 134 162" fill="none" stroke="#D7261E" stroke-width="14"/><path d="M94 74 A 110 110 0 0 1 172 152" fill="none" stroke="#D7261E" stroke-width="14"/><path d="M105 35 A 150 150 0 0 1 211 141" fill="none" stroke="#D7261E" stroke-width="14"/></svg>
```

## 音の鳴るアプリ（`phone`）

```html
<svg aria-label="音を鳴らす" class="pic" width="200" height="200" viewBox="0 0 320 320"><rect x="90" y="50" width="120" height="230" rx="18" fill="#1C1C1C"/><rect x="104" y="80" width="92" height="160" fill="#F7F7F4"/><path d="M232 120 A 50 50 0 0 1 232 200" fill="none" stroke="#D7261E" stroke-width="12"/><path d="M256 96 A 80 80 0 0 1 256 224" fill="none" stroke="#D7261E" stroke-width="12"/></svg>
```

