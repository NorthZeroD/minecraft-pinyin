from Downloader import *
from Formatter import *
from PinyinGenerator import *
from PackGenerator import *

def main() -> None:
    try:
        downloader = Downloader('download')
        downloader.get_version_manifest_json()
        print(downloader._version_manifest_json['latest'])
        downloader.select_version(input('Enter the Minecraft version: '))
        downloader.get_version_json()
        downloader.get_asset_index_json()
        downloader.get_lang_json()

        print(formats)
        formatter = Formatter(input('Enter the pinyin format: '))

        pinyin_generator = PinyinGenerator(
            formatter,
            downloader._lang_json,
            'output'
        )
        pinyin_generator.run()

        pack_generator = PackGenerator('output')
        pack_generator.run()
    except Exception as e:
        print(f'Error occurred: {e}')

    print(f'Done! Check the "{pack_generator._output_dir}" folder!')

if __name__ == '__main__':
    main()
