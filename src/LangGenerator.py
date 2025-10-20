import os
import json
from copy import deepcopy
from typing import Callable, Union
from pypinyin import lazy_pinyin, load_phrases_dict
from pypinyin_dict.phrase_pinyin_data import cc_cedict
from phrases_dict import phrases_dict


class LangGenerator:
    left_converter: Union[Callable, str]
    right_converter: Union[Callable, str]
    lang_jsons: dict
    output_dir: str

    def __init__(
        self,
        left_converter: Union[Callable, str],
        right_converter: Union[Callable, str],
        lang_jsons: dict,
        output_dir: str,
        minecraft_version: str,
    ) -> None:
        self.left_converter = left_converter
        self.right_converter = right_converter
        self.lang_jsons = deepcopy(lang_jsons)
        self.output_dir = f"{output_dir}/{minecraft_version}"

    def run(self) -> None:
        cc_cedict.load()
        load_phrases_dict(phrases_dict)
        zhcn_lang = self.lang_jsons["zh_cn"]
        lc = self.left_converter
        rc = self.right_converter
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
        os.makedirs(self.output_dir, exist_ok=True)
        filepath = f"{self.output_dir}/zh_cn.json"
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
