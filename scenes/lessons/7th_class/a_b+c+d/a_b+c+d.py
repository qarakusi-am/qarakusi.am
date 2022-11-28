from manim import WHITE, YELLOW, ORANGE, BLUE, RED, MAROON, GOLD_A, TEAL, GREEN
from manim import MathTex, VGroup
from manim import SurroundingRectangle, Rectangle, Circle
from manim import RIGHT, LEFT, UP, DOWN, DR, UL, DR, ORIGIN
from manim import AnimationGroup, Write, Unwrite, FadeIn, FadeOut, Create, ReplacementTransform
from manim import Indicate, Circumscribe, Wiggle, TransformMatchingTex, ClockwiseTransform

import numpy as np
from colour import Color

from aramanim import ConectionLine
from hanrahashiv import FormulaModificationsScene, ModifyFormula

BIG_SCALE = 1.3
SCALE = .45


def get_tex(expression, color=WHITE):
    """
    Receives a math expression, and attempts to parse that into a Tex object.
    It's pretty basic and the main advantage is the readability of the expression.
    Avoids the dollar signs and other ugly details.
    WARNING: Don't use this for very complex formulas.
    """
    tex_list = list()
    if '$\cdot$' in expression:
        raise Exception("Please provide the dot multiply sign as '*'")
    skip_char = False
    for i, char in enumerate(expression):
        if skip_char:
            skip_char = False
            continue
        if char.isalpha():
            tex_list.append(char)
        elif char == '*':
            tex_list.append('\cdot')
        elif char == '^':
            tex_list.append(f'^{expression[i + 1]}')
            skip_char = True
        elif char == ' ':
            tex_list.append(' ')
        else:
            tex_list.append(char)

    return MathTex(*tex_list, color=color, arg_separator=' ')


def find_index(arr, val):
    """
    Given a string or an array [arr], find the index of the given char or value [val].
    Ex: find_index('a*(a+b)', 'a') -> [0, 3]
    """
    return [ind for ind, el in enumerate(arr) if el == val]


def circle(mobject, color=WHITE, stroke_width=4.5, buff=0.08):
    """
    Defines a surrounding circle for the given mobject
    """
    c = Circle(color=color, stroke_width=stroke_width).surround(mobject, buffer_factor=1)
    radius = c.width / 2
    c.scale((radius + buff) / radius)
    return c


