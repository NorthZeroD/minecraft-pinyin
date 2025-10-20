from Downloader import Downloader
from Formatter import Formatter
from LangGenerator import LangGenerator
from PackGenerator import PackGenerator


class App:
    download_dir: str
    output_dir: str
    downloader: Downloader
    formatter: Formatter
    langGenerator: LangGenerator
    packGenerator: PackGenerator

    def __init__(
        self,
        download_dir: str = "download",
        output_dir: str = "output",
    ) -> None:
        self.download_dir = download_dir
        self.output_dir = output_dir
        self.downloader = Downloader(self.download_dir)
        self.formatter = Formatter()

    def run(self) -> None:
        self.downloader.run()
        self.formatter.run()
        self.langGenerator = LangGenerator(
            self.formatter,
            self.downloader.lang_jsons,
            self.output_dir,
            self.downloader.minecraft_version,
        )
        mcv = self.downloader.minecraft_version
        lcc = self.formatter.left_content_code
        rcc = self.formatter.right_content_code
        base_resourcepack_name = f"Pinyin_Resource_Pack_{mcv}_{lcc}_{rcc}"
        base_lang_json_name = f"zh_cn_{mcv}_{lcc}_{rcc}"
        self.langGenerator.run()
        self.packGenerator = PackGenerator(
            self.output_dir,
            self.downloader.minecraft_version,
            base_resourcepack_name,
            base_lang_json_name,
        )
        self.packGenerator.run()


if __name__ == "__main__":
    app = App()
    app.run()
