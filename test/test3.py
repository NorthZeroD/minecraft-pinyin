import sys
import os
import json
import re

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

from download import get_zhcn_lang_json


def main():
    zhcn_lang_json = get_zhcn_lang_json("1.21.10")
    for k in zhcn_lang_json:
        if re.match(r"^advancements(\.[a-zA-Z0-9_]+)+(?!\.description)$", k):
            print(k)


if __name__ == "__main__":
    main()
