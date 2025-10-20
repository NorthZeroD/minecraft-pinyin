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

from Intro import Intro
from typing import Callable
from converters import *

format_converters = {
    "src": "src",
    "szm": szm,
    "qp": qp,
    "xh": xh,
    "zrm": zrm,
    "sg": sg,
    "wr": wr,
    "zg": zg,
    "abc": abc,
    "gb": gb,
    "jj": jj,
    "none": "none",
}


class Formatter:
    left_content: str
    right_content: str
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
            print(f"\n你已选定格式: '{l}'")
        else:
            print(f"\n你已选定格式: '{l} | {r}'")
        a = input("(Y)是的，继续 (n)不对，重选\n")
        if a == "y" or a == "Y" or a == "":
            self.left_content = l
            self.right_content = r
            self.left_converter = format_converters[l]
            self.right_converter = format_converters[r]
        else:
            self.select()

    def run(self) -> None:
        Intro.show()
        self.select()


if __name__ == "__main__":
    formatter = Formatter()
    formatter.run()
