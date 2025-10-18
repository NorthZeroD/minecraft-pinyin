from Downloader import Downloader
from Formatter import Formatter, schemes
from PinyinGenerator import PinyinGenerator
from PackGenerator import PackGenerator
from DictGenerator import DictGenerator

class App:
    download_dir: str
    output_dir: str
    minecraft_version: str
    pinyin_scheme_code: str
    lang_json: dict
    
    @property
    def base_lang_json_name(self):
        return f'zh_cn_{self.minecraft_version}_{self.pinyin_scheme_code}'
    
    @property
    def base_resourcepack_name(self):
        return f'Pinyin_Resource_Pack_{self.minecraft_version}_{self.pinyin_scheme_code}'
    
    downloader: Downloader
    formatter: Formatter
    pinyinGenerator: PinyinGenerator
    packGenerator: PinyinGenerator
    dictGenerator: DictGenerator
    
    def __init__(
        self,
        download_dir: str = 'download',
        output_dir: str = 'output'
    ) -> None:
        self.download_dir = download_dir
        self.output_dir = output_dir
    
    def run(self) -> None:
        try:
            self.downloader = Downloader(self.download_dir)
            self.downloader.get_version_manifest_json()
            print(self.downloader.version_manifest_json['latest'])
            self.minecraft_version = input('Enter the Minecraft version: ')
            self.downloader.select_version(self.minecraft_version)
            self.downloader.get_version_json()
            self.downloader.get_asset_index_json()
            self.lang_json = self.downloader.get_lang_json()

            print(schemes)
            self.formatter = Formatter(input('Enter the pinyin format: '))
            self.pinyin_scheme_code = self.formatter.pinyin_scheme_code

            pinyin_generator = PinyinGenerator(
                self.output_dir,
                self.base_lang_json_name,
                self.formatter.get_converter(),
                self.lang_json
            )
            pinyin_generator.run()

            pack_generator = PackGenerator(
                self.output_dir,
                self.base_resourcepack_name,
                self.base_lang_json_name
            )
            pack_generator.run()
            
            dict_generator = DictGenerator(
                self.output_dir,
                self.lang_json,
                self.minecraft_version,
            )
            dict_generator.run()
        except Exception as e:
            print(f'Error occurred: {e}')
        
        print(f'Done! Check the "{self.output_dir}" folder!')
