from pathlib import Path

import numpy as np
from manim import linear, MathTex
from manim import VMobject, VGroup, ValueTracker, Scene
from manim import Dot, Rectangle
from manim import RED, WHITE, BLACK, GOLD, GREEN
from manim import RIGHT, DOWN, UP, ORIGIN, OUT, PI
from manim import FadeIn, UpdateFromAlphaFunc
from manim import SVGMobject as OriginalSVGMobject
from manim import always_redraw
from colour import Color

from constants import DEFAULT_PAPERS_BUFF

white_chess_figures_fill_color = WHITE
white_chess_figures_stroke_color = BLACK
black_chess_figures_fill_color = BLACK
black_chess_figures_stroke_color = WHITE
chess_figures_stroke_width = 2.5
chess_figures_scale_factor = 0.3

objects_directory = Path(__file__).parent
path_to_SVG = objects_directory / 'SVG_files'


class SVGMobject(OriginalSVGMobject):
    def __init__(self, path, *args, **kwargs):
        if isinstance(path, Path):
            path = path.as_posix()
        super().__init__(path, *args, **kwargs)


class Defaults:
    def __init__(self):
        self.prefix_defaults = {}
        self.fixed_defaults = {}

    @staticmethod
    def _set(key: str, values: dict, defaults: dict):
        if key not in defaults:
            defaults[key] = {}
        defaults[key].update(values)

    def add_prefix_default(self, prefix: str, values: dict):
        self._set(prefix, values, self.prefix_defaults)

    def add_default(self, name: str, values: dict):
        self._set(name, values, self.fixed_defaults)

    def get_defaults(self, name):
        defaults = {
            'folder': path_to_SVG
        }

        if name in self.fixed_defaults:
            defaults.update(self.fixed_defaults[name])
            return defaults
        for key in self.prefix_defaults:
            if name.startswith(key):
                defaults.update(self.prefix_defaults[key])
                return defaults
        return defaults


svg_defaults = Defaults()
svg_defaults.add_prefix_default(
    'man_',
    {'folder': path_to_SVG / 'people' / 'men',
     'color': WHITE})
svg_defaults.add_prefix_default(
    'woman_',
    {'folder': path_to_SVG / 'people' / 'woman',
     'color': WHITE})
svg_defaults.add_prefix_default(
    'city_',
    {'folder': path_to_SVG / 'cities'})
svg_defaults.add_prefix_default(
    'boy_',
    {'folder': path_to_SVG / 'people' / 'children',
     'color': WHITE})
svg_defaults.add_prefix_default(
    'girl_',
    {'folder': path_to_SVG / 'people' / 'children',
     'color': WHITE})
svg_defaults.add_default(
    'pigeon',
    {'folder': path_to_SVG / 'animals',
     'scale': 0.5,
     'color': WHITE})
svg_defaults.add_default(
    'hippo',
    {'folder': path_to_SVG / 'animals',
     'scale': 0.5})
svg_defaults.add_default(
    'rabbit',
    {'folder': path_to_SVG / 'animals',
     'scale': 0.55,
     'color': WHITE})
svg_defaults.add_default(
    'duck',
    {'folder': path_to_SVG / 'animals',
     'scale': 0.5, })
svg_defaults.add_default(
    'goose',
    {'folder': path_to_SVG / 'animals',
     'scale': 0.5})
svg_defaults.add_default(
    'cage_square',
    {'scale': 1.5,
     'color': GOLD})
svg_defaults.add_default(
    'small_car',
    {'scale': 0.2,
     'color': RED})
svg_defaults.add_default(
    'cage_bird',
    {'scale': 2,
     'color': GOLD})
svg_defaults.add_prefix_default(
    'empty_bag_',
    {'folder': path_to_SVG / 'bags'})
svg_defaults.add_default(
    'bucket_of_mandarins',
    {'folder': path_to_SVG / 'fruits',
     'scale': 0.4})
svg_defaults.add_default(
    'green_apple',
    {'folder': path_to_SVG / 'fruits',
     'scale': 0.25})
svg_defaults.add_default(
    'red_apple',
    {'folder': path_to_SVG / 'fruits',
     'scale': 0.25})
