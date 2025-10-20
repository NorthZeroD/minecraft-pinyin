import os
import json
import copy
from typing import Callable
from pypinyin import lazy_pinyin, load_phrases_dict
from pypinyin_dict.phrase_pinyin_data import cc_cedict
from phrases_dict import phrases_dict

class PinyinGenerator:
    output_dir: str
    lang_json: dict
    converter: Callable
    base_lang_json_name: str

    def __init__(self,
        output_dir: str,
        base_lang_json_name:str,
        converter: Callable,
        lang_json: dict
    ) -> None:
        self.output_dir = output_dir
        self.base_lang_json_name = base_lang_json_name
        self.converter = converter
        self.lang_json = copy.deepcopy(lang_json)
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def run(self) -> None:
        cc_cedict.load()
        load_phrases_dict(phrases_dict)

        for k, v in self.lang_json.items():
            if (not k.startswith('item.minecraft.')
                and not k.startswith('block.minecraft.')
                and not k.startswith('effect.minecraft.')
                and not k.startswith('enchantment.minecraft.')
            ):
                continue
            try:
                pinyin_list = lazy_pinyin(v, errors='exception')
                for i in range(len(pinyin_list)):
                    pinyin_list[i] = self.converter(pinyin_list[i])
                pinyin_str = ''.join(pinyin_list)
                self.lang_json[k] = f'{v} | {pinyin_str}'
            except ValueError as e:
                raise e
            except Exception as e:
                print(f'{e}. Ignore "{k}": "{v}"')
                pass

        path = f'{self.output_dir}/{self.base_lang_json_name}.json'
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(self.lang_json, f, ensure_ascii=False, indent=2)

        print(f'Generated and saved {path}')
