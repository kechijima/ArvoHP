#!/usr/bin/env python3
"""ARVO HP のページ生成スクリプト.

src/page.html（共通テンプレート）から、ファーストビューだけを差し替えた
3つのページを作ります。

  index.html   ① 全年齢パターン        https://arvo-fitness.web.app/
  30s40s.html  ② 30〜40代向けパターン  https://arvo-fitness.web.app/30s40s
  50s.html     ③ 50代以上向けパターン  https://arvo-fitness.web.app/50s

使い方:  python3 tools/build.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHECK = '<svg aria-hidden="true"><use href="#i-check"/></svg>'

PAGES = {
    # ① 全年齢
    "index.html": dict(
        PATH="",
        TITLE="女性専用フィットネス・ピラティス | ARVO和歌山",
        DESC="和歌山市・オークワセントラルシティ内の女性専用フィットネス「ARVO」。ピラティス・ヨガ・ダンス系レッスンとマシンピラティスのパーソナル。平日は夜21:15まで。ピラティスパーソナル体験1回4,400円。ご予約はLINEから。",
        OG_DESC="女性だけのスタジオで、自分のペースで。平日は夜21:15まで。ピラティスパーソナル体験1回4,400円。",
        HERO_TAG="和歌山市の女性専用フィットネス",
        H1='女性だけの空間で、<br><span class="nw"><em>自分のペース</em>で。</span>',
        LEAD="ピラティス・ヨガ・ダンス。<br>はじめての方も、久しぶりの方も。",
        HERO_IMG="hero-pilates.webp", HERO_ALT="マシンピラティスで身体を伸ばす女性", HERO_W=1333, HERO_H=2000, HERO_POS="45% 45%",
        CHIPS=["女性だけのスタジオ", "はじめてでも大丈夫", "平日は夜21:15まで", "オークワセントラルシティ内"],
    ),
    # ② 30〜40代
    "30s40s.html": dict(
        PATH="30s40s",
        TITLE="仕事帰りに通える女性専用ピラティス | ARVO和歌山",
        DESC="和歌山市・オークワセントラルシティ内の女性専用フィットネス「ARVO」。平日は夜21:15まで、仕事帰りにマシンピラティス。姿勢もボディラインも。ピラティスパーソナル体験1回4,400円。ご予約はLINEから。",
        OG_DESC="仕事帰りの1時間で、自分を整える。平日は夜21:15まで。ピラティスパーソナル体験1回4,400円。",
        HERO_TAG="平日は夜21:15まで｜女性専用",
        H1='仕事帰りの1時間で、<br><span class="nw"><em>自分を整える</em>。</span>',
        LEAD="マシンピラティスで、姿勢もボディラインも。<br>夜の時間を、自分のために。",
        HERO_IMG="hero-group.webp", HERO_ALT="グループでマシンピラティスをする女性たち", HERO_W=1000, HERO_H=1125, HERO_POS="60% 40%",
        CHIPS=["女性だけのスタジオ", "平日は夜21:15まで", "マシンピラティス対応", "お買い物ついでに通える"],
    ),
    # ③ 50代以上
    "50s.html": dict(
        PATH="50s",
        TITLE="50代からはじめる、女性専用ピラティス | ARVO和歌山",
        DESC="和歌山市・オークワセントラルシティ内の女性専用フィットネス「ARVO」。50代からでも無理なくはじめられるピラティス・ヨガ。平日は夜21:15まで、仕事帰りにも通えます。ピラティスパーソナル体験1回4,400円。ご予約はLINEから。",
        OG_DESC="いまの私に、ちょうどいい運動を。平日は夜21:15まで。ピラティスパーソナル体験1回4,400円。",
        HERO_TAG="和歌山市の女性専用フィットネス",
        H1='50代からの私に、<br><span class="nw"><em>ちょうどいい運動</em>を。</span>',
        LEAD="肩こり、姿勢、体力の変化。<br>ピラティスで、やさしく整えませんか。",
        HERO_IMG="hero-pilates.webp", HERO_ALT="マシンピラティスで身体を伸ばす女性", HERO_W=1333, HERO_H=2000, HERO_POS="45% 45%",
        CHIPS=["女性だけのスタジオ", "運動が久しぶりでも大丈夫", "マシンピラティス対応", "オークワセントラルシティ内"],
    ),
}


def main():
    tpl = (ROOT / "src" / "page.html").read_text(encoding="utf-8")
    for name, v in PAGES.items():
        html = tpl
        for key, val in v.items():
            if key == "CHIPS":
                val = "\n".join(f"      <li>{CHECK}{c}</li>" for c in val)
            html = html.replace("{{" + key + "}}", str(val))
        assert "{{" not in html, f"{name}: 未置換のプレースホルダがあります"
        (ROOT / name).write_text(html, encoding="utf-8")
        print("built", name)


if __name__ == "__main__":
    main()
