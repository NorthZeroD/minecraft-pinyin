from Downloader import Downloader
from Fomatter import Formatter
from LangGenerator import LangGenerator


class App:
    download_dir: str
    output_dir: str
    downloader: Downloader
    formatter: Formatter
    langGenerator: LangGenerator

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
            self.formatter.left_converter,
            self.formatter.right_converter,
            self.downloader.lang_jsons,
            self.output_dir,
            self.downloader.minecraft_version
        )
        self.langGenerator.run()


if __name__ == "__main__":
    app = App()
    app.run()