svg_defaults.add_default(
    'mushfroom',
    {'folder': path_to_SVG / 'fruits',
     'scale': 0.25})
svg_defaults.add_default(
    'tomato',
    {'folder': path_to_SVG / 'fruits',
     'scale': 0.25})
svg_defaults.add_default(
    'carrot',
    {'folder': path_to_SVG / 'fruits',
     'scale': 0.25})
svg_defaults.add_default(
    'banana',
    {'folder': path_to_SVG / 'fruits',
     'scale': 0.25})
svg_defaults.add_default(
    'pear',
    {'folder': path_to_SVG / 'fruits',
     'scale': 0.25})
svg_defaults.add_default(
    'mandarin',
    {'folder': path_to_SVG / 'fruits'})
svg_defaults.add_default(
    '20dram',
    {'folder': path_to_SVG / 'coins'})
svg_defaults.add_default(
    'mandarins',
    {'folder': path_to_SVG / 'fruits',
     'scale': 0.35})
svg_defaults.add_prefix_default(
    'book_',
    {'folder': path_to_SVG / 'books',
     'color': WHITE})
svg_defaults.add_default(
    'house',
    {'color': WHITE})
svg_defaults.add_default(
    'video_icon',
    {'color': WHITE})
svg_defaults.add_default(
    'pen',
    {'rotate': PI / 7,
     'scale': 0.5,
     'color': WHITE})
svg_defaults.add_prefix_default(
    'pencil_',
    {'folder': path_to_SVG / 'pencils',
     'scale': 0.6,
     'rotate': PI / 12,
     'color': WHITE})
svg_defaults.add_default(
    'open_scissors',
    {'folder': path_to_SVG / 'scissors',
     'scale': 0.5,
     'rotate': PI / 10,
     'color': WHITE})
svg_defaults.add_default(
    'closed_scissors',
    {'folder': path_to_SVG / 'scissors',
     'scale': 0.4,
     'rotate': PI / 5,
     'color': WHITE})
svg_defaults.add_prefix_default(
    'scissors_',
    {'folder': path_to_SVG / 'scissors'})
svg_defaults.add_default(
    'tennis_ball',
    {'folder': path_to_SVG,
     'scale': 0.5})
svg_defaults.add_default(
    'locust',
    {'folder': path_to_SVG / 'animals'})
svg_defaults.add_default(
    'thinking_boy_outlines',
    {'folder': path_to_SVG / 'people' / 'thinking'})
svg_defaults.add_default(
    'big_pool',
    {'folder': path_to_SVG / 'pool'})
svg_defaults.add_default(
    'small_pool',
    {'folder': path_to_SVG / 'pool'})


class SimpleSVGMobject(VMobject):
    def __init__(self, obj_name: str,
                 *,
                 scale: float = None,
                 rotate: float = None,
                 color=None):
        super().__init__()

        defaults = svg_defaults.get_defaults(obj_name)
        if scale is None:
            scale = defaults.get('scale')
        if color is None:
            color = defaults.get('color')
        if rotate is None:
            rotate = defaults.get('rotate')
        obj_path = (defaults['folder'] / obj_name).with_suffix('.svg')

        svg_object = SVGMobject(obj_path)
        if color is not None:
            svg_object.set_color(color)
        if scale is not None:
            svg_object.scale(scale)
        if rotate is not None:
            svg_object.rotate(rotate)
        self.add(svg_object)


