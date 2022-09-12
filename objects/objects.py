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


class Man(VMobject):
    def __init__(self, svg_index=1):
        super().__init__()

        man = SVGMobject(path_to_SVG / 'people' / 'men' / f'man_{svg_index}')
        man.set_color(WHITE)

        self.add(man)

class Woman(VMobject):
    def __init__(self, svg_index=1):
        super().__init__()

        man = SVGMobject(path_to_SVG / 'people' / 'woman' / f'woman_{svg_index}')
        man.set_color(WHITE)

        self.add(man)


class Boy(VMobject):
    def __init__(self, svg_index=1):
        super().__init__()

        boy = SVGMobject(
            path_to_SVG / 'people' / 'children' / f'boy_{svg_index}'
        )
        boy.set_color(WHITE)

        self.add(boy)


class Girl(VMobject):
    def __init__(self, svg_index=1):
        super().__init__()

        girl = SVGMobject(
            path_to_SVG / 'people' / 'children' / f'girl_{svg_index}'
        )
        girl.set_color(WHITE)

        self.add(girl)


class Pigeon(VMobject):
    def __init__(self):
        super().__init__()
        pigeon = SVGMobject(path_to_SVG / 'animals' / 'pigeon')
        pigeon.set_color(WHITE).scale(0.5)

        self.add(pigeon)


class Rabbit(VMobject):
    def __init__(self):
        super().__init__()
        rabbit = SVGMobject(path_to_SVG / 'animals' / 'rabbit')
        rabbit.set_color(WHITE).scale(0.55)

        self.add(rabbit)

class Duck(VMobject):
    def __init__(self):
        VMobject.__init__(self)
        duck = SVGMobject(path_to_SVG / 'animals' / 'duck')
        duck.scale(0.5)

        self.add(duck)

class Goose(VMobject):
    def __init__(self):
        VMobject.__init__(self)
        goose = SVGMobject(path_to_SVG / 'animals' / 'goose')
        goose.scale(0.6)

        self.add(goose)


class Cage(VMobject):
    def __init__(self, style='square'):
        super().__init__()

        if style == 'square':
            cage = SVGMobject(path_to_SVG / 'cage_square')
            cage.set_color(GOLD).scale(1.5)

        if style == 'bird':
            cage = SVGMobject(path_to_SVG / 'cage_bird')
            cage.set_color(GOLD).scale(2)

        self.add(cage)

class Coin(VMobject):
    def __init__(self):
        super().__init__()
        coin = SVGMobject(path_to_SVG / 'coins' / '20dram')
        self.add(coin)


class OpenScissors(VMobject):
    def __init__(self):
        super().__init__()
        open_scissors = SVGMobject(
            (path_to_SVG / 'scissors' / 'open_scissors').as_posix()
        )
        open_scissors.set_color(WHITE).rotate(PI/10).scale(0.5)

        self.add(open_scissors)


class ClosedScissors(VMobject):
    def __init__(self):
        super().__init__()
        closed_scissors = SVGMobject(
            path_to_SVG / 'scissors' / 'closed_scissors'
        )
        closed_scissors.set_color(WHITE).scale(0.4).rotate(PI/5)

        self.add(closed_scissors)

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
        self.move_to(p_end).shift(0.5*DOWN)
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
                        path_to_SVG /
                        'thinking_bubbles'
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


class Book(VMobject):
    def __init__(self, svg_index=1):
        super().__init__()

        book = SVGMobject(path_to_SVG / 'books' / f'book_{svg_index}')
        book.set_color(WHITE)

        self.add(book)


class Pen(VMobject):
    def __init__(self):
        super().__init__()
        pen = SVGMobject(
            path_to_SVG / 'pen'
        ).set_color(WHITE).scale(0.5).rotate(PI / 7)

        self.add(pen)


class Pencil(VMobject):
    def __init__(self, svg_index=1):
        super().__init__()

        pencil = SVGMobject(path_to_SVG / 'pencils' / f'pencil_{svg_index}')
        pencil.scale(0.6).rotate(PI / 12)
        pencil.set_color(WHITE)

        self.add(pencil)


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


class House(VMobject):
    def __init__(self):
        super().__init__()
        house = SVGMobject(path_to_SVG / 'house').set_color(WHITE)

        self.add(house)


