# Minecraft Pinyin

生成 Minecraft **Rime词库**，以及汉语拼音**资源包**，支持全拼、各种双拼和首字母！

[使用 - 生成资源包](#使用---生成资源包)

[使用 - 生成Rime词库](使用---生成Rime词库)

当前支持的资源包拼音方案:

- [x] 首字母
- [x] 全拼
- [x] 小鹤双拼
- [ ] 自然码
- [ ] 搜狗双拼
- [ ] 微软双拼
- [ ] 紫光双拼
- [ ] 国标双拼
- [ ] 拼音加加
- [ ] 智能ABC

*持续更新中...*

## 使用 - 生成资源包

**请确保你的操作系统上已安装 git 和 python，然后再进行下一步。**

### Linux

1. 克隆项目并切换到项目根目录

```bash
git clone https://github.com/NorthZeroD/minecraft-pinyin.git && cd minecraft-pinyin
```

2. 更改脚本权限并执行

```bash
chmod +x script/run.sh && ./script/run.sh
```

### Windows

1. 克隆项目并切换到项目根目录

如果使用 **PowerShell 5**:

```bash
git clone https://github.com/NorthZeroD/minecraft-pinyin.git ; cd minecraft-pinyin
```

如果使用 **CMD** 或 **PowerShell 7**:

```bash
git clone https://github.com/NorthZeroD/minecraft-pinyin.git && cd minecraft-pinyin
```

2. 执行脚本

如果使用 **Powershell**:

```bash
.\script\run.bat
```

如果使用 **CMD**:

```bash
script\run.bat
```

## 使用 - 生成Rime词库

请先[生成资源包](#使用---生成资源包)，然后进行下一步。

### Linux

更改脚本权限并执行:

```bash
chmod +x script/dict.sh && ./script/dict.sh
```

### Windows

执行脚本。

如果使用 **Powershell**:

```bash
.\script\dict.bat
```

如果使用 **CMD**:

```bash
script\dict.bat
```