class ChessFigures(VMobject):
    pawn_path = path_to_SVG / 'chess_figures' / 'pawn.svg'
    knight_path = path_to_SVG / 'chess_figures' / 'knight.svg'
    bishop_path = path_to_SVG / 'chess_figures' / 'bishop.svg'
    rook_path = path_to_SVG / 'chess_figures' / 'rook.svg'
    queen_path = path_to_SVG / 'chess_figures' / 'queen.svg'
    king_path = path_to_SVG / 'chess_figures' / 'king.svg'

    def __init__(self):
        super().__init__()

        self.white_pawn = SVGMobject(self.pawn_path)
        self.white_pawn.scale(chess_figures_scale_factor)
        self.white_pawn.set_fill(white_chess_figures_fill_color)
        self.white_pawn.set_stroke(white_chess_figures_stroke_color,
                                   chess_figures_stroke_width)

        self.black_pawn = SVGMobject(self.pawn_path)
        self.black_pawn.scale(chess_figures_scale_factor)
        self.black_pawn.set_fill(black_chess_figures_fill_color)
        self.black_pawn.set_stroke(black_chess_figures_stroke_color,
                                   chess_figures_stroke_width)

        self.white_knight = SVGMobject(self.knight_path)
        self.white_knight.scale(chess_figures_scale_factor)
        self.white_knight.set_fill(white_chess_figures_fill_color)
        self.white_knight.set_stroke(white_chess_figures_stroke_color,
                                     chess_figures_stroke_width)

        self.black_knight = SVGMobject(self.knight_path)
        self.black_knight.scale(chess_figures_scale_factor)
        self.black_knight.set_fill(black_chess_figures_fill_color)
        self.black_knight.set_stroke(black_chess_figures_stroke_color,
                                     chess_figures_stroke_width)

        self.white_bishop = SVGMobject(self.bishop_path)
        self.white_bishop.scale(chess_figures_scale_factor)
        self.white_bishop.set_fill(white_chess_figures_fill_color)
        self.white_bishop.set_stroke(white_chess_figures_stroke_color,
                                     chess_figures_stroke_width)

        self.black_bishop = SVGMobject(self.bishop_path)
        self.black_bishop.scale(chess_figures_scale_factor)
        self.black_bishop.set_fill(black_chess_figures_fill_color)
        self.black_bishop.set_stroke(black_chess_figures_stroke_color,
                                     chess_figures_stroke_width)

        self.white_rook = SVGMobject(self.rook_path)
        self.white_rook.scale(chess_figures_scale_factor)
        self.white_rook.set_fill(white_chess_figures_fill_color)
        self.white_rook.set_stroke(white_chess_figures_stroke_color,
                                   chess_figures_stroke_width)

        self.black_rook = SVGMobject(self.rook_path)
        self.black_rook.scale(chess_figures_scale_factor)
        self.black_rook.set_fill(black_chess_figures_fill_color)
        self.black_rook.set_stroke(black_chess_figures_stroke_color,
                                   chess_figures_stroke_width)

        self.white_queen = SVGMobject(self.queen_path)
        self.white_queen.scale(chess_figures_scale_factor)
        self.white_queen.set_fill(white_chess_figures_fill_color)
        self.white_queen.set_stroke(white_chess_figures_stroke_color,
                                    chess_figures_stroke_width)

        self.black_queen = SVGMobject(self.queen_path)
        self.black_queen.scale(chess_figures_scale_factor)
        self.black_queen.set_fill(black_chess_figures_fill_color)
        self.black_queen.set_stroke(black_chess_figures_stroke_color,
                                    chess_figures_stroke_width)

        self.white_king = SVGMobject(self.king_path)
        self.white_king.scale(chess_figures_scale_factor)
        self.white_king.set_fill(white_chess_figures_fill_color)
        self.white_king.set_stroke(white_chess_figures_stroke_color,
                                   chess_figures_stroke_width)

        self.black_king = SVGMobject(self.king_path)
        self.black_king.scale(chess_figures_scale_factor)
        self.black_king.set_fill(black_chess_figures_fill_color)
        self.black_king.set_stroke(black_chess_figures_stroke_color,
                                   chess_figures_stroke_width)


class DScissors(VGroup):
    def __init__(self, cut_point, **kwargs):
        self.scissor_1 = SVGMobject(
            path_to_SVG / 'scissors' / 'scissors_1.svg'
        ).set_color(WHITE)
        self.scissor_2 = SVGMobject(
            path_to_SVG / 'scissors' / 'scissors_2.svg'
        ).set_color(WHITE)
        self.dot = Dot().scale(0.2)
        super().__init__(self.scissor_1, self.scissor_2, **kwargs)
        self.arrange(RIGHT, buff=-1.1)
        self.add(self.dot)
        self.scale(0.5)
        self.scissor_1.shift(0.08 * DOWN).rotate(angle=-0.03, about_point=self.dot.get_center())
        self.scissor_2.shift(0.08 * DOWN).rotate(angle=0.03, about_point=self.dot.get_center())
        self.cut_point = np.array(cut_point)
        shift_vector = np.array([0, -0.35, 0])
        p_end = self.cut_point + shift_vector
        self.move_to(p_end).shift(0.5 * DOWN)

    def open(self, angle):
        self.scissor_1.rotate(angle=angle, about_point=self.dot.get_center())
        self.scissor_2.rotate(angle=-angle, about_point=self.dot.get_center())


