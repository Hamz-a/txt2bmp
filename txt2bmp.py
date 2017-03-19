#!/usr/bin/env python
import argparse
import math
from PIL import Image


def txt2rgb(text):
    # Add NULL bytes and new lines
    prepend = "\x00\r\n\r\n"
    formed_string = prepend + text + "\x00"

    pixel_len = math.ceil(len(formed_string) / 3)  # 3 rgb values per pixel
    width = math.ceil(math.sqrt(pixel_len))
    width = math.ceil(
        width / 4) * 4  # Make width a multiple of 4 to prevent a byte being added for the 4-byte alignment
    height = math.ceil(pixel_len / width)

    while len(formed_string) != (width * height * 3):  # Padding
        formed_string += "\x00"

    offset = 0
    matrix = [[0 for x in range(width)] for y in range(height)]
    for y in range(height - 1, -1, -1):  # Loop from the bottom to top
        for x in range(0, width):  # Loop from left to right
            r = ord(formed_string[offset + 2])
            g = ord(formed_string[offset + 1])
            b = ord(formed_string[offset])
            matrix[y][x] = (r, g, b)
            offset += 3

    return matrix


def matrix2rep(matrix):
    height = len(matrix)
    width = len(matrix[0])
    representation = "Width={}, height={}\n".format(width, height)
    for y in range(height):
        for x in range(width):
            r, g, b = matrix[y][x]
            representation += "rgb({0: >3}, {1: >3}, {2: >3})  ".format(r, g, b)
        representation += "\n"
    return representation


def matrix2bmp(matrix, filename):
    height = len(matrix)
    width = len(matrix[0])
    im = Image.new("RGB", (width, height))
    pixels = im.load()

    for y in range(height):
        for x in range(width):
            # r, g, b = matrix[y][x]
            pixels[x, y] = matrix[y][x]

    try:
        im.save(filename, "bmp")
    except:
        return False
    return True


def get_text(args):
    if args.input is not None:
        return args.input
    else:
        try:
            with open(args.file, "r") as f:
                return f.read()
        except:
            print("Can't read file.")
            return False


def main():
    argument_parser = argparse.ArgumentParser(description="Convert text to bmp.")
    group = argument_parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-i", "--input", type=str, help="Input text from cli")
    group.add_argument("-f", "--file", type=str, help="Input text from file")
    argument_parser.add_argument("-b", "--bitmap", type=str, help="Save image as bitmap")
    argument_parser.add_argument("-t", "--text", type=str, help="Save rgb values to file")
    argument_parser.add_argument("-p", "--pixels", help="Print RGB values")
    args = argument_parser.parse_args()

    text = get_text(args)
    if text is not False:
        matrix = txt2rgb(text)
        if args.bitmap is not None:
            if matrix2bmp(matrix, args.bitmap):
                print("Saved as bitmap in: {}".format(args.bitmap))
            else:
                print("Failed to save as bitmap...")
        elif args.text is not None:
            try:
                with open(args.text, "w") as f:
                    f.write(matrix2rep(matrix))
                print("Saved as text in: {}".format(args.text))
            except:
                print("Failed to save as text...")
        else:
            print(matrix2rep(matrix))


if __name__ == "__main__":
    main()
