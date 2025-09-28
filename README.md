# rong2025
# Image Splitter (图片切割工具)

这是一个简单的 Python 脚本，用于将一张图片平均切割成两部分。支持垂直（左右）和水平（上下）两种切割方式。

## 特性

-   将任何图片切割成相等的两半。
-   支持 **垂直** 切割和 **水平** 切割。
-   通过命令行操作，简单易用。
-   可以自定义输出目录。

## 安装

1.  **克隆或下载本仓库**
    ```bash
    git clone [你的仓库URL]
    cd image-splitter
    ```

2.  **安装依赖**
    本项目依赖 `Pillow` 库。通过 `pip` 安装：
    ```bash
    pip install -r requirements.txt
    ```

## 如何使用

通过命令行运行 `split_image.py` 脚本。

### 基本用法

-   **垂直切割 (默认)**

    将名为 `my_photo.jpg` 的图片垂直切割成左右两半，并保存在当前目录。

    ```bash
    python split_image.py my_photo.jpg
    ```
    输出文件将是 `my_photo_left.jpg` 和 `my_photo_right.jpg`。

-   **水平切割**

    使用 `-d` 或 `--direction` 参数来指定切割方向为 `horizontal`。

    ```bash
    python split_image.py my_photo.jpg -d horizontal
    ```
    输出文件将是 `my_photo_top.jpg` 和 `my_photo_bottom.jpg`。


### 高级用法

-   **指定输出目录**

    使用 `-o` 或 `--output` 参数来指定保存切割后图片的目录。

    ```bash
    # 创建一个名为 "output" 的文件夹来存放结果
    mkdir output

    # 运行脚本
    python split_image.py my_photo.jpg -o output
    ```
    输出文件将被保存在 `output/` 目录下。

### 帮助

查看所有可用选项：
```bash
python split_image.py -h
