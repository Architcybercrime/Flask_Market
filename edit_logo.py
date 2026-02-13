#!/usr/bin/env python3
"""
Simple logo text replacer using Pillow.
Usage:,..
  python edit_logo.py input_image.png --text "ARCHITSHAPEDCODING" --output out.png
If you don't pass text, it defaults to replacing the first 3 letters with 'ARCHIT' (i.e. ARCHITSHAPEDCODING).
"""
import sys
import os
import argparse

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print('\nERROR: The Pillow library is required to run this script.')
    print('Install it in your active environment with:')
    print('  pip install Pillow')
    print('Or install all requirements:')
    print('  pip install -r requirements.txt\n')
    sys.exit(1)

COMMON_FONTS = [
    r"C:\Windows\Fonts\arialbd.ttf",
    r"C:\Windows\Fonts\arial.ttf",
    r"/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    r"/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]


def find_font(preferred_size):
    for path in COMMON_FONTS:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, preferred_size)
            except Exception:
                continue
    return ImageFont.load_default()


def main():
    p = argparse.ArgumentParser()
    p.add_argument('input', help='Path to input image')
    p.add_argument('--text', '-t', default=None, help='Full text to write')
    p.add_argument('--output', '-o', default=None, help='Output path')
    p.add_argument('--fontsize', type=int, default=0, help='Force font size')
    args = p.parse_args()

    if not os.path.exists(args.input):
        print('Input file not found:', args.input)
        sys.exit(1)

    img = Image.open(args.input).convert('RGBA')
    w, h = img.size

    # default new text: replace leading 'JIM' or just use provided text
    if args.text:
        new_text = args.text
    else:
        # try to preserve rest of text if visible
        new_text = 'ARCHITSHAPEDCODING'

    # pick font size relative to image width
    fontsize = args.fontsize if args.fontsize > 0 else max(18, w // 10)
    font = find_font(fontsize)

    draw = ImageDraw.Draw(img)

    # measure text size
    text_w, text_h = draw.textsize(new_text, font=font)

    # approximate position: horizontally centered; vertically near top third (adjustable)
    x = (w - text_w) // 2
    y = int(h * 0.18)

    # sample background color from image center (assumes circular badge)
    try:
        bg_color = img.getpixel((w//2, h//2))
    except Exception:
        bg_color = (0, 0, 0, 255)

    # if bg_color has alpha, convert to RGB tuple for rectangle fill
    if isinstance(bg_color, tuple) and len(bg_color) == 4:
        rect_fill = bg_color
    else:
        rect_fill = bg_color

    padding_x = max(10, text_w // 20)
    padding_y = max(6, text_h // 6)

    # draw rectangle behind text to hide previous text
    rect = (x - padding_x, y - padding_y, x + text_w + padding_x, y + text_h + padding_y)

    overlay = Image.new('RGBA', img.size, (255,255,255,0))
    o_draw = ImageDraw.Draw(overlay)
    o_draw.rectangle(rect, fill=rect_fill)

    # paste overlay onto image
    img = Image.alpha_composite(img, overlay)

    # draw text in white (or choose contrasting color if bg is light)
    # decide text color based on bg brightness
    r, g, b = rect_fill[0], rect_fill[1], rect_fill[2]
    brightness = (r*299 + g*587 + b*114) / 1000
    text_color = (0,0,0,255) if brightness > 160 else (255,255,255,255)

    draw = ImageDraw.Draw(img)
    draw.text((x, y), new_text, font=font, fill=text_color)

    out_path = args.output if args.output else os.path.splitext(args.input)[0] + '_archit.png'
    img.convert('RGB').save(out_path)
    print('Saved edited image to', out_path)


if __name__ == '__main__':
    main()
