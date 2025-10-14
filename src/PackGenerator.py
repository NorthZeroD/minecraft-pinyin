import shutil
import os
from pack_meta import *

class PackGenerator:
    _output_dir: str = 'output'

    def __init__(self, output_dir: str = 'output') -> None:
        self._output_dir = output_dir
        if not os.path.exists(self._output_dir):
            os.makedirs(self._output_dir)

    def run(self) -> None:
        os.makedirs(f'{self._output_dir}/Pinyin_Resource_Pack/assets/minecraft/lang', exist_ok=True)
        with open(f'{self._output_dir}/Pinyin_Resource_Pack/pack.mcmeta', 'w', encoding='utf-8') as f:
            import json
            json.dump(pack_meta, f, ensure_ascii=False, indent=2)

        shutil.copy(
            f'{self._output_dir}/zh_py.json',
            f'{self._output_dir}/Pinyin_Resource_Pack/assets/minecraft/lang/zh_py.json'
        )
        shutil.make_archive(
            f'{self._output_dir}/Pinyin_Resource_Pack',
            'zip',
            f'{self._output_dir}/Pinyin_Resource_Pack'
        )
        print(f'Generated and saved {self._output_dir}/Pinyin_Resource_Pack.zip')
