from Downloader import *
from gen_pinyin import main as gen_pinyin_main
from gen_pack import main as gen_pack_main

def main() -> None:
    downloader = Downloader('download/')
    downloader.get_version_manifest_json()
    print(downloader._version_manifest_json['latest'])
    downloader.select_version(input("Enter the Minecraft version: "))
    downloader.get_version_json()
    downloader.get_asset_index_json()
    downloader.get_lang_json()

    gen_pinyin_main()
    gen_pack_main()

if __name__ == "__main__":
    main()
