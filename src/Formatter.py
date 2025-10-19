schemes = '''
0. 首字母
1. 全拼
2. 小鹤双拼
3. 自然码
4. 搜狗双拼
5. 微软双拼
6. 紫光双拼
7. 智能ABC
8. 国标双拼
9. 拼音加加
'''

scheme_codes = [
    'szm',
    'qp',
    'xh',
    'zrm',
    'sg',
    'wr',
    'zg',
    'abc',
    'gb',
    'jj',
    'Unknow',
]

def to_szm(s: str) -> str:
    return s[0]

def to_qp(s: str) -> str:
    return s

from typing import Callable

class Formatter:
    pinyin_scheme_number: str
    pinyin_scheme_code: str

    def __init__(self, pinyin_scheme_number: str) -> None:
        self.pinyin_scheme_number = pinyin_scheme_number
        self.pinyin_scheme_code = scheme_codes[int(self.pinyin_scheme_number)]

    def get_converter(self):
        to_pinyin_scheme: Callable
        if self.pinyin_scheme_number == '0':
            to_pinyin_scheme = to_szm
        elif self.pinyin_scheme_number == '1':
            to_pinyin_scheme = to_qp
        elif self.pinyin_scheme_number == '2':
            from keymaps.xh import to_xh
            to_pinyin_scheme = to_xh
        elif self.pinyin_scheme_number == '3':
            from keymaps.zrm import to_zrm
            to_pinyin_scheme = to_zrm
        elif self.pinyin_scheme_number == '4':
            from keymaps.sg import to_sg
            to_pinyin_scheme = to_sg
        elif self.pinyin_scheme_number == '5':
            from keymaps.wr import to_wr
            to_pinyin_scheme = to_wr
        elif self.pinyin_scheme_number == '6':
            from keymaps.zg import to_zg
            to_pinyin_scheme = to_zg
        elif self.pinyin_scheme_number == '7':
            from keymaps.abc import to_abc
            to_pinyin_scheme = to_abc
        elif self.pinyin_scheme_number == '8':
            from keymaps.gb import to_gb
            to_pinyin_scheme = to_gb
        elif self.pinyin_scheme_number == '9':
            from keymaps.jj import to_jj
            to_pinyin_scheme = to_jj
        else:
            raise ValueError(f'Unknown format: {self.pinyin_scheme_number}')
        return to_pinyin_scheme