class ThinkingBubble(VMobject):
    def __init__(self, smooth=True, from_left_to_right=True, style=1):
        super().__init__()

        if smooth:
            if from_left_to_right:
                if style == 1:
                    thinking_bubble = SVGMobject(
                        path_to_SVG
                        / 'thinking_bubbles'
                        / 'smooth_thinking_bubble_left_1'
                    )
                else:
                    thinking_bubble = SVGMobject(
                        path_to_SVG
                        / 'thinking_bubbles'
                        / 'smooth_thinking_bubble_left_2'
                    )
            else:
                if style == 1:
                    thinking_bubble = SVGMobject(
                        path_to_SVG
                        / 'thinking_bubbles'
                        / 'smooth_thinking_bubble_right_1'
                    )
                else:
                    thinking_bubble = SVGMobject(
                        path_to_SVG
                        / 'thinking_bubbles'
                        / 'smooth_thinking_bubble_right_2'
                    )
        else:
            if from_left_to_right:
                if style == 1:
                    thinking_bubble = SVGMobject(
                        path_to_SVG
                        / 'thinking_bubbles'
                        / 'thinking_bubble_left_1'
                    )
                    thinking_bubble = VGroup(
                        thinking_bubble[1],
                        thinking_bubble[2],
                        thinking_bubble[0]
                    )
                else:
                    thinking_bubble = SVGMobject(
                        path_to_SVG
                        / 'thinking_bubbles'
                        / 'thinking_bubble_left_2'
                    )
                    thinking_bubble = VGroup(
                        thinking_bubble[1],
                        thinking_bubble[2],
                        thinking_bubble[3],
                        thinking_bubble[0]
                    )
            else:
                if style == 1:
                    thinking_bubble = SVGMobject(
                        path_to_SVG
                        / 'thinking_bubbles'
                        / 'thinking_bubble_right_1'
                    )
                    thinking_bubble = VGroup(
                        thinking_bubble[1],
                        thinking_bubble[2],
                        thinking_bubble[0]
                    )
                else:
                    thinking_bubble = SVGMobject(
                        path_to_SVG
                        / 'thinking_bubbles'
                        / 'thinking_bubble_right_2'
                    )
                    thinking_bubble = VGroup(
                        thinking_bubble[1],
                        thinking_bubble[2],
                        thinking_bubble[3],
                        thinking_bubble[0]
                    )

        thinking_bubble.set_color(WHITE)

        self.add(thinking_bubble)


class AppleSLices(VGroup):
    def __init__(self, **kwargs):
        self.apple_ul = SVGMobject(
            path_to_SVG
            / 'fruits'
            / 'green_apple_slices'
            / 'green_apple_1.svg').set_color(GREEN)
        self.apple_dl = SVGMobject(
            path_to_SVG
            / 'fruits'
            / 'green_apple_slices'
            / 'green_apple_2.svg').set_color(GREEN)
        self.apple_ur = SVGMobject(
            path_to_SVG
            / 'fruits'
            / 'green_apple_slices'
            / 'green_apple_3.svg').set_color(GREEN)
        self.apple_dr = SVGMobject(
            path_to_SVG
            / 'fruits'
            / 'green_apple_slices'
            / 'green_apple_4.svg').set_color(GREEN)
        self.apple_ur.match_width(self.apple_dr)
        self.apple_dl.stretch_to_fit_width(self.apple_ul.width)
        self.apple_dr.stretch_to_fit_height(self.apple_dl.height + 0.03)
        super().__init__(self.apple_ul, self.apple_dl, self.apple_ur, self.apple_dr, **kwargs)
        self.arrange_in_grid(2, 2, buff=0, flow_order="dr")
        self.apple_ul.scale(1.01)
        self.apple_ur.scale(1.1)
        self.apple_ur.stretch_to_fit_height(1.05 * self.apple_ur.height)
        self.apple_ur.next_to(self.apple_dr, UP, buff=0, aligned_edge=RIGHT)
        self.apple_ul.next_to(self.apple_dl, UP, buff=0, aligned_edge=RIGHT)


