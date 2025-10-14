import json
import os

class Json:    
    _content: dict

    def __init__(self, content: dict) -> None:
        self._content = content

    def load(self, file_path: str) -> None:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        self._content = json.loads(content)

    def save(self, file_path: str) -> None:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(self._content, f, ensure_ascii=False)

    def save_formatted(self, file_path: str) -> None:
        dir_name = os.path.dirname(file_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(self._content, f, indent=2, ensure_ascii=False)

    def print(self) -> None:
        print(self._content)

    @staticmethod
    def load_file(file_path: str) -> 'Json':
        if os.path.exists(file_path) is False:
            return Json({"ignore_keys": []})
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return Json(json.loads(content))

    def data(self) -> dict:
        return self._content
