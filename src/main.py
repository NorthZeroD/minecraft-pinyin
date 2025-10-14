from download import *
from utils import *
from gen_pinyin import main as gen_pinyin_main
from gen_pack import main as gen_pack_main

def main() -> None:
    version_manifest = get_version_manifest()

    print(version_manifest['latest'])
    selected_version: str = input("Enter the Minecraft version: ")
    for v in version_manifest['versions']:
        if v['id'] == selected_version:
            version_json_url = v['url']
            break
    else:
        print("Version not found.")
        return
    
    lang_json = get_lang_json(selected_version, version_json_url)
    if lang_json is None:
        print("Failed to get language JSON.")
        return

    gen_pinyin_main()
    gen_pack_main()

if __name__ == "__main__":
    main()
