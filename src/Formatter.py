schemes = '''
0. 首字母
1. 全拼
2. 小鹤双拼
'''

scheme_codes = [
    'szm',
    'qp',
    'xh',
    'zrm',
    'sg',
    'wr',
    'zg',
    'gb',
    'jj',
    'abc',
]

def to_szm(s: str) -> str:
    return s[0]

def to_qp(s: str) -> str:
    return s

class Formatter:
    pinyin_scheme_number: str = 'Unknow'
    pinyin_scheme_code: str = 'Unknow'

    def __init__(self, pinyin_scheme_number: str) -> None:
        self.pinyin_scheme_number = pinyin_scheme_number
        self.pinyin_scheme_code = scheme_codes[int(self.pinyin_scheme_number)]

    def get_converter(self):
        if self.pinyin_scheme_number == '0':
            to_pinyin_scheme = to_szm
        elif self.pinyin_scheme_number == '1':
            to_pinyin_scheme = to_qp
        elif self.pinyin_scheme_number == '2':
            from keymaps.xiaohe import to_xh
            to_pinyin_scheme = to_xh
        else:
            raise ValueError(f'Unknown format: {self.pinyin_scheme_number}')
        return to_pinyin_scheme
