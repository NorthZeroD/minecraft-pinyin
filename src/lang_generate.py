import os
import json
from typing import Callable
from pypinyin import lazy_pinyin, load_phrases_dict
from pypinyin_dict.phrase_pinyin_data import cc_cedict
from phrases_dict import phrases_dict
from Formatter import Formatter


def lang_generate(
    lang_json: dict, minecraft_version: str, formatter: Formatter, output_dir="output"
) -> None:
    cc_cedict.load()
    load_phrases_dict(phrases_dict)
    mcv = minecraft_version
    lcc = formatter.left_content_code
    rcc = formatter.right_content_code
    lc = formatter.left_converter
    rc = formatter.right_converter
    for k, v in lang_json.items():
        if (
            not k.startswith("item.minecraft.")
            and not k.startswith("block.minecraft.")
            and not k.startswith("effect.minecraft.")
            and not k.startswith("enchantment.minecraft.")
        ):
            continue
        try:
            # if isinstance(lc, str):
            result = v
            if isinstance(lc, Callable):
                pinyin_list = lazy_pinyin(v, errors="exception")
                result = lc(pinyin_list)
            if isinstance(rc, str):
                if rc == "src":
                    result = f"{result} | {v}"
            elif isinstance(rc, Callable):
                pinyin_list = lazy_pinyin(v, errors="exception")
                result = f"{result} | {rc(pinyin_list)}"
            lang_json[k] = result
        except Exception as e:
            print(e)
    os.makedirs(f"{output_dir}/{mcv}", exist_ok=True)
    filepath = f"{output_dir}/{mcv}/zh_cn_{mcv}_{lcc}_{rcc}.json"
    with open(
        filepath,
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(
            lang_json,
            f,
            ensure_ascii=False,
            indent=2,
        )


if __name__ == "__main__":
    pass
