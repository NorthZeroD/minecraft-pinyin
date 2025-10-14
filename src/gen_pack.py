import shutil
import os
from ojson import Json

pack_meta = {
  "pack": {
    "description": "Pinyin Resource Pack\ngithub.com/NorthZeroD/minecraft-pinyin-resourcepack",
    "pack_format": 99,
  },
  "language": {
    "zh_py": {
      "name": "中文",
      "region": "拼音",
    },
  }
}

def main() -> None:
    os.makedirs("Pinyin_Resource_Pack/assets/minecraft/lang", exist_ok=True)
    pack_meta_json = Json(pack_meta)
    pack_meta_json.save_formatted("Pinyin_Resource_Pack/pack.mcmeta")
    shutil.copy("output/zh_py.json", "Pinyin_Resource_Pack/assets/minecraft/lang/zh_py.json")
    shutil.make_archive('Pinyin_Resource_Pack', 'zip', 'Pinyin_Resource_Pack')

if __name__ == "__main__":
    main()
