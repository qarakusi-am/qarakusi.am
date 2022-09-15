import os
import subprocess
from pathlib import Path


def main():
    enumerated_problems = Path('scenes/enumerated')
    for path in enumerated_problems.glob('problem_*'):
        index = path.name[len('problem_'):]
        if not all(i.isdigit() for i in index):
            print('invalid path:', path)
            continue
        for language in ['armenian', 'english']:
            subprocess.run(['python', 'qarakusi.am.py', index,
                            '-ql', '--language', language],
                            env=os.environ)


if __name__ == '__main__':
    main()
