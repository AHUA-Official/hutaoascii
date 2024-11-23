import argparse
import cv2
import numpy as np


def get_args():
    parser = argparse.ArgumentParser("Image to ASCII")
    parser.add_argument("--input", type=str, default="data/furina-23.jpg", help="Path to input image")
    parser.add_argument("--mode", type=str, default="simple", choices=["simple", "complex"],
                        help="10 or 70 different characters")
    parser.add_argument("--num_cols", type=int, default=1500, help="number of character for output's width")
    args = parser.parse_args()
    return args


def rgb_to_ansi(r, g, b):
    """
    将 RGB 颜色转换为 ANSI 转义序列
    """
    return f"\033[38;2;{r};{g};{b}m"


def main(opt):
    if opt.mode == "simple":
        CHAR_LIST = '@%#*+=-:. '
    else:
        CHAR_LIST = r'$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`\'. '

       # CHAR_LIST = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\()1{}[]?-_+~<>i!lI;:,\"^`\'.'

    num_chars = len(CHAR_LIST)
    num_cols = opt.num_cols
    image = cv2.imread(opt.input)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    height, width, _ = image.shape
    cell_width = width / opt.num_cols
    cell_height = 2 * cell_width
    num_rows = int(height / cell_height)
    if num_cols > width or num_rows > height:
        print("Too many columns or rows. Use default setting")
        cell_width = 6
        cell_height = 12
        num_cols = int(width / cell_width)
        num_rows = int(height / cell_height)

    for i in range(num_rows):
        for j in range(num_cols):
            # 获取部分图像
            partial_image = image[
                int(i * cell_height):min(int((i + 1) * cell_height), height),
                int(j * cell_width):min(int((j + 1) * cell_width), width),
                :
            ]
            # 计算部分图像的平均颜色
            avg_color = np.mean(partial_image, axis=(0, 1)).astype(int)
            r, g, b = avg_color
            # 计算平均亮度并选择合适的字符
            avg_brightness = np.mean(avg_color)
            char = CHAR_LIST[min(int(avg_brightness * num_chars / 255), num_chars - 1)]
            # 直接在终端中打印带有 ANSI 转义序列的字符
            print(f"{rgb_to_ansi(r, g, b)}{char}\033[0m", end='')
        print()  # 换行


if __name__ == '__main__':
    opt = get_args()
    main(opt)