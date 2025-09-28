# split_image.py

import os
from PIL import Image
import argparse

def split_image(image_path, output_dir='.', direction='vertical'):
    """
    将一张图片切割成两部分并保存.

    :param image_path: 输入图片的路径.
    :param output_dir: 切割后图片的保存目录.
    :param direction: 切割方向 ('vertical' 或 'horizontal').
    """
    try:
        # 打开图片文件
        img = Image.open(image_path)
        width, height = img.size
        
        # 获取文件名和扩展名，用于生成新的文件名
        base_name = os.path.basename(image_path)
        name, ext = os.path.splitext(base_name)

        # 确保输出目录存在
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"创建目录: {output_dir}")

        if direction == 'vertical':
            # 垂直切割（左右两半）
            print("正在进行垂直切割...")
            mid_point = width // 2
            
            # 定义左半部分的切割区域: (左, 上, 右, 下)
            box1 = (0, 0, mid_point, height)
            part1 = img.crop(box1)
            
            # 定义右半部分的切割区域
            box2 = (mid_point, 0, width, height)
            part2 = img.crop(box2)
            
            # 保存文件
            output_path1 = os.path.join(output_dir, f"{name}_left{ext}")
            output_path2 = os.path.join(output_dir, f"{name}_right{ext}")

        elif direction == 'horizontal':
            # 水平切割（上下两半）
            print("正在进行水平切割...")
            mid_point = height // 2
            
            # 定义上半部分的切割区域
            box1 = (0, 0, width, mid_point)
            part1 = img.crop(box1)
            
            # 定义下半部分的切割区域
            box2 = (0, mid_point, width, height)
            part2 = img.crop(box2)
            
            # 保存文件
            output_path1 = os.path.join(output_dir, f"{name}_top{ext}")
            output_path2 = os.path.join(output_dir, f"{name}_bottom{ext}")
        
        else:
            print(f"错误: 无效的切割方向 '{direction}'. 请选择 'vertical' 或 'horizontal'.")
            return

        part1.save(output_path1)
        part2.save(output_path2)
        
        print(f"图片已成功切割并保存为:")
        print(f"- {output_path1}")
        print(f"- {output_path2}")

    except FileNotFoundError:
        print(f"错误: 找不到文件 '{image_path}'")
    except Exception as e:
        print(f"处理图片时发生错误: {e}")


if __name__ == "__main__":
    # 使用 argparse 创建一个命令行接口
    parser = argparse.ArgumentParser(description="将一张图片切割成两部分。")
    
    # 添加必须的参数：图片路径
    parser.add_argument("image_path", type=str, help="需要切割的图片文件路径。")
    
    # 添加可选参数
    parser.add_argument("-d", "--direction", type=str, default="vertical", choices=['vertical', 'horizontal'],
                        help="切割方向: 'vertical' (垂直) 或 'horizontal' (水平)。默认为 'vertical'。")
    parser.add_argument("-o", "--output", type=str, default=".",
                        help="切割后图片的输出目录。默认为当前目录。")
                        
    args = parser.parse_args()
    
    # 调用主函数
    split_image(args.image_path, args.output, args.direction)
