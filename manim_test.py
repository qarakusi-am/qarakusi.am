import os
import subprocess
from pathlib import Path
from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser(
        description='run all problems in scenes/enumerated'
    )
    parser.add_argument('--last-screen', action='store_true')
    return parser.parse_args()


def main(args):
    enumerated_problems = Path('scenes/enumerated')
    extra_args = []
    if args.last_screen:
        extra_args.append('-s')
    for path in enumerated_problems.glob('problem_*'):
        index = path.name[len('problem_'):]
        if not all(i.isdigit() for i in index):
            print('invalid path:', path)
            continue
        for language in ['armenian', 'english']:
            subprocess.run(['python', 'qarakusi.am.py', index,
                            '-ql', '--language', language] + extra_args,
                            env=os.environ)


if __name__ == '__main__':
    main(parse_args())
