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
    _selected_scheme: str = ''
    _selected_scheme_code: str = ''

    def __init__(self, selected_format: str) -> None:
        self._selected_scheme = selected_format

    def get_formatter(self):
        if self._selected_scheme == '0':
            to_pinyin_scheme = to_szm
        elif self._selected_scheme == '1':
            to_pinyin_scheme = to_qp
        elif self._selected_scheme == '2':
            from keymaps.xiaohe import to_xh
            to_pinyin_scheme = to_xh
        else:
            raise ValueError(f'Unknown format: {self._selected_scheme}')
        self._selected_scheme_code = scheme_codes[int(self._selected_scheme)]
        return to_pinyin_scheme
