#!/usr/bin/env python3

import importlib
import sys
import os

from constants import LanguageConfig


def main():
    if len(sys.argv) != 2:
        sys.exit('Usage: qarakusi.am.py <problem-number>')

    problem_id = sys.argv[1]

    language = os.environ.get('LANGUAGE')
    if language:
        LanguageConfig.set_language(language)

    print('Hello, Qarakusi.am!')
    print(f'Requested problem: {problem_id}')

    try:
        scene = load_problem_scene(problem_id)
    except Exception as err:
        sys.exit(f'Loading problem module failed: {err}')

    scene.render(True)


def load_problem_scene(problem_id):
    module_name = (
        f'problems.enumerated.problem_{problem_id}.problem_{problem_id}'
    )
    problem_module = importlib.import_module(module_name)

    sceneClass = getattr(problem_module, f'Problem{problem_id}')
    return sceneClass()


if __name__ == '__main__':
    main()
