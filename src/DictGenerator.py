import os
import json
from pypinyin import lazy_pinyin, load_phrases_dict, Style
from pypinyin_dict.phrase_pinyin_data import cc_cedict
from phrases_dict import phrases_dict

class DictGenerator:
    _lang_json: dict = {}
    _output_dir: str = 'output'
    _dict: dict = {}

    def __init__(self, lang_json: dict, output_dir: str) -> None:
        self._lang_json = lang_json
        self._output_dir = output_dir
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
                pinyin_list = lazy_pinyin(v, style=Style.TONE, errors='exception')
                pinyin_str = ' '.join(pinyin_list)
                self._dict.update({v: pinyin_str})
            except Exception as e:
                print(f'{e}. Ignore "{k}": "{v}"')

        with open(f'{self._output_dir}/minecraft.dict.yaml', 'w', encoding='utf-8') as f:
            f.write('---\n')
            f.write('name: "Minecraft Dictionary"\n')
            f.write('version: "1.0"\n')
            f.write('sort: by_weight\n')
            f.write('...\n')
            for k, v in self._dict.items():
                f.write(f'{k}\t{v}\n')

        print(f'Generated and saved {self._output_dir}/minecraft.dict.yaml')

if __name__ == '__main__':
    with open('download/zh_cn.json', 'r', encoding='utf-8') as f:
        lang_json = json.load(f)

    dict_generator = DictGenerator(lang_json, 'output')
    dict_generator.run()

    print('Generated and saved output/zh_cn_dict.json')
