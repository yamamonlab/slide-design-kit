#!/usr/bin/env python3
"""tokens.json から tokens.css を作る。

使い方:
    python3 scripts/build-tokens-css.py design-systems/kozu

- 出力は同じフォルダの tokens.css（上書き）。
- CSS 変数だけを書く。クラス（.title など）は書かない。デッキの deck.css のクラスとぶつけないため。
- 値の "{name}" は var(--name) に置き換える。
- 標準ライブラリだけで動く。
"""
import json
import re
import sys
from pathlib import Path


def css_value(value: str) -> str:
    return re.sub(r"\{([a-z0-9-]+)\}", r"var(--\1)", str(value))


def comment(text: str) -> str:
    return " /* " + str(text).replace("*/", "* /") + " */" if text else ""


def line(name: str, value: str, usage: str = "") -> str:
    return f"  --{name}: {css_value(value)};{comment(usage)}"


def build(data: dict) -> str:
    out = [f"/* {data.get('name', '')} — generated from tokens.json */"]
    theme = data["color"]["themes"][0]["id"]
    out.append(f':root, [data-theme="{theme}"] {{')
    out += [line(t["name"], t["value"], t.get("usage", "")) for t in data["color"]["tokens"]]
    out.append("}")
    out.append(":root {")
    for group in ("spacing", "radius", "stroke", "layout"):
        for t in data.get(group, {}).get("tokens", []):
            out.append(line(t["name"], t["value"], t.get("usage", "")))
    families = data.get("type", {}).get("families", {})
    for key, value in families.items():
        out.append(f"  --font-{key}: {value};")
    for group in data.get("type", {}).get("groups", []):
        family = group.get("family", "sans")
        for s in group["styles"]:
            font = f"{s['fontWeight']} {s['fontSize']}/{s['lineHeight']} var(--font-{family})"
            out.append(line("text-" + s["name"], font, s.get("usage", "")))
    out.append("}")
    return "\n".join(out) + "\n"


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("使い方: python3 scripts/build-tokens-css.py <デザインシステムのフォルダ>")
    folder = Path(sys.argv[1])
    data = json.loads((folder / "tokens.json").read_text(encoding="utf-8"))
    (folder / "tokens.css").write_text(build(data), encoding="utf-8")
    print(f"wrote {folder / 'tokens.css'}")


if __name__ == "__main__":
    main()
