import re
from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser(description='Fix given SVG')
    parser.add_argument('file', help='svg file path')
    return parser.parse_args()


EMPTY_POLYGON_PATTERN = '<polygon[^>]*points=""[^>]*>'

def main(args):
    with open(args.file) as rfile:
        svg_txt = rfile.read()
    svg_txt = re.sub(EMPTY_POLYGON_PATTERN, '', svg_txt)
    with open(args.file, 'w') as wfile:
        wfile.write(svg_txt)


if __name__ == '__main__':
    main(parse_args())
