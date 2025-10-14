import requests
import json
from ojson import Json

def get_json_file(file_name: str, url: str) -> int:
    response = requests.get(url)
    if response.status_code == 200:
        data = Json(json.loads(response.text))
        data.save_formatted(f'download/{file_name}')
        return 200
    return response.status_code

def load_json_file(file_path: str) -> dict:
    return Json.load_file(f'download/{file_path}').data()
