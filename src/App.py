from Downloader import Downloader


class App:
    download_dir: str
    output_dir: str
    downloader: Downloader

    def __init__(
        self,
        download_dir: str = "download",
        output_dir: str = "output",
    ) -> None:
        self.download_dir = download_dir
        self.output_dir = output_dir
        self.downloader = Downloader(self.download_dir)
