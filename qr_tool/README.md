# 本地二维码工具

一个简洁的本地二维码生成与解析工具。

## 功能

- **生成二维码**: 输入文字/链接生成二维码图片
- **解析二维码**: 上传图片自动识别其中的二维码内容

## 安装

```bash
cd qr_tool
pip install -r requirements.txt
```

**注意**: 解析二维码需要安装 zbar 库:

- **Ubuntu/Debian**: `sudo apt-get install libzbar0`
- **CentOS/RHEL**: `sudo yum install zbar-devel`
- **macOS**: `brew install zbar`
- **Windows**: 安装 prebuilt wheels 或使用 conda

## 运行

```bash
python main.py
```

## 使用

1. **生成二维码**: 在左侧输入框输入内容，点击"生成二维码"
2. **保存二维码**: 点击"保存二维码"按钮保存到本地
3. **解析二维码**: 在右侧点击"上传图片"，选择二维码图片，自动显示解析结果