class Papers(VMobject):
    def __init__(self, number_of_pages=1):
        super().__init__()

        if number_of_pages == 1:
            paper = SVGMobject(path_to_SVG / 'papers' / 'paper_1')

            self.colors = paper[0]
            self.outlines = paper[1]
            self.texts = paper[2]
            self.papers = VGroup(self.colors, self.outlines)

            # self.outlines.set_z(self.colors.get_z() + 1)
            # self.texts.set_z(self.outlines.get_z() + 1)

            self.add(self.colors, self.outlines, self.texts)
        else:
            self.colors = VGroup()
            self.outlines = VGroup()
            self.texts = VGroup()
            self.papers = VGroup()

            for i in range(number_of_pages):
                paper = Papers()
                if i > 0:
                    # paper.colors.set_z(self.texts[i - 1].get_z())
                    # paper.outlines.set_z(paper.colors.get_z() + 1)
                    # paper.texts.set_z(paper.outlines.get_z() + 1)
                    paper.move_to(self.papers[i - 1].get_center()
                                  + DEFAULT_PAPERS_BUFF * UP)

                self.colors.add(paper.colors)
                self.outlines.add(paper.outlines)
                self.texts.add(paper.texts)
                self.papers.add(paper.papers)

                self.add(paper)


class Scales(VMobject):
    def __init__(self, plate_stretch_factor=1):
        VMobject.__init__(self)

        self.plate_stretch_factor = plate_stretch_factor

        scales = SVGMobject(path_to_SVG / 'scales').scale(1.2)

        scales[0].set_color('#8c6239')
        scales[1].set_color('#764d26')
        scales[2].set_color('#603813')
        scales[3].set_color('#00786f')
        scales[4].set_color('#00a99d')
        scales[5].set_color('#8c6239').set_stroke(BLACK, 0.4)
        scales[6].set_color(BLACK)
        scales[7].set_color('#00786f')
        scales[8].set_color('#4a2c06')
        scales[9].set_color('#4a2c06')
        scales[10].set_color('#00786f')
        scales[11].set_color('#00786f')

        self.rotation_dot = scales[6]

        self.fixed_part = VGroup(scales[3], scales[4], scales[5], scales[6], scales[7])
        self.rotating_part = VGroup(scales[0], scales[1], scales[2], scales[8], scales[9])
        self.left_plate = always_redraw(lambda: scales[10].next_to(scales[8], UP, buff=0.01))
        self.right_plate = always_redraw(lambda: scales[11].next_to(scales[9], UP, buff=0.01))

        self.fixed_part.set_z_index(self.rotating_part.get_z() + 1)

        self.body = VGroup(self.rotating_part, self.fixed_part)

        self.left_plate.stretch(self.plate_stretch_factor, 0)
        self.right_plate.stretch(self.plate_stretch_factor, 0)

        self.add(self.body, self.left_plate, self.right_plate)


class Weight(VGroup):
    def __init__(self, kg=1, unit_kg=1, scale_factor=0.75):
        super().__init__()

        self.scale_factor = scale_factor
        self.weight_value = kg

        # Սա ընդամենը բազմանդամ է, որի միջոցով ընտրվում է կշռաքարի վրայի գրվող թվի չափսը՝ կախված դրա զանգվածի նիշերի քանակից
        # (առավելագույնը 4 նիշանոց թվերի համար)
        x = len(str(kg))
        polynomial = (
                20 / 6 * (x - 1) * (x - 2) * (x - 3) + 25 / (-2) *
                (x - 1) * (x - 2) * (x - 4) + 35 / 2 * (x - 1) *
                (x - 3) * (x - 4) + 45 / (-6) * (x - 2) * (x - 3) * (x - 4)
        )

        self.weight = VGroup(
            SimpleSVGMobject('weight').scale(0.5),
            MathTex(f"{kg:,}".replace(',', '.'),
                    color=BLACK, font_size=polynomial).shift(0.1 * DOWN)
        ).scale(((kg / (2 * unit_kg)) ** (1. / 3.)) * self.scale_factor)

        self.kettlebell = self.weight[0]
        self.weight_text = self.weight[1]

        # self.weight_text.match_width(self.kettlebell).scale(0.9)

        self.add(self.kettlebell, self.weight_text)


