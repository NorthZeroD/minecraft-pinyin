import shutil
import json
import os
from pack_meta import pack_meta

class PackGenerator:
    output_dir: str
    base_resourcepack_name: str
    base_lang_json_name: str

    def __init__(self,
        output_dir: str,
        base_resourcepack_name: str,
        base_lang_json_name: str
    ) -> None:
        self.output_dir = output_dir
        self.base_resourcepack_name = base_resourcepack_name
        self.base_lang_json_name = base_lang_json_name
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def run(self) -> None:
        output_rp = f'{self.output_dir}/{self.base_resourcepack_name}'
        
        os.makedirs(f'{output_rp}/assets/minecraft/lang', exist_ok=True)
        
        with open(f'{output_rp}/pack.mcmeta', 'w', encoding='utf-8') as f:
            json.dump(pack_meta, f, ensure_ascii=False, indent=2)

        shutil.copy(
            f'{self.output_dir}/{self.base_lang_json_name}.json',
            f'{output_rp}/assets/minecraft/lang/zh_cn.json'
        )
        shutil.make_archive(
            output_rp,
            'zip',
            output_rp
        )
        print(f'Generated and saved {output_rp}.zip')
