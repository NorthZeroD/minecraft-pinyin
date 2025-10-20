from typing import Callable
from converters import format_converters

format_maps = {
    "src": "原文",
    "szm": "首字母",
    "qp": "全拼",
    "xh": "小鹤双拼",
    "zrm": "自然码",
    "sg": "搜狗双拼",
    "wr": "微软双拼",
    "zg": "紫光双拼",
    "abc": "智能ABC",
    "gb": "国标双拼",
    "jj": "拼音加加",
    "none": "无",
}

format_codes = [
    "src",
    "szm",
    "qp",
    "xh",
    "zrm",
    "sg",
    "wr",
    "zg",
    "abc",
    "gb",
    "jj",
    "none",
]


guide: str = """
有以下可用格式代码:

src\t原文
szm\t首字母
qp\t全拼
xh\t小鹤双拼
zrm\t自然码
sg\t搜狗双拼
wr\t微软双拼
zg\t紫光双拼
abc\t智能ABC
gb\t国标双拼
jj\t拼音加加
none\t无

接下来你将自定义资源包的语言格式。
例如 'src | szm' 你将最终得到 '草方块 | cfk' 的效果。
例如 'qp | none' 你将最终得到 'caofangkuai' 的效果。
"""


class Formatter:
    left_content_code: str
    right_content_code: str
    left_converter: Callable
    right_converter: Callable

    def __init__(self) -> None:
        pass

    def select(self) -> None:
        l = ""
        r = ""
        while not l in format_codes:
            l = input("'XXX | ...' 现在输入左侧内容: ")
            if l == "none":
                print("左侧内容不可为 'none'。请重新输入。")
                l = ""
                continue
            if not l in format_codes:
                print(f"格式化代码 '{l}' 不存在。请重新输入。")
        while not r in format_codes:
            r = input(f"'{l} | XXX' 现在输入右侧内容: ")
            if not r in format_codes:
                print(f"格式化代码 '{r}' 不存在。请重新输入。")
        if r == "none":
            print(f"\n你已选定格式: '{format_maps[l]}'")
        else:
            print(f"\n你已选定格式: '{format_maps[l]} | {format_maps[r]}'")
        a = input("(Y)是的，继续 (n)不对，重选\n")
        if a == "y" or a == "Y" or a == "":
            self.left_content_code = l
            self.right_content_code = r
            self.left_converter = format_converters[l]
            self.right_converter = format_converters[r]
        else:
            self.select()

    def run(self) -> None:
        print(guide)
        self.select()


if __name__ == "__main__":
    formatter = Formatter()
    formatter.run()