class FruitShop(VMobject):
    def __init__(self):
        super().__init__()

        shop = SVGMobject(path_to_SVG / 'fruit_shop')
        shop.scale(2)
        shop.add(Rectangle('#9e7f51', 0.5, 4.3).shift([0.07, -1.63, 0]))

        self.shelf = shop[1]
        self.add(shop)


class BagOfMandarins(VMobject):
    def __init__(self, size: str = 'normal', svg_index=1):
        super().__init__()

        if size == 'normal':
            bag_of_mandarins = SVGMobject(
                path_to_SVG / 'bags' / f'bag_with_mandarins_{svg_index}'
            )
            bag_of_mandarins.scale(0.5)
        else:
            bag_of_mandarins = SVGMobject(
                path_to_SVG / 'bags' / f'bag_with_mandarins_{svg_index}_large'
            )
            bag_of_mandarins.scale(0.66)

        self.add(bag_of_mandarins)


class ScaleStar(VMobject):
    def __init__(self):
        super().__init__()

        star = SVGMobject(path_to_SVG / 'star').set_stroke(width=0)
        star.scale(0.25)

        self.add(star)


class Checkmark(VMobject):
    def __init__(self):
        super().__init__()

        checkmark = SVGMobject(path_to_SVG / 'check')

        self.add(checkmark)


class Scissors:
    def __init__(self, cut_coordinate=ORIGIN, style=1):
        self.style = style

        if style == 1:
            self.open_scissors = SimpleSVGMobject('open_scissors')
            self.closed_scissors = SimpleSVGMobject('closed_scissors')
            self.cut_coordinate = (
                np.array(cut_coordinate)
                - np.array([0.2, 0.4, 0])
            )
            self.closed_scissors.move_to(self.cut_coordinate)
            self.open_scissors.move_to(
                self.cut_coordinate
                - np.array([0, 0.5, 0])
            )
        elif style == 2:
            self.cut_coordinate = cut_coordinate
            scissor_1 = SimpleSVGMobject('scissors_1')
            scissor_2 = SimpleSVGMobject('scissors_2')

            dot = Dot().scale(0.2)
            self.__p_end = [a + b for a, b in
                            zip([0, -0.35, 0], cut_coordinate)]
            VGroup(scissor_1, scissor_2).arrange(RIGHT, buff=0.1)
            scissor_1.shift(0.08 * DOWN + 0.6 * RIGHT)
            scissor_2.shift(0.08 * DOWN - 0.6 * RIGHT)
            scissors_with_dot = VGroup(scissor_1, scissor_2, dot).scale(0.5)
            point = scissors_with_dot[2].get_center()
            scissors_with_dot[0].rotate(angle=-0.02, about_point=point)
            scissors_with_dot[1].rotate(angle=0.02, about_point=point)
            scissors_with_dot.move_to(self.__p_end)
            scissors_with_dot.shift(DOWN)
            self.siz = scissors_with_dot

    def cut(self, scene: Scene, run_time=3):
        if self.style == 1:
            scene.play(FadeIn(self.open_scissors), run_time=run_time / 3)
            scene.wait(run_time / 9)
            scene.play(
                self.open_scissors.animate().move_to(self.cut_coordinate),
                run_time=run_time / 3
            )
            scene.wait(run_time / 9)
            scene.remove(self.open_scissors)
            scene.add(self.closed_scissors)
            scene.add_sound(objects_directory / 'sounds' / 'scissors_sound')
            scene.wait(0.25)
            scene.remove(self.closed_scissors)
            scene.add(self.open_scissors)
            scene.wait(run_time / 9)
        elif self.style == 2:
            run_time = 1

            def function_from_time(mobject, t):
                frame_rate = scene.camera.frame_rate
                dt = run_time / frame_rate
                dl = [0, dt, 0]
                if t < run_time / 2:
                    angle = PI / 8 * dt
                else:
                    angle = -PI / 8 * dt
                mobject.shift(dl)
                point = mobject[2].get_center()
                mobject[0].rotate(angle=angle, about_point=point)
                mobject[1].rotate(angle=-angle, about_point=point)

            scene.play(
                UpdateFromAlphaFunc(self.siz,
                                    function_from_time,
                                    run_time=run_time,
                                    rate_func=linear)
            )
            scene.add_sound(objects_directory / 'sounds' / 'scissors_sound')
            scene.wait(0.2)
            self.siz.move_to(self.__p_end)

    def fade_out(self, scene: Scene, run_time=1):
        if self.style == 1:
            scene.play(
                self.open_scissors.animate().move_to(
                    self.cut_coordinate
                    - np.array([0, 0.5, 0])
                ).set_opacity(0),
                run_time=run_time
            )
            scene.remove(self.open_scissors)
        elif self.style == 2:
            def function_from_time(mobject, t):
                frame_rate = scene.camera.frame_rate
                dt = run_time / frame_rate
                dl = [0, -dt, 0]
                angle = PI / 10 * dt
                mobject.shift(dl)
                point = mobject[2].get_center()
                color = Color(hue=1, saturation=t / 3, luminance=1 - t)
                mobject.set_color(color)
                mobject[0].rotate(angle=angle, about_point=point)
                mobject[1].rotate(angle=-angle, about_point=point)

            scene.play(
                UpdateFromAlphaFunc(
                    self.siz,
                    function_from_time,
                    run_time=run_time,
                    rate_func=linear
                )
            )
            scene.remove(self.siz)


