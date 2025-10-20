import os
import copy
from pypinyin import lazy_pinyin, load_phrases_dict, Style
from pypinyin_dict.phrase_pinyin_data import cc_cedict
from phrases_dict import phrases_dict

class DictGenerator:
    output_dir: str
    lang_json: dict
    minecraft_version: str
    output_dict: dict = {}

    def __init__(self,
        output_dir: str,
        lang_json: dict,
        minecraft_version: str
    ) -> None:
        self.output_dir = output_dir
        self.lang_json = copy.deepcopy(lang_json)
        self.minecraft_version = minecraft_version
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
                and not k.startswith('entity.minecraft.')
            ):
                continue
            try:
                pinyin_list = lazy_pinyin(v, style=Style.TONE, errors='exception')
                pinyin_str = ' '.join(pinyin_list)
                self.output_dict.update({v: pinyin_str})
            except Exception as e:
                pass

        with open(f'{self.output_dir}/minecraft.dict.yaml', 'w', encoding='utf-8') as f:
            f.write('---\n')
            f.write('name: "Minecraft Dictionary"\n')
            f.write(f'version: "{self.minecraft_version}"\n')
            f.write('sort: by_weight\n')
            f.write('...\n')
            for k, v in self.output_dict.items():
                f.write(f'{k}\t{v}\n')

        print(f'Generated and saved {self.output_dir}/minecraft.dict.yaml')

if __name__ == '__main__':
    from main import main
    main()
