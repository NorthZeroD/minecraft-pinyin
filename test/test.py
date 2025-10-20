import sys
import os
import json

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)
from download import get_version_manifest_json


def main() -> None:
    version_manifest_json = get_version_manifest_json()
    versions = version_manifest_json["versions"]
    result_verions = []
    for version in versions:
        result_verions.append(version["id"])
    print(result_verions)


if __name__ == "__main__":
    main()
