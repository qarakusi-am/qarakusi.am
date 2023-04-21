from manim import LEFT, RIGHT, ORIGIN, UL, UP, UR, DR, DOWN, DL
from manim import FadeOut, Write, FadeIn
from manim import Group, VGroup, ReplacementTransform, ImageMobject, AnimationGroup
from manim import Line, Rectangle, Arrow, MathTex, Dot, BraceText, Tex, Brace
from manim import RED, ORANGE, YELLOW, WHITE, PURE_GREEN

from movement_problems import Coordinate
from qarakusiscene import QarakusiScene
from objects import SimpleSVGMobject
from segment import Segment
from . import text


class Problem12781(QarakusiScene):
    """Նարեկը վիդեոներ է մոնտաժում"""
    def construct(self):
        screen_center = [0, 0, 0]
        condition_point = [-4.5, 3.15, 0]

        coord_y = -2.6
        start_point = [-6.5, coord_y, 0]
        end_point = [6.5, coord_y, 0]

        coordinate = Coordinate(start_point, end_point)
        segment_coord = coordinate.divide_segment_into_equal_parts(7)
        segment_coord.insert(0, start_point)


        self.add_task_number(text=text.TASK_NUMBER_STR)
        MathTex.set_default(font_size=text.default_font_size)
        self.add_plane()

        # -------------------------- Point 1 ------------------------------- #
        boy = SimpleSVGMobject('boy_2', color=WHITE).move_to(screen_center).scale(1.3)
        computer = SimpleSVGMobject('computer').next_to(boy).scale(0.7)
        self.play(FadeIn(boy), FadeIn(computer))
        self.wait()

        # -------------------------- Point 2 ------------------------------- #
        screenshots = Group(*[ImageMobject(f'objects/PNG_files/qarakusi_video_screenshots/{i}'
            ).next_to(boy, p, buff=0.6) for i, p in enumerate(
            (UL + LEFT, UP + DOWN * 0.6, UR + RIGHT, LEFT, DL + LEFT, DOWN + DOWN), start=1)])

        self.play(AnimationGroup(*[FadeIn(item) for item in screenshots], lag_ratio=0.8))
        self.wait()

        # -------------------------- Point 3 ------------------------------- #
        main_segment = Segment(start_point, end_point)
        self.play(FadeOut(screenshots), ReplacementTransform(Group(boy, computer), main_segment))
        self.wait()

        # -------------------------- Point 4 ------------------------------- #
        condition_1 = MathTex(*text.CONDITION_1).next_to(condition_point)
        self.play(Write(condition_1))
        self.wait()

        # -------------------------- Point 5 ------------------------------- #
        dot_1 = VGroup(*[Dot() for _ in range(7)]).move_to(condition_1[1][-1]).set_opacity(0)
        segments_pattern = VGroup(*[Segment(segment_coord[0], segment_coord[1]
                                      ).next_to(p, buff=0) for p in segment_coord]).set_color(YELLOW)

        dot_2 = VGroup(dot_1[0].copy().move_to(condition_1[1][0]), dot_1[0].copy().move_to(condition_1[1][0]))

        segments_2 = VGroup(segments_pattern[0].copy().set_color(RED), segments_pattern[1].copy().set_color(RED))
        segments_3 = VGroup(segments_pattern[2].copy().set_color(RED), segments_pattern[3].copy().set_color(RED))

        coordinate_1 = Coordinate(segment_coord[4], segment_coord[5])

        segments_4_second_p = coordinate_1.get_point_by_percent_on_segment(63)
        segments_4 = Segment(segment_coord[4],
                             segments_4_second_p).next_to(segment_coord[4], buff=0).set_color(PURE_GREEN)

        self.play(AnimationGroup(*[ReplacementTransform(dot_1[i], segments_pattern[i]) for i in range(7)],
                                 lag_ratio=0.5,
                                 run_time=6))
        self.wait()

        # -------------------------- Point 6 ------------------------------- #
        self.play(AnimationGroup(ReplacementTransform(dot_2[0], segments_2[0]),
                                 ReplacementTransform(dot_2[1], segments_2[1]),
                                 lag_ratio=0.5,
                                 run_time=3))
        self.wait()

        # -------------------------- Point 7 ------------------------------- #
        brace_text_1 = BraceText(segments_2, text.SEGMENT_TEXT_1, label_constructor=MathTex, buff=0, font_size=65)
        self.play(FadeIn(brace_text_1))
        self.wait()

        # -------------------------- Point 8 ------------------------------- #
        condition_2 = MathTex(*text.CONDITION_2).next_to(condition_1, DOWN, aligned_edge=LEFT)
        self.play(Write(condition_2))
        self.wait()

        # -------------------------- Point 9 ------------------------------- #
        dot_3 = VGroup(*[Dot() for _ in range(2)]).move_to(condition_2[0]).set_opacity(0)
        self.play(AnimationGroup(ReplacementTransform(dot_3[0], segments_3[0]),
                                 ReplacementTransform(dot_3[1], segments_3[1]),
                                 lag_ratio=0.5,
                                 run_time=3))
        self.wait()

        # -------------------------- Point 10 ------------------------------- #
        dot_4 = Dot().move_to(condition_2[1]).set_opacity(0)
        self.play(ReplacementTransform(dot_4, segments_4), run_time=1.5)
        self.wait()

        # -------------------------- Point 11 ------------------------------- #
        brace_text_2 = BraceText(segments_3, text.SEGMENT_TEXT_1, label_constructor=MathTex, buff=0, font_size=65)
        brace_text_3 = BraceText(segments_4, "5", label_constructor=MathTex, buff=0, font_size=65)
        self.play(FadeIn(brace_text_2))
        self.play(FadeIn(brace_text_3))
        self.wait()

        # -------------------------- Point 12 ------------------------------- #
        invisible_line = Segment(segments_4_second_p, end_point).set_opacity(0)
        brace_text_4 = BraceText(invisible_line,
                                 "19", label_constructor=MathTex, buff=0, font_size=65)
        self.play(FadeIn(brace_text_4))
        self.play(FadeOut(Group(condition_1, condition_2)))
        self.wait()

        # -------------------------- Point 13 ------------------------------- #
        condition_3 = MathTex(*text.CONDITION_3).next_to(condition_point).shift(RIGHT)
        self.play(Write(condition_3[0]))
        self.wait()
        self.play(Write(condition_3[1:]))
        self.wait()

        # -------------------------- Point 14 ------------------------------- #
        condition_3_2_copy = condition_3[2].copy()
        brace_1 = Brace(segments_pattern[:4] ,direction=UP, buff=0)
        self.play(FadeIn(brace_1), condition_3_2_copy.animate.next_to(brace_1, UP, buff=0.05))
        self.wait()

        # -------------------------- Point 15 ------------------------------- #
        condition_4 = MathTex(*text.CONDITION_4).next_to(condition_3, DOWN, buff=0.15)
        self.play(Write(condition_4[0]))
        self.wait()
        self.play(Write(condition_4[1]))
        self.wait()
        self.play(Write(condition_4[2]))
        self.wait()
        self.play(Write(condition_4[3]))
        self.wait()


        # -------------------------- Point 16 ------------------------------- #
        condition_4_3_copy = condition_4[3].copy()
        brace_2 = Brace(segments_pattern[4:], direction=UP, buff=0)
        self.play(FadeIn(brace_2), condition_4_3_copy.animate.next_to(brace_2, UP, buff=0.05))
        self.wait()
        brace_text_5 = BraceText(segments_pattern[4:], "24", label_constructor=MathTex, buff=0, font_size=65)
        self.play(ReplacementTransform(Group(brace_text_3, brace_text_4), brace_text_5), FadeOut(segments_4))
        self.wait()

        # -------------------------- Point 17 ------------------------------- #
        condition_5 = MathTex(*text.CONDITION_5).next_to(condition_4, DOWN, buff=0.15)
        self.play(Write(condition_5))
        self.wait()

        # -------------------------- Point 18 ------------------------------- #
        brace_3 = Brace(segments_pattern, direction=UP, buff=0)
        self.play(FadeOut(Group(condition_4_3_copy, condition_3_2_copy)),
                  ReplacementTransform(Group(brace_1, brace_2), brace_3),
                  condition_5[1].copy().animate.next_to(brace_3, UP, buff=0.15))
        self.wait(3)
