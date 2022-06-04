#!/usr/bin/env python3

import importlib
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit('Usage: qarakusi.am.py <problem-number>')

    problem_id = sys.argv[1]

    print('Hello, Qarakusi.am!')
    print(f'Requested problem: {problem_id}')

    try:
        problem_module = load_problem_module(problem_id)
    except Exception as err:
        sys.exit(f'Loading problem module failed: {err}')

    problem_module.run()


def load_problem_module(problem_id):
    module_name = f'problems.problem_{problem_id}'
    problem_module = importlib.import_module(module_name)

    return problem_module


if __name__ == '__main__':
    main()
