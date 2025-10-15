import os
import json
import copy
from pypinyin import lazy_pinyin, load_phrases_dict
from pypinyin_dict.phrase_pinyin_data import cc_cedict
from Formatter import *
from phrases_dict import phrases_dict

class PinyinGenerator:
    _output_dir: str = 'output'
    _formatter: Formatter
    _lang_json: dict = {}

    def __init__(self, output_dir: str, formatter: Formatter, lang_json: dict) -> None:
        self._output_dir = output_dir
        self._formatter = formatter
        self._lang_json = copy.deepcopy(lang_json)
        if not os.path.exists(self._output_dir):
            os.makedirs(self._output_dir)

    def run(self) -> None:
        cc_cedict.load()
        load_phrases_dict(phrases_dict)

        for k, v in self._lang_json.items():
            if (not k.startswith('item.minecraft.')
                and not k.startswith('block.minecraft.')
                and not k.startswith('effect.minecraft.')
                and not k.startswith('enchantment.minecraft.')
            ):
                continue
            try:
                pinyin_list = lazy_pinyin(v, errors='exception')
                for i in range(len(pinyin_list)):
                    pinyin_list[i] = self._formatter.get_formatter()(pinyin_list[i])
                pinyin_str = ''.join(pinyin_list)
                self._lang_json[k] = f'{v} | {pinyin_str}'
            except ValueError as e:
                raise e
            except Exception as e:
                print(f'{e}. Ignore "{k}": "{v}"')
                pass

        with open(f'{self._output_dir}/zh_cn.json', 'w', encoding='utf-8') as f:
            json.dump(self._lang_json, f, ensure_ascii=False, indent=2)

        print(f'Generated and saved {self._output_dir}/zh_cn.json')
