import shutil
import os
from pack_meta import *

class PackGenerator:
    _output_dir: str = 'output'
    _minecraft_version: str = 'Unknown'
    _pinyin_scheme: str = 'Unknown'

    def __init__(self, output_dir: str, minecraft_version: str, pinyin_scheme: str) -> None:
        self._output_dir = output_dir
        self._minecraft_version = minecraft_version
        self._pinyin_scheme = pinyin_scheme
        if not os.path.exists(self._output_dir):
            os.makedirs(self._output_dir)

    def run(self) -> None:
        rp_name = f'Pinyin_Resource_Pack_{self._minecraft_version}_{self._pinyin_scheme}'

        os.makedirs(f'{self._output_dir}/{rp_name}/assets/minecraft/lang', exist_ok=True)
        with open(f'{self._output_dir}/{rp_name}/pack.mcmeta', 'w', encoding='utf-8') as f:
            import json
            json.dump(pack_meta, f, ensure_ascii=False, indent=2)

        shutil.copy(
            f'{self._output_dir}/zh_cn.json',
            f'{self._output_dir}/{rp_name}/assets/minecraft/lang/zh_cn.json'
        )
        shutil.make_archive(
            f'{self._output_dir}/{rp_name}',
            'zip',
            f'{self._output_dir}/{rp_name}'
        )
        print(f'Generated and saved {self._output_dir}/{rp_name}.zip')
