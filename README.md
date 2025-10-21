# Minecraft Pinyin

生成 Minecraft **Rime词库**，以及汉语拼音**资源包**(1.13+)，支持全拼、各种双拼和首字母！

你还能对资源包语言格式进行[**自定义**](#脚本交互)！

![资源包列表展示](./.screenshot/pic4.webp)
![物品搜索](./.screenshot/pic1.webp)
![词库](./.screenshot/pic2.webp)
![输入法展示](./.screenshot/pic3.webp)

当前支持的资源包拼音方案:

- [x] 首字母
- [x] 全拼
- [x] 小鹤双拼
- [x] 自然码
- [x] 搜狗双拼
- [x] 微软双拼
- [x] 紫光双拼
- [X] 国标双拼
- [X] 拼音加加
- [X] 智能ABC
- [ ] 粤拼(港繁)

*⭐积极维护中⭐*

## 使用

**请确保你的操作系统上已安装 git 和 python，然后再进行下一步。**

或者，下载[源代码压缩包](https://github.com/NorthZeroD/minecraft-pinyin/archive/refs/heads/main.zip)，在项目根目录进行以下操作中的步骤2️⃣。

### Linux

1️⃣ 克隆项目并切换到项目根目录

```bash
git clone https://github.com/NorthZeroD/minecraft-pinyin.git && cd minecraft-pinyin
```

2️⃣ 更改脚本权限并执行

```bash
chmod +x script/run.sh && ./script/run.sh
```

### Windows

1️⃣ 克隆项目并切换到项目根目录

如果使用 **PowerShell 5**:

```bash
git clone https://github.com/NorthZeroD/minecraft-pinyin.git ; cd minecraft-pinyin
```

如果使用 **CMD** 或 **PowerShell 7**:

```bash
git clone https://github.com/NorthZeroD/minecraft-pinyin.git && cd minecraft-pinyin
```

2️⃣ 执行脚本

如果使用 **Powershell**:

```bash
.\script\run.bat
```

如果使用 **CMD**:

```bash
script\run.bat
```

## 脚本交互

```text
欢迎使用 Minecraft Pinyin 生成器！
https://github.com/NorthZeroD/minecraft-pinyin

你想做什么?
1. 生成资源包和Rime词库 (默认)
2. 生成资源包
3. 生成Rime词库
4. 退出

* 直接回车以选择默认项
[用户输入] 你的选择: 
... ...
1.21.10         25w42a
1.21.9          25w41a
1.21.8          1.21.10-rc1
1.21.7          1.21.9-rc1
1.21.6          1.21.9-pre4
[用户输入] 输入一个MC版本号 (25w42a): 
... ...

有以下可用格式代码:

src     原文
szm     首字母
qp      全拼
xh      小鹤双拼
zrm     自然码
sg      搜狗双拼
wr      微软双拼
zg      紫光双拼
abc     智能ABC
gb      国标双拼
jj      拼音加加
none    无

接下来你将自定义资源包的语言格式。
例如 'src | szm' 你将最终得到 '草方块 | cfk' 的效果。
例如 'qp | none' 你将最终得到 'caofangkuai' 的效果。

[用户输入] 'XXX | ...' 现在输入左侧内容: src
[用户输入] 'src | XXX' 现在输入右侧内容: xh

你已选定格式: '原文 | 小鹤双拼'
(Y)是的，继续 (n)不对，重选
[用户输入] 你的选择: 
... ...
[资源包] 开始生成资源包...
[资源包] 已生成资源包并保存到 output/25w42a/Pinyin_Resource_Pack_25w42a_src_xh.zip
... ...
[词库] 开始生成Rime词库...
[词库] 已生成词库并保存到 output/minecraft.dict.yaml
[结束] 任务已完成。请检查 'output' 文件夹。
```

## 其他

使用 `script` 目录下的 `clean.sh` 或 `clean.bat` 清理 `download` 和 `output` 目录。

使用 `clean.sh` 或 `clean.bat` 递归清理 `__pycache__` 目录。
