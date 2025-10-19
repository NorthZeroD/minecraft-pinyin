import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from pycantonese import characters_to_jyutping

def main() -> None:
    print(characters_to_jyutping('閃長巖'))

if __name__ == '__main__':
    main()