class scene1(FormulaModificationsScene):
    def construct(self):
        self.wait()

        abc = get_tex('a b c').scale(BIG_SCALE)
        equal_sign_1 = get_tex('=', color=YELLOW)
        plus_sign_1, plus_sign_2, plus_sign_3, plus_sign_4 = (get_tex('+', color=YELLOW) for _ in range(4))

        self.form_1_str = 'a*(b+c      )=a*b+a*c            '
        self.form_2_str = 'a*(b+c+d    )=a*b+a*c+a*d        '
        self.form_3_str = 'a*(b+c+d+e+f)=a*b+a*c+a*d+a*e+a*f'
        a_idx, b_idx, c_idx, d_idx, e_idx, f_idx = [find_index(self.form_3_str, char) for char in 'abcdef']

        form_1, form_2, form_3 = [
            get_tex(form).scale(BIG_SCALE) 
            for form in [self.form_1_str, self.form_2_str, self.form_3_str]
        ]

        [form_1[i].set_color(ORANGE) for i in a_idx]
        [form_1[i].set_color(BLUE) for i in b_idx + c_idx]
        [form_2[i].set_color(ORANGE) for i in a_idx]
        [form_2[i].set_color(BLUE) for i in b_idx + c_idx + d_idx]
        [form_3[i].set_color(ORANGE) for i in a_idx]
        [form_3[i].set_color(BLUE) for i in b_idx + c_idx + d_idx + e_idx + f_idx]

        self.form_1_copy, self.form_2_copy, self.form_3_copy = [form.copy() for form in [form_1, form_2, form_3]]

        srr_rect1 = SurroundingRectangle(form_1, BLUE, buff=.2, corner_radius=.3)
        self.ex_1 = get_tex('x^2*(n+yz+6)').scale(BIG_SCALE)

        h, opc = 5, 0.7
        rect_prop = {
            1: {'h': h, 'w': 3.0, 'c': RED},
            2: {'h': h, 'w': 5.0, 'c': BLUE},
            3: {'h': h, 'w': 2.0, 'c': ORANGE},
            4: {'h': h, 'w': 2.5, 'c': MAROON},
            5: {'h': h, 'w': 3.5, 'c': GOLD_A},
        }

        rect_1, rect_2, rect_3, rect_4, rect_5 = [
            Rectangle(
                Color(WHITE),
                rect_prop[i]['h'] * SCALE,
                rect_prop[i]['w'] * SCALE,
                fill_color=rect_prop[i]['c'],
                fill_opacity=opc)
            for i in rect_prop
        ]

        rect_2.next_to(rect_1, RIGHT, buff=0)
        [rect.next_to(rect_2, RIGHT, buff=0) for rect in [rect_3, rect_4, rect_5]]
        rect_3_copy, rect_4_copy, rect_5_copy = [rect.copy() for rect in [rect_3, rect_4, rect_5]]

        a, b, c, d, e, f = [get_tex(char).scale(0.6).set_opacity(1) for char in 'abcdef']
        a_copy1, a_copy2, a_copy3, a_copy_4, b_copy, c_copy, d_copy, e_copy, f_copy = [
            el.copy() for el in [a, a, a, a, b, c, d, e, f]
        ]

        a.move_to(rect_1.get_edge_center(LEFT) + RIGHT * 0.2)
        b.move_to(rect_1.get_edge_center(DOWN) + UP * 0.2)
        c.move_to(rect_2.get_edge_center(DOWN)).align_to(b, DOWN)
        a_copy1.move_to(rect_2.get_edge_center(LEFT) + RIGHT * 0.2)

        rect = Rectangle(Color(WHITE), 5 * SCALE, 8 * SCALE, fill_opacity=opc)

        rect.set_fill(color=[BLUE, RED], opacity=1),
        rect_abc = VGroup(
            rect,
            a.copy().move_to(rect.get_edge_center(LEFT) + RIGHT * 0.2),
            get_tex('b+c        ').set_opacity(1).scale(0.6).move_to(rect.get_edge_center(DOWN)).align_to(b, DOWN)
        ).copy()

        rect_abc_copy = VGroup(rect_1, rect_2, a, b, c, a_copy1).copy()

        # INTRO
        self.play(AnimationGroup(*[Write(l) for l in abc], lag_ratio=0.2))
        self.wait()
        self.play(ReplacementTransform(abc, form_1), Write(srr_rect1))
        self.wait()
        self.play(VGroup(form_1, srr_rect1).animate.to_edge(UP, buff=1))
        self.wait()
        self.play(Write(self.ex_1, run_time=2))
        self.wait()
        self.play(Circumscribe(self.ex_1[4:-1], fade_out=True, run_time=1.5))
        ex_1_anim = [Indicate(self.ex_1[start:end]) for start, end in zip([4, 6, 9], [5, 8, 10])]
        self.play(AnimationGroup(*ex_1_anim, lag_ratio=0.5))
        self.wait()
        self.play(self.ex_1.animate.to_edge(DR))
        self.wait()

        self.play(VGroup(form_1, srr_rect1).animate)
        self.play(Write(rect_abc.next_to(form_1, DOWN, buff=0.5).shift(LEFT * 0.35)))
        self.add(rect_abc[1:])
        self.wait()

        self.play(rect_abc.animate.shift(LEFT * 3))
        rect_abc_copy.align_to(rect_abc, UL)
        shift_scale = 0.5
        rect_abc_copy[2:].set_opacity(0)
        self.play(Write(rect_abc_copy[:2]))
        self.play(rect_abc_copy.animate.next_to(rect_abc, RIGHT * 8).align_to(rect_abc, DOWN))
        self.play(Write(rect_abc_copy[2:].set_opacity(1)))

        rect_abc_anim = [
            rect_abc_copy[0].animate.shift(LEFT * shift_scale),
            rect_abc_copy[1].animate.shift(RIGHT * shift_scale),
            rect_abc_copy[2].animate.shift(LEFT * shift_scale),
            rect_abc_copy[3].animate.shift(LEFT * shift_scale),
            rect_abc_copy[4].animate.shift(RIGHT * shift_scale),
            rect_abc_copy[5].animate.shift(RIGHT * shift_scale),
        ]

        self.play(AnimationGroup(*rect_abc_anim))

        eq_sign_pos = np.average([rect_abc.get_edge_center(RIGHT), rect_abc_copy.get_edge_center(LEFT)], 0)
        pl_sign_loc = np.average([rect_abc_copy[0].get_edge_center(RIGHT), rect_abc_copy[1].get_edge_center(LEFT)], 0)
        self.play(AnimationGroup(*[Write(equal_sign_1.move_to(eq_sign_pos)), Write(plus_sign_1.move_to(pl_sign_loc))]))

        self.play(Unwrite(srr_rect1))

        form_1_anim = [
            FadeOut(srr_rect1),
            form_1[:9 + 4].animate.move_to(rect_abc.get_edge_center(UP)).align_to(form_1, DOWN),
            form_1[9 + 4].animate.move_to(eq_sign_pos).align_to(form_1[9 + 4], DOWN),
            form_1[10 + 4:13 + 4].animate.move_to(rect_abc_copy[0].get_edge_center(UP)).align_to(
                form_1[0], DOWN),
            form_1[13 + 4].animate.move_to(pl_sign_loc).align_to(form_1[13 + 4], DOWN),
            form_1[14 + 4:].animate.move_to(rect_abc_copy[1].get_edge_center(UP)).align_to(form_1[0], DOWN),
        ]

        self.play(AnimationGroup(*form_1_anim))

        #######################################################################################
        # ATTACHING A NEW rectangle with sides a and d
        self.play(rect_abc.animate.shift(LEFT * 1))

        rect_3.next_to(rect_abc, RIGHT, buff=0).align_to(rect_abc, DOWN)
        rect_3_copy.next_to(rect_abc_copy[1], RIGHT * 4).align_to(rect_abc_copy[1], DOWN)
        d.move_to(rect_3.get_edge_center(DOWN) + UP).align_to(rect_abc[-1], DOWN)
        d_copy.move_to(rect_3_copy.get_edge_center(DOWN) + UP * 0.2).align_to(rect_abc[-1], DOWN)
        a_copy2.move_to(rect_3_copy.get_edge_center(LEFT) + RIGHT * 0.2)
        pl2_sign_loc = np.average([rect_abc_copy[1].get_edge_center(RIGHT), rect_3_copy.get_edge_center(LEFT)], 0)

        form_2.align_to(form_1, DOWN)
        form_2[:9 + 4].move_to(VGroup(rect_abc, rect_3).get_edge_center(UP)).align_to(form_1, DOWN)
        form_2[9 + 4].move_to(eq_sign_pos).align_to(form_1[9 + 4], DOWN)
        form_2[10 + 4:13 + 4].move_to(rect_abc_copy[0].get_edge_center(UP)).align_to(form_1[0], DOWN)
        form_2[13 + 4].move_to(pl_sign_loc).align_to(form_1[13 + 4], DOWN)
        form_2[14 + 4:17 + 4].move_to(rect_abc_copy[1].get_edge_center(UP)).align_to(form_1[0], DOWN)
        form_2[17 + 4].move_to(pl2_sign_loc).align_to(form_1[13 + 4], DOWN)
        form_2[18 + 4:].move_to(rect_3_copy.get_edge_center(UP)).align_to(form_1[0], DOWN)

        self.play(
            ReplacementTransform(form_1, form_2),
            Write(VGroup(rect_3_copy, a_copy2, d_copy)),
            Write(VGroup(rect_3, d)),
            Write(plus_sign_2.move_to(pl2_sign_loc))
        )
        self.wait(0.5)

        rect_new = Rectangle(Color(WHITE), 5 * SCALE, 10 * SCALE, fill_opacity=opc)
        rect_new.set_fill(color=[ORANGE, BLUE, RED], opacity=1)
        rect_abcd = VGroup(
            rect_new,
            a.copy().move_to(rect_new.get_edge_center(LEFT) + RIGHT * 0.2),
            get_tex('b+c+d    ').scale(0.6).set_opacity(opc).move_to(rect_new.get_edge_center(DOWN)).align_to(b, DOWN)
        ).copy().align_to(rect_abc, UL)

        self.play(
            AnimationGroup(
                FadeIn(rect_abcd, run_time=1.5),
                FadeOut(VGroup(rect_abc, rect_3, d), run_time=1),
                lag_ratio=0.25
            )
        )
        self.wait()

        self.play(Circumscribe(form_2[0:1], fade_out=True))
        self.wait(0.25)
        self.play(Circumscribe(form_2[2:11], fade_out=True))
        self.wait()
        self.play(
            Wiggle(rect_abc_copy[0]),
            Wiggle(rect_abc_copy[1]),
            Wiggle(rect_3_copy)
        )
        self.wait()
        self.play(
            Circumscribe(form_2[14:17], fade_out=True),
            Indicate(VGroup(rect_abc_copy[0], rect_abc_copy[2], rect_abc_copy[3]), color=None)
        )
        self.wait(0.25)
        self.play(
            Circumscribe(form_2[18:21], fade_out=True),
            Indicate(VGroup(rect_abc_copy[1], rect_abc_copy[4], rect_abc_copy[5]), color=None)
        )
        self.wait(0.25)
        self.play(
            Circumscribe(form_2[22:-1], fade_out=True),
            Indicate(VGroup(rect_3_copy, d_copy, a_copy2), color=None)
        )
        self.wait()

        self.play(Circumscribe(form_2[10 + 4:]))
        self.wait()

        self.play(Circumscribe(form_2[:9 + 4]))
        self.wait()
        self.play(Circumscribe(form_2[10 + 4:]))
        self.wait()
        self.play(Wiggle(form_2[9 + 4], scale_value=1.8))
        self.wait()

        shapes = VGroup(
            rect_abcd, rect_abc_copy,
            VGroup(rect_3_copy, a_copy2, d_copy), d_copy,
            equal_sign_1, plus_sign_1, plus_sign_2
        )

        shapes.save_state()
        form_2.save_state()

        #######################################################################################
        # SOLVING THE EXAMPLE PROBLEM

        self.form_2_copy.scale(BIG_SCALE).to_edge(UL)
        self.srr_rect2 = SurroundingRectangle(self.form_2_copy, BLUE, buff=.2, corner_radius=.3)
        self.play(
            AnimationGroup(
                FadeOut(shapes, run_time=1),
                TransformMatchingTex(form_2, self.form_2_copy),
                Write(self.srr_rect2),
                self.ex_1.animate.next_to(self.srr_rect2, DOWN).align_to(self.form_2_copy, LEFT),
                lag_ratio=opc
            )
        )
        self.wait()

        self.solve_ex1()

        #######################################################################################
        # adding 2 new rectangles with sides a•e and a•f

        new_scale = 0.7
        shapes.restore()
        form_2.restore()
        VGroup(shapes, form_2).scale(new_scale).move_to(ORIGIN)

        self.play(
            ReplacementTransform(self.form_2_copy, form_2),
            FadeIn(shapes)
        )
        self.wait()
        self.play(rect_abcd.animate.shift(LEFT * 2).align_to(rect_abcd, DOWN))
        self.wait()

        rescale_obj = [
            e, e_copy, a_copy3,  rect_4, rect_4_copy, f, f_copy, a_copy_4,
            rect_5, rect_5_copy, form_3, plus_sign_3, plus_sign_4
        ]
        [el.scale(new_scale) for el in rescale_obj]

        rect_4.next_to(rect_abcd, RIGHT, buff=0).align_to(rect_abcd, DOWN)
        rect_4_copy.next_to(rect_3_copy, RIGHT * 4).align_to(rect_abc_copy[1], DOWN)
        e.move_to(rect_4.get_edge_center(DOWN) + UP).align_to(rect_abcd[-1], DOWN)
        e_copy.move_to(rect_4_copy.get_edge_center(DOWN) + UP * 0.2).align_to(rect_abcd[-1], DOWN)
        a_copy3.move_to(rect_4_copy.get_edge_center(LEFT) + RIGHT * 0.2)

        rect_5.next_to(rect_4, RIGHT, buff=0).align_to(rect_abcd, DOWN)
        rect_5_copy.next_to(rect_4_copy, RIGHT * 4).align_to(rect_abc_copy[1], DOWN)
        f.move_to(rect_5.get_edge_center(DOWN) + UP).align_to(rect_abcd[-1], DOWN)
        f_copy.move_to(rect_5_copy.get_edge_center(DOWN) + UP * 0.2).align_to(rect_abcd[-1], DOWN)
        a_copy_4.move_to(rect_5_copy.get_edge_center(LEFT) + RIGHT * 0.2)

        pl_1_sign_loc = np.average([rect_abc_copy[0].get_edge_center(RIGHT), rect_abc_copy[1].get_edge_center(LEFT)], 0)
        pl_2_sign_loc = np.average([rect_abc_copy[1].get_edge_center(RIGHT), rect_3_copy.get_edge_center(LEFT)], 0)

        form_3.align_to(form_2, DOWN)

        form_3[:9 + 4].move_to(VGroup(rect_abcd, rect_3).get_edge_center(UP)).align_to(form_2, DOWN)
        form_3[9 + 4].move_to(eq_sign_pos).align_to(form_2[9 + 4], DOWN)
        form_3[10 + 4:13 + 4].move_to(rect_abc_copy[0].get_edge_center(UP)).align_to(form_2[0], DOWN)
        form_3[13 + 4].move_to(pl_1_sign_loc).align_to(form_2[13 + 4], DOWN)
        form_3[14 + 4:17 + 4].move_to(rect_abc_copy[1].get_edge_center(UP)).align_to(form_2[0], DOWN)
        form_3[17 + 4].move_to(pl_2_sign_loc).align_to(form_2[13 + 4], DOWN)
        form_3[18 + 4:21 + 4].move_to(rect_3_copy.get_edge_center(UP)).align_to(form_2[0], DOWN)

        form_3[21 + 4:].set_opacity(0)

        self.play(
            ReplacementTransform(form_2, form_3),
            Write(rect_4),
            Write(e),
            Write(rect_5),
            Write(f),
            FadeOut(shapes[4])
        )
        self.play(FadeOut(form_3[13], run_time=0.5))
        self.wait(0.1)

        rect_new = Rectangle(Color(WHITE), 5 * SCALE, 16 * SCALE, fill_opacity=opc)
        rect_new.set_fill(color=[GOLD_A, MAROON, ORANGE, BLUE, RED], opacity=1)
        bcdef = get_tex('b+c+d+e+f').scale(0.6).set_opacity(opc).move_to(rect_new.get_edge_center(DOWN)).align_to(b,
                                                                                                                  DOWN)
        rect_abcdef = VGroup(
            rect_new,
            a.copy().move_to(rect_new.get_edge_center(LEFT) + RIGHT * 0.2),
            bcdef
        ).copy().scale(new_scale).align_to(rect_abcd, UL)

        self.play(FadeOut(VGroup(rect_abcd, rect_4, rect_5, e, f), run_time=2), FadeIn(rect_abcdef, run_time=2))
        self.wait(0.1)

        v_group = VGroup(
            rect_abcdef, equal_sign_1, VGroup(rect_abc_copy[0], rect_abc_copy[2:4]), plus_sign_1,
            VGroup(rect_abc_copy[1], rect_abc_copy[4:]), plus_sign_2, VGroup(rect_3_copy, a_copy2, d_copy),
            plus_sign_3.set_opacity(0), VGroup(rect_4_copy, a_copy3, e_copy), plus_sign_4.set_opacity(0),
            VGroup(rect_5_copy, a_copy_4, f_copy)
        )
        self.play(
            v_group.animate.arrange(RIGHT, buff=0.15).align_to(rect_abcdef, UL).shift(LEFT * 0.3),
        )

        form_3_tmp = form_3.copy()

        form_3_tmp.set_opacity(1)
        eq_sign_pos = np.average([rect_abcdef.get_edge_center(RIGHT), rect_abc_copy.get_edge_center(LEFT)], 0)
        pl_1_sign_loc = np.average([rect_abc_copy[0].get_edge_center(RIGHT), rect_abc_copy[1].get_edge_center(LEFT)], 0)
        pl_2_sign_loc = np.average([rect_abc_copy[1].get_edge_center(RIGHT), rect_3_copy.get_edge_center(LEFT)], 0)
        pl_3_sign_loc = np.average([rect_3_copy.get_edge_center(RIGHT), rect_4_copy.get_edge_center(LEFT)], 0)
        pl_4_sign_loc = np.average([rect_4_copy.get_edge_center(RIGHT), rect_5_copy.get_edge_center(LEFT)], 0)

        form_3_tmp[:9 + 4].move_to(VGroup(rect_abcd, rect_3).get_edge_center(UP)).align_to(form_2, DOWN)
        form_3_tmp[9 + 4].move_to(eq_sign_pos).align_to(form_2[9 + 4], DOWN)
        form_3_tmp[10 + 4:13 + 4].move_to(rect_abc_copy[0].get_edge_center(UP)).align_to(form_2[0], DOWN)
        form_3_tmp[13 + 4].move_to(pl_1_sign_loc).align_to(form_2[13 + 4], DOWN)
        form_3_tmp[14 + 4:17 + 4].move_to(rect_abc_copy[1].get_edge_center(UP)).align_to(form_2[0], DOWN)
        form_3_tmp[17 + 4].move_to(pl_2_sign_loc).align_to(form_2[13 + 4], DOWN)
        form_3_tmp[18 + 4:21 + 4].move_to(rect_3_copy.get_edge_center(UP)).align_to(form_2[0], DOWN)
        form_3_tmp[21 + 4].move_to(pl_3_sign_loc).align_to(form_2[13 + 4], DOWN)
        form_3_tmp[22 + 4:25 + 4].move_to(rect_4_copy.get_edge_center(UP)).align_to(form_2[0], DOWN)
        form_3_tmp[25 + 4].move_to(pl_4_sign_loc).align_to(form_2[13 + 4], DOWN)
        form_3_tmp[26 + 4:].move_to(rect_5_copy.get_edge_center(UP)).align_to(form_2[0], DOWN).shift(DOWN * 0.1)

        self.form_3_copy.align_to(form_3, DOWN).scale(new_scale)
        self.play(ReplacementTransform(form_3[:21 + 4], form_3_tmp[:21 + 4]))
        self.wait(0.1)
        self.play(Write(form_3_tmp[21 + 4:]), Write(plus_sign_3.set_opacity(1)), Write(plus_sign_4.set_opacity(1)))
        self.wait(0.1)

        self.play(ReplacementTransform(form_3_tmp, self.form_3_copy.shift(UP * 0.5).set_color(WHITE)))
        self.wait(0.1)

        ################################################################################################################

        circle_a = circle(self.form_3_copy[0], color=TEAL)

        left_side_idx = np.arange(3, 12, 2)
        right_side_idx = np.arange(14, 32, 4)
        right_buff = 3
        colors = [RED, BLUE, ORANGE, MAROON, GOLD_A]
        circle_b, circle_c, circle_d, circle_e, circle_f = [
            circle(self.form_3_copy[i], color=c)
            for i, c in zip(left_side_idx, colors)
        ]

        circle_ab, circle_ac, circle_ad, circle_ae, circle_af = [
            circle(self.form_3_copy[i:i + right_buff], color=c) for i, c in zip(right_side_idx, colors)
        ]

        circles_left = [circle_b, circle_c, circle_d, circle_e, circle_f]
        circles_right = [circle_ab, circle_ac, circle_ad, circle_ae, circle_af]

        self.play(Write(circle_a))
        self.wait(0.1)
        self.play(Write(circle_b), Write(circle_ab))
        self.wait(0.1)
        for i, j in zip(range(0, 4), range(1, 5)):
            self.play(
                ReplacementTransform(circles_left[i], circles_left[j]),
                ReplacementTransform(circles_right[i], circles_right[j])
            )
            self.wait(0.1)

        self.play(Unwrite(circle_a), Unwrite(circles_left[-1]), Unwrite(circles_right[-1]))
        self.wait(0.1)

        self.play(FadeOut(v_group))
        self.wait(0.1)
        self.play(self.form_3_copy.animate.move_to(ORIGIN))
        self.wait(0.1)

        ################################################################################################################

        form_3_str = 'a*(b+c+d+e+f)                    '
        form_4_str = 'a*(b+c+d    )                    '
        form_5_str_0 = 'a*(b+c+d+e  )                    '
        form_5_str_1 = 'a*(b+c+d+e  )=a*b                '
        form_5_str_2 = 'a*(b+c+d+e  )=a*b+a*c            '
        form_5_str_3 = 'a*(b+c+d+e  )=a*b+a*c+a*d        '
        form_5_str_4 = 'a*(b+c+d+e  )=a*b+a*c+a*d+a*e    '
        form_3 = get_tex(form_3_str).move_to(self.form_3_copy)
        form_4 = get_tex(form_4_str).move_to(self.form_3_copy)
        form_5s = [
            get_tex(x).move_to(form_4) for x in [form_5_str_0, form_5_str_1, form_5_str_2, form_5_str_3, form_5_str_4]]

        a_idx, b_idx, c_idx, d_idx, e_idx, f_idx = [find_index(form_3_str, char) for char in 'abcdef']
        a_copy3, b_4, c_4, d_4 = [find_index(form_4_str, char) for char in 'abcd']
        a_copy_4, b_5, c_5, d_5, e_5 = [find_index(form_5_str_4, char) for char in 'abcde']

        [form_3[i].set_color(ORANGE) for i in a_idx]
        [form_3[i].set_color(BLUE) for i in b_idx + c_idx + d_idx + e_idx + f_idx]
        [form_4[i].set_color(ORANGE) for i in a_copy3]
        [form_4[i].set_color(BLUE) for i in b_4 + c_5 + d_5]
        [form_4[i].set_color(ORANGE) for i in a_copy3]
        [form_4[i].set_color(BLUE) for i in b_4 + c_5 + d_5]

        for form_5 in form_5s:
            [form_5[i].set_color(ORANGE) for i in a_copy_4]
            [form_5[i].set_color(BLUE) for i in b_5 + c_5 + d_5 + e_5]

        self.play(ReplacementTransform(self.form_3_copy, form_3.scale(1.25)))
        self.wait()
        self.play(ReplacementTransform(form_3, form_4.scale(1.25)))
        self.wait()
        self.play(ReplacementTransform(form_4, form_5s[0].scale(1.25)))
        self.wait()

        self.play(form_5s[0].animate.to_edge(LEFT, buff=0.75))

        self.wait()

        lines = [ConectionLine(form_5s[0][0], form_5s[0][i], alpha=1 / 5, color='#628E90') for i in [3, 5, 7, 9]]

        add_items = [' = a\cdot b', ' + a\cdot c', ' + a\cdot d', ' + a\cdot e']
        self.fix_formula(form_5s[0])
        self.play(Create(lines[0]))
        for i in range(4):
            if i != 0:
                self.play(ReplacementTransform(lines[i-1], lines[i]))
            self.play(
                ModifyFormula(
                    form_5s[0],
                    add_after_items=[len(form_5s[0]) - 1], add_items_strs=[[add_items[i]]], add_items_animation_style=Write
                )
            )
            self.wait(0.25)

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)

        last_exercise = get_tex('m(x+y^2+3+2z)').scale(BIG_SCALE)
        self.play(Write(last_exercise))
        self.wait(3)

    def solve_ex1(self):

        a_idx, b_idx, c_idx, d_idx = [find_index(self.form_2_str, char) for char in 'abcd']

        solution = self.form_2_copy.copy()\
            .scale(1 / BIG_SCALE)\
            .next_to(self.ex_1, DOWN)\
            .align_to(self.ex_1, LEFT)\
            .set_color(WHITE)
        solution_copy = self.form_2_copy.copy()

        self.play(ClockwiseTransform(solution_copy, solution))
        self.add(solution).remove(solution_copy)

        colors = [RED, GREEN, BLUE, ORANGE]
        start = [0, 4, 6, -2]
        end = [2, 5, 8, -1]
        lt_idx = [a_idx, b_idx, c_idx, d_idx]
        replace_items_strs = [r'x^2', 'n', 'yz', '6']
        remove_items = [[], [], [], [8, 9, 10, 11, 25, 26, 27, 28, 29, 30, 31, 32]]

        for c, st, en, idx, r, rm in zip(colors, start, end, lt_idx, replace_items_strs, remove_items):
            replace_items = [[x] for x in idx]
            self.play(Indicate(self.ex_1[st:en].set_color(color=c), color=c))
            self.play(*[Indicate(solution[i].set_color(color=c), color=c) for i in idx])
            self.fix_formula(solution)
            self.play(
                ModifyFormula(
                    solution,
                    replace_items=replace_items,
                    replace_items_strs=[[r]] * len(replace_items),
                    remove_items=rm
                )
            )

        # finish exercise
        self.fix_formula(solution)

        self.play(Wiggle(solution[10:13], scale_value=1.4))
        self.wait(0.5)

        rearrange_list = []
        for i in range(len(solution)):
            if i == 10:
                rearrange_list.append(12)
            elif i == 12:
                rearrange_list.append(10)
            else:
                rearrange_list.append(i)

        self.rearrange_formula(
            solution, rearrange_list,
            [12], [], [11], []
        )
        self.wait(0.25)

        self.play(ModifyFormula(solution, remove_items=[11]))
        self.fix_formula(solution)
        self.wait()

        self.play(Wiggle(solution[13:16], scale_value=1.4))
        self.wait(0.25)

        self.play(ModifyFormula(solution, remove_items=[14]))
        self.fix_formula(solution)
        self.wait()

        self.play(Wiggle(solution[16:19], scale_value=1.4))
        self.fix_formula(solution)
        self.wait(0.25)

        rearrange_list = []
        for i in range(len(solution)):
            if i == 16:
                rearrange_list.append(18)
            elif i == 18:
                rearrange_list.append(16)
            else:
                rearrange_list.append(i)

        self.rearrange_formula(solution, rearrange_list, [18], [], [17], [])
        self.wait(0.25)

        self.play(ModifyFormula(solution, remove_items=[17]))
        self.wait()

        self.play(
            Unwrite(self.ex_1),
            solution.animate.move_to(ORIGIN).set_color(WHITE)
        )
        self.wait(0.25)

        self.play(Unwrite(VGroup(self.srr_rect2, self.ex_1, solution), run_time=2))
        self.wait()
