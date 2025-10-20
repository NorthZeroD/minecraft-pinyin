intro: str = """
有以下可用格式代码:

src\t原文本
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

if __name__ == "__main__":
    print(intro)