class VideoIcon(VMobject):
    def __init__(self):
        super().__init__()
        video_icon = SVGMobject(path_to_SVG / 'video_icon').set_color(WHITE)

        self.add(video_icon)


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

        self.weight = VGroup(
            SVGMobject(path_to_SVG / 'weight').set_color(WHITE).scale(0.5),
            MathTex(f"{kg:,}".replace(',', '.'),
                    color=BLACK, font_size=100 / (np.log10(kg)+1)).shift(0.1 * DOWN)
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


class EmptyBag(VMobject):
    def __init__(self, svg_index=1):
        super().__init__()

        empty_bag = SVGMobject(
            path_to_SVG / 'bags' / f'empty_bag_{svg_index}'
        )

        self.add(empty_bag)


class BucketOfMandarins(VMobject):
    def __init__(self):
        super().__init__()

        bucket_of_mandarins = SVGMobject(
            path_to_SVG / 'fruits' / 'bucket_of_mandarins'
        )
        bucket_of_mandarins.scale(0.4)

        self.add(bucket_of_mandarins)


class Apple(VMobject):
    def __init__(self, color=GREEN):
        super().__init__()

        if color == GREEN:
            apple = SVGMobject(path_to_SVG / 'fruits' / 'green_apple')

        elif color == RED:
            apple = SVGMobject(path_to_SVG / 'fruits' / 'red_apple')

        apple.scale(0.25)

        self.add(apple)


class Mushroom(VMobject):
    def __init__(self):
        super().__init__()

        mushroom = SVGMobject(path_to_SVG / 'fruits' / 'mushroom')
        mushroom.scale(0.25)

        self.add(mushroom)


class Tomato(VMobject):
    def __init__(self):
        super().__init__()

        tomato = SVGMobject(path_to_SVG / 'fruits' / 'tomato')
        tomato.scale(0.25)

        self.add(tomato)


class Carrot(VMobject):
    def __init__(self):
        super().__init__()

        carrot = SVGMobject(path_to_SVG / 'fruits' / 'carrot')
        carrot.scale(0.25)

        self.add(carrot)


class Banana(VMobject):
    def __init__(self):
        super().__init__()

        banana = SVGMobject(path_to_SVG / 'fruits' / 'banana')
        banana.scale(0.25)

        self.add(banana)


class Pear(VMobject):
    def __init__(self):
        super().__init__()

        pear = SVGMobject(path_to_SVG / 'fruits' / 'pear')
        pear.scale(0.25)

        self.add(pear)


class Mandarin(VMobject):
    def __init__(self):
        super().__init__()

        mandarin = SVGMobject(path_to_SVG / 'fruits' / 'mandarin')

        self.add(mandarin)


class Mandarins(VMobject):
    def __init__(self):
        super().__init__()

        mandarins = SVGMobject(path_to_SVG / 'fruits' / 'mandarins')
        mandarins.scale(0.35)

        self.add(mandarins)


class ScaleStar(VMobject):
    def __init__(self):
        super().__init__()

        star = SVGMobject(path_to_SVG / 'star').set_stroke(width=0)
        star.scale(0.25)

        self.add(star)


class Scissors:
    def __init__(self, cut_coordinate=ORIGIN, style=1):
        self.style = style

        if style == 1:
            self.open_scissors = OpenScissors()
            self.closed_scissors = ClosedScissors()
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
            scissor_1 = SVGMobject(
                path_to_SVG / 'scissors' / 'scissors_1'
            ).set_color(WHITE)

            scissor_2 = SVGMobject(
                path_to_SVG / 'scissors' / 'scissors_2'
            ).set_color(WHITE)

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
                color = Color(hue=1, saturation=t/3, luminance=1 - t)
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
        self.stopwatch_arrow = SVGMobject(path_to_SVG / 'stopwatch' /'stopwatch_arow.svg')
        self.stopwatch_resetter = SVGMobject(path_to_SVG / 'stopwatch' / 'stopwatch_resetter.svg').set_color(WHITE).scale(0.3)
        self.__aligning()
        vmobjects = [self.stopwatch, self.stopwatch_arrow, self.stopwatch_resetter]
        super().__init__(*vmobjects, **kwargs)
    
    def __aligning(self):
        self.stopwatch_arrow.move_to(self.stopwatch.get_center()).shift(0.48*UP+0.01*RIGHT)
        self.stopwatch_resetter.next_to(self.stopwatch, UP, buff=0.05)
    def speedup(self, ratio:float):
        self.__speed *= ratio
    def set_time(self, value = 0):
        self.time.set_value(value=value)
        self.stopwatch_arrow.rotate(
            2 * value/60 * PI,
            axis=OUT,
            about_point=self.stopwatch.get_center()
        )


