#!/usr/bin/env python3

from imp import load_source
import importlib
from json import load
from statistics import multimode
import sys
from pathlib import Path

import click
from manim import config, error_console
from manim.cli.render.ease_of_access_options import ease_of_access_options
from manim.cli.render.global_options import global_options
from manim.cli.render.output_options import output_options
from manim.cli.render.render_options import render_options
from manim import Scene

from constants import LanguageConfig


@click.command()
@click.argument("problem_id", type=str, required=True)
@click.option("--scene-class",
              type=str,
              required=False,
              help="Scene class name")
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
    scene_class=None,
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
        if '/' in kwargs['problem_id'] or '\\' in kwargs['problem_id']:
            file_path = kwargs['problem_id'].replace(
                '\\', '.').replace(
                '/', '.')
            if file_path.endswith('.py'):
                file_path = file_path[:-3]
            if not file_path.startswith('scenes.'):
                raise ValueError('Invalid file path given')
            scene = load_scene(importlib.import_module(file_path), scene_class, True)
        else:
            scene = load_problem_scene(kwargs['problem_id'], scene_class)
    except Exception as err:
        sys.exit(f'Loading problem module failed: {err}')

    try:
        scene.render(True)
    except Exception:
        error_console.print_exception()
        sys.exit(1)

    return kwargs


def load_problem_scene(problem_id, scene_class_name):
    module_name = (
        f'scenes.enumerated.problem_{problem_id}.problem_{problem_id}'
    )
    problem_module = importlib.import_module(module_name)
    prefix = False
    if scene_class_name is None:
        scene_class_name = f'Problem{problem_id}'
        prefix = True
    return load_scene(problem_module, scene_class_name, prefix)


def load_scene(module, scene_class_name, prefix=False):
    if scene_class_name is None:
        scene_class_name = ''
    if prefix:
        scene_names = [key for key in dir(module)
                       if key.startswith(scene_class_name)
                       and isinstance(getattr(module, key), type)
                       and getattr(module, key) is not Scene
                       and issubclass(getattr(module, key), Scene)]
        if len(scene_names) == 0:
            raise Exception('No scene found')
        elif len(scene_names) == 1:
            scene_class_name = scene_names[0]
        else:
            print_lst = ['Several Scenes found'] + [
                f'[{ind+1}] {name}'
                for ind, name in enumerate(scene_names)
            ] + ['', 'Which one do you want to render? (type the index only)']

            print('\n'.join(print_lst), flush=True)
            ind = None
            try:
                ind = int(input()) - 1
                if ind not in range(len(scene_names)):
                    ind = None
            except Exception:
                pass
            if ind is None:
                raise Exception('Wrong scene index inputted')
            scene_class_name = scene_names[ind]
    sceneClass = getattr(module, scene_class_name)
    return sceneClass()


if __name__ == '__main__':
    render()
