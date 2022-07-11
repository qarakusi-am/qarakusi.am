#!/usr/bin/env python3

import importlib
import sys
from pathlib import Path

import click
from manim import config, error_console
from manim.cli.render.ease_of_access_options import ease_of_access_options
from manim.cli.render.global_options import global_options
from manim.cli.render.output_options import output_options
from manim.cli.render.render_options import render_options

from constants import LanguageConfig


@click.command()
@click.argument("problem_id", type=str, required=True)
@click.option("--language",
              default='armenian',
              show_default=True,
              help="Language of the rendered video",
              type=click.Choice(['armenian', 'english'],
                                case_sensitive=False))
@global_options
@output_options
@render_options
@ease_of_access_options
def render(
    *,
    language='armenian',
    **kwargs
):
    """Render SCENE from the file corresponding to problem_id.

    problem_id is the id of the progblem, e.g. `10674`.
    """

    kwargs['file'] = Path()
    kwargs['scene_names'] = []

    class ClickArgs:
        def __init__(self, args):
            for name in args:
                setattr(self, name, args[name])

        def _get_kwargs(self):
            return list(self.__dict__.items())

        def __eq__(self, other):
            if not isinstance(other, ClickArgs):
                return NotImplemented
            return vars(self) == vars(other)

        def __contains__(self, key):
            return key in self.__dict__

        def __repr__(self):
            return str(self.__dict__)

    click_args = ClickArgs(kwargs)

    if kwargs["jupyter"]:
        return click_args

    config.digest_args(click_args)

    LanguageConfig.set_language(language)

    print('Hello, Qarakusi.am!')

    try:
        scene = load_problem_scene(kwargs['problem_id'])
    except Exception as err:
        sys.exit(f'Loading problem module failed: {err}')

    try:
        scene.render(True)
    except Exception:
        error_console.print_exception()
        sys.exit(1)

    return kwargs


def load_problem_scene(problem_id):
    module_name = (
        f'problems.enumerated.problem_{problem_id}.problem_{problem_id}'
    )
    problem_module = importlib.import_module(module_name)

    sceneClass = getattr(problem_module, f'Problem{problem_id}')
    return sceneClass()


if __name__ == '__main__':
    render()
