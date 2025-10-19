import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from keymaps.xh import *
from pypinyin import lazy_pinyin, load_phrases_dict
from pypinyin_dict.phrase_pinyin_data import cc_cedict
from phrases_dict import phrases_dict

def main():
    cc_cedict.load()
    load_phrases_dict(phrases_dict)
    tests = [
        '海豚的恩惠',
        '快乐恶魂',
        '无穷无尽',
        '闪长岩',
        '樱花木栅栏',
        '鞘翅'
    ]
    for j in tests:
        pinyin_list = lazy_pinyin(j, errors='exception')
        for i in range(len(pinyin_list)):
            pinyin_list[i] = to_xh(pinyin_list[i])
        pinyin_str = ''.join(pinyin_list)
        print(pinyin_str)

if __name__ == '__main__':
    main()

# qiao chi -> qxoii