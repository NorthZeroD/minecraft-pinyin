import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from keymap.xiaohe import *

def main():
    print(to_xiaohe('shi'))

if __name__ == '__main__':
    main()

# shi -> v