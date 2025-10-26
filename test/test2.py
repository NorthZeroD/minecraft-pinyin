import sys
import os
import json

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

from schemes.wr import *
from template import _map


def main() -> None:
    for k in _map:
        _map[k] = to_wr(k)
    print(_map)

if __name__ == '__main__':
    main()
