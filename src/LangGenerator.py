import os
import json
from copy import deepcopy
from typing import Callable, Union
from pypinyin import lazy_pinyin, load_phrases_dict
from pypinyin_dict.phrase_pinyin_data import cc_cedict
from phrases_dict import phrases_dict
from Formatter import Formatter


class LangGenerator:
    formatter: Formatter
    lang_jsons: dict
    minecraft_version: str
    output_dir: str

    def __init__(
        self,
        formatter: Formatter,
        lang_jsons: dict,
        output_dir: str,
        minecraft_version: str,
    ) -> None:
        self.formatter = formatter
        self.lang_jsons = deepcopy(lang_jsons)
        self.minecraft_version = minecraft_version
        self.output_dir = output_dir

    def run(self) -> None:
        cc_cedict.load()
        load_phrases_dict(phrases_dict)
        zhcn_lang = self.lang_jsons["zh_cn"]
        lc = self.formatter.left_converter
        rc = self.formatter.right_converter
        for k, v in zhcn_lang.items():
            if (
                not k.startswith("item.minecraft.")
                and not k.startswith("block.minecraft.")
                and not k.startswith("effect.minecraft.")
                and not k.startswith("enchantment.minecraft.")
            ):
                continue
            if isinstance(lc, str):
                result = v
            elif isinstance(lc, Callable):
                try:
                    pinyin_list = lazy_pinyin(v, errors="exception")
                except Exception as e:
                    print(e)
                result = lc(pinyin_list)
            if isinstance(rc, str):
                if rc == "src":
                    result = f"{result} | {v}"
            elif isinstance(rc, Callable):
                try:
                    pinyin_list = lazy_pinyin(v, errors="exception")
                except Exception as e:
                    print(e)
                result = f"{result} | {rc(pinyin_list)}"
            zhcn_lang[k] = result
        mcv = self.minecraft_version
        lcc = self.formatter.left_content_code
        rcc = self.formatter.right_content_code
        os.makedirs(f'{self.output_dir}/{mcv}', exist_ok=True)
        filepath = f"{self.output_dir}/{mcv}/zh_cn_{mcv}_{lcc}_{rcc}.json"
        with open(
            filepath,
            "w",
            encoding="utf-8",
        ) as f:
            json.dump(
                zhcn_lang,
                f,
                ensure_ascii=False,
                indent=2,
            )


if __name__ == "__main__":
    from main import main

    main()
