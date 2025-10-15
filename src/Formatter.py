from keymaps.xiaohe import to_xiaohe

formats = '''
0. 首字母
1. 全拼
2. 小鹤双拼
'''

class Formatter:
    _selected_format: str = ''

    def __init__(self, selected_format: str) -> None:
        self._selected_format = selected_format

    def get_formatter(self):
        if self._selected_format == '0':
            return lambda x: x[0]
        if self._selected_format == '1':
            return lambda x: x
        if self._selected_format == '2':
            return to_xiaohe
        raise ValueError(f'Unknown format: {self._selected_format}')
