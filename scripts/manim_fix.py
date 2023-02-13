from pathlib import Path
from manim.mobject.svg import svg_path


def get_svg_path_file() -> Path:
    return Path(svg_path.__file__).resolve()


def main():
    path = get_svg_path_file()
    code = path.read_text()
    code = code.replace('[x1, y1, x2, y2, x2, y2]', '[[x1, y1, 0], [x2, y2, 0], [x2, y2, 0]]')
    path.write_text(code)


if __name__ == '__main__':
    main()
