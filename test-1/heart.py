#!/usr/bin/env python3
"""
heart.py

在终端打印心形字符图案。支持调整宽度、高度与填充字符。

用法示例:
    python heart.py --width 60 --height 30 --char "*"

"""
import argparse


def draw_heart(width=60, height=30, char='*'):
    """绘制心形：使用隐式方程 (x^2 + y^2 - 1)^3 - x^2 * y^3 <= 0。"""
    for i in range(height, -height - 1, -1):
        y = i / float(height)
        line = []
        for j in range(-width, width + 1):
            x = j / float(width)
            value = (x * x + y * y - 1) ** 3 - (x * x) * (y ** 3)
            if value <= 0:
                line.append(char)
            else:
                line.append(' ')
        print(''.join(line))


def main():
    parser = argparse.ArgumentParser(description='打印心形字符图案')
    parser.add_argument('--width', '-W', type=int, default=60, help='水平分辨率（越大越宽）')
    parser.add_argument('--height', '-H', type=int, default=30, help='垂直分辨率（越大越高）')
    parser.add_argument('--char', '-c', type=str, default='*', help='填充字符（只取第一个字符）')
    args = parser.parse_args()
    ch = args.char[0] if args.char else '*'
    draw_heart(width=args.width, height=args.height, char=ch)


if __name__ == '__main__':
    main()
