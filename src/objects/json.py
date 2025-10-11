class Json:
    _content: str

    def __init__(self, content: str) -> None:
        self._content = content

    def load(self, file_path: str) -> None:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        self._content = content

    def save(self, file_path: str) -> None:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(self._content)

    def save_formatted(self, file_path: str) -> None:
        import json
        import os
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        parsed = json.loads(self._content)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(parsed, f, indent=2, ensure_ascii=False)

    def print(self) -> None:
        print(self._content)

    @staticmethod
    def load_file(file_path: str) -> 'Json':
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return Json(content)

    def data(self) -> dict:
        import json
        return json.loads(self._content)
