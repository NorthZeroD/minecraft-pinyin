import os
import json
from pypinyin import lazy_pinyin, Style

class PinyinGenerator:
    _output_dir: str = 'output'
    _lang_json: dict = {}

    def __init__(self, lang_json: dict = {}, output_dir: str = 'output') -> None:
        self._lang_json = lang_json
        self._output_dir = output_dir
        if not os.path.exists(self._output_dir):
            os.makedirs(self._output_dir)

    def run(self) -> None:
        for k, v in self._lang_json.items():
            if not k.startswith('item.minecraft.') and not k.startswith('block.minecraft.'):
                continue

            try:
                pinyin_list = lazy_pinyin(v, style=Style.FIRST_LETTER, neutral_tone_with_five=True, errors='exception')
                pinyin_str = ''.join(pinyin_list)
                self._lang_json[k] = f'{v} | {pinyin_str}'
            except Exception as e:
                print(f'{e}. Ignore "{k}": "{v}"')

        with open(f'{self._output_dir}/zh_py.json', 'w', encoding='utf-8') as f:
            json.dump(self._lang_json, f, ensure_ascii=False, indent=2)

        print(f'Generated and saved {self._output_dir}/zh_py.json')