class Stopwatch(VGroup):
    def __init__(self, **kwargs):
        self.__speed = 1
        self.time = ValueTracker(0)
        self.stopwatch = SVGMobject(path_to_SVG / 'stopwatch' / 'stopwatch.svg').set_color(WHITE).scale(1.8)
        self.stopwatch_arrow = SVGMobject(path_to_SVG / 'stopwatch' / 'stopwatch_arow.svg')
        self.stopwatch_resetter = SVGMobject(path_to_SVG / 'stopwatch' / 'stopwatch_resetter.svg').set_color(
            WHITE).scale(0.3)
        self.__aligning()
        vmobjects = [self.stopwatch, self.stopwatch_arrow, self.stopwatch_resetter]
        super().__init__(*vmobjects, **kwargs)

    def __aligning(self):
        self.stopwatch_arrow.move_to(self.stopwatch.get_center()).shift(0.48 * UP + 0.01 * RIGHT)
        self.stopwatch_resetter.next_to(self.stopwatch, UP, buff=0.05)

    def speedup(self, ratio: float):
        self.__speed *= ratio

    def set_time(self, value=0):
        self.time.set_value(value=value)
        self.stopwatch_arrow.rotate(
            2 * value / 60 * PI,
            axis=OUT,
            about_point=self.stopwatch.get_center()
        )


class Train(VGroup):
    def __init__(self, with_locomotive=True, passenger=True, number_of_rolling_cars=2):
        n = number_of_rolling_cars
        path_to_cars = path_to_SVG / 'train' / 'passenger_car.svg' if passenger else path_to_SVG / 'train' / 'freight_car.svg'
        path_to_locomotive = path_to_SVG / 'train' / 'locomotive.svg'
        vmobjects = [SVGMobject(path_to_cars) for _ in range(n)]
        if with_locomotive:
            vmobjects.append(SVGMobject(path_to_locomotive))
        super().__init__(*vmobjects)
        self.arrange(RIGHT, aligned_edge=DOWN)


class Car(VGroup):
    def __init__(self, index=True):
        super().__init__()
        stroke_prop = {
            'car_6': {
                'object_stokes': {16: 2}
            }
        }

        path_to_car = path_to_SVG / 'cars' / f'{index}.svg'
        car = SVGMobject(path_to_car)
        if index in stroke_prop:
            for obj_idx, stoke_width in stroke_prop[index]['object_stokes'].items():
                car[obj_idx].set_stroke(width=stoke_width)
        self.add(car)
