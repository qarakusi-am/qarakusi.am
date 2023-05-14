from manim import Scene, FadeIn, Create, Circle, VGroup, MathTex, Write, Intersection, Transform, TransformFromCopy, AnimationGroup, FadeOut, ReplacementTransform, Difference, Group, Tex, Circumscribe
from manim import YELLOW, GREEN, RED, BLUE_B, BLUE
from manim import LEFT, UP, RIGHT, DOWN, ORIGIN
from manim import PI
from manim import rate_functions
from numpy import array
from qarakusiscene import TaskNumberBox
from objects import SimpleSVGMobject, Checkmark
from math import sqrt
from .text import *

SCALE = .5
CIRCLE_FONT_SIZE = 120 * SCALE

class Problem12794(Scene):
    def construct(self):
        self.wait()

        Tex.set_default(font_size=60)

        # task number
        task_number = TaskNumberBox(task_number_str)
        self.play(FadeIn(task_number))
        self.wait()

        # questions
        bicycle_svg = SimpleSVGMobject("bicycle")
        scooter_svg = SimpleSVGMobject("scooter")
        ball_svg = SimpleSVGMobject("football_1")

        question1 = Tex(question1_str)
        question2 = VGroup(
            Tex(question2_str[0]),
            Tex(question2_str[1])
        ).arrange(DOWN, aligned_edge=LEFT)
        question3 = VGroup(
            Tex(question3_str)
        )
        question4 = VGroup(
            Tex(question4_str)
        )
        question5 = VGroup(
            Tex(question5_str)
        )

        questions = VGroup(
            question1,
            question2,
            question3,
            question4,
            question5
        ).arrange(DOWN, aligned_edge=LEFT).scale(1.3)
        question1.shift(UP*2)

        questions.shift(RIGHT*self.camera.frame_width)

        # create 3 circles
        bicycle_circle = Circle(sqrt(25)*SCALE, color=YELLOW).set_fill(YELLOW, .5)
        scooter_circle = Circle(sqrt(17)*SCALE, color=GREEN).set_fill(GREEN, .5)
        ball_circle = Circle(sqrt(13)*SCALE, color=RED).set_fill(RED, .5)

        ball_circle.next_to(bicycle_circle, buff=0).shift(LEFT*ball_circle.radius*.95).rotate(PI/5, about_point=bicycle_circle.get_center())
        scooter_circle.next_to(ball_circle, buff=0).shift(LEFT*scooter_circle.radius*.6).rotate(-PI/14, about_point=ball_circle.get_center())

        VGroup(bicycle_circle, scooter_circle, ball_circle).move_to(ORIGIN).to_edge(DOWN)

        # 3 svgs
        bicycle_svg.scale(.5).move_to(bicycle_circle, aligned_edge=DOWN).shift(UP*bicycle_circle.radius*.2).set_z_index(bicycle_circle.z_index+1)
        scooter_svg.scale(.5).move_to(scooter_circle, aligned_edge=DOWN).shift(UP*ball_circle.radius*.2).set_z_index(scooter_circle.z_index+1)
        ball_svg.scale(.5).move_to(ball_circle, aligned_edge=UP).shift(DOWN*ball_circle.radius*.2).set_z_index(ball_circle.z_index+1)

        self.play(FadeIn(bicycle_svg, scooter_svg, ball_svg))
        self.wait()

        # there aren't children who have bicycle and scooter
        condition1 = Tex(condition1_str)
        condition1.to_edge(UP)
        self.play(Write(condition1))
        self.wait()

        self.play(
            Create(bicycle_circle),
            Create(scooter_circle)
        )
        self.wait()

        checkmark = Checkmark().scale(.35)
        checkmark1 = checkmark.copy()
        checkmark1.next_to(condition1)
        self.play(Write(checkmark1))
        self.wait()
        self.play(FadeOut(condition1, checkmark1))
        self.wait()

        # bicycle and ball
        condition2 = Tex(condition2_str)
        condition2.to_edge(UP)
        self.play(Write(condition2))
        self.wait()

        bicycle_and_ball = Intersection(bicycle_circle, ball_circle)
        bicycle_and_ball_svgs = VGroup(
            bicycle_svg.copy(),
            ball_svg.copy()
        ).arrange().scale(.5)
        bicycle_and_ball_count = MathTex("7", font_size=CIRCLE_FONT_SIZE)
        bicycle_and_ball_count.next_to(bicycle_and_ball_svgs, UP)
        VGroup(bicycle_and_ball_count, bicycle_and_ball_svgs).move_to(bicycle_and_ball)

        self.play(Create(ball_circle))
        self.wait()
        self.play(Create(bicycle_and_ball))
        self.play(
            AnimationGroup(
                AnimationGroup(
                    TransformFromCopy(bicycle_svg, bicycle_and_ball_svgs[0]),
                    TransformFromCopy(ball_svg, bicycle_and_ball_svgs[1])
                ),
                Write(bicycle_and_ball_count),
                lag_ratio=.5
            )
        )
        self.wait()

        checkmark2 = checkmark.copy()
        checkmark2.next_to(condition2)
        self.play(Write(checkmark2))
        self.wait()
        self.play(FadeOut(condition2, checkmark2))
        self.wait()

        # scooter and ball
        condition3 = Tex(condition3_str)
        condition3.to_edge(UP)
        self.play(Write(condition3))
        self.wait()

        scooter_and_ball = Intersection(scooter_circle, ball_circle)
        scooter_and_ball_svgs = VGroup(
            ball_svg.copy(),
            scooter_svg.copy()
        ).arrange().scale(.4)
        scooter_and_ball_count = MathTex("4", font_size=CIRCLE_FONT_SIZE)
        scooter_and_ball_count.next_to(scooter_and_ball_svgs, UP)
        VGroup(scooter_and_ball_count, scooter_and_ball_svgs).move_to(scooter_and_ball)

        self.wait()
        self.play(Create(scooter_and_ball))
        self.play(
            AnimationGroup(
                AnimationGroup(
                    TransformFromCopy(scooter_svg, scooter_and_ball_svgs[1]),
                    TransformFromCopy(ball_svg, scooter_and_ball_svgs[0])
                ),
                Write(scooter_and_ball_count),
                lag_ratio=.5
            )
        )
        self.wait()

        checkmark3 = checkmark.copy()
        checkmark3.next_to(condition3)
        self.play(Write(checkmark3))
        self.wait()
        self.play(FadeOut(condition3, checkmark3))
        self.wait()

        # only bicycle
        condition4 = Tex(condition4_str)
        condition4.to_edge(UP)
        self.play(Write(condition4))
        self.wait()

        temp_bicycle_circle = bicycle_circle.copy().set_z_index(2)
        bicycle_svg.set_z_index(temp_bicycle_circle.z_index+1)
        self.play(
            FadeIn(temp_bicycle_circle)
        )
        self.wait()

        bicycle_count = MathTex("25", font_size=CIRCLE_FONT_SIZE*temp_bicycle_circle.radius)
        bicycle_count.move_to(temp_bicycle_circle).shift(LEFT*.3).set_z_index(temp_bicycle_circle.z_index+1)
        self.play(Write(bicycle_count))
        self.wait()

        checkmark4 = checkmark.copy()
        checkmark4.next_to(condition4)
        self.play(Write(checkmark4))
        self.wait()
        self.play(FadeOut(condition4, checkmark4))
        self.wait()

        only_bicycle_count = MathTex("25", "-", "7", font_size=CIRCLE_FONT_SIZE*bicycle_circle.radius*.5)
        only_bicycle_count.move_to(bicycle_circle, aligned_edge=LEFT).shift(RIGHT*bicycle_circle.radius*.2)
        only_bicycle = Difference(bicycle_circle, ball_circle, color=BLUE_B, stroke_width=12)
        only_bicycle.set_z_index(temp_bicycle_circle.z_index+1)

        self.play(
            FadeOut(temp_bicycle_circle),
            Create(only_bicycle, run_time=2)
        )
        self.wait()
        self.play(
            ReplacementTransform(bicycle_count, only_bicycle_count[0]),
            Write(only_bicycle_count[1]),
            TransformFromCopy(bicycle_and_ball_count, only_bicycle_count[2])
        )
        self.wait()
        self.play(
            Transform(
                only_bicycle_count,
                MathTex("18", font_size=CIRCLE_FONT_SIZE*bicycle_circle.radius*.9).move_to(only_bicycle_count.get_center())
            )
        )
        self.play(FadeOut(only_bicycle))
        self.wait()

        # only scooter
        condition5 = Tex(condition5_str)
        condition5.to_edge(UP)
        self.play(Write(condition5))
        self.wait()

        temp_scooter_circle = scooter_circle.copy().set_z_index(2)
        scooter_svg.set_z_index(temp_scooter_circle.z_index+1)
        self.play(
            FadeIn(temp_scooter_circle)
        )
        self.wait()

        scooter_count = MathTex("13", font_size=CIRCLE_FONT_SIZE*temp_scooter_circle.radius)
        scooter_count.move_to(temp_scooter_circle).shift(RIGHT*.3).set_z_index(temp_scooter_circle.z_index+1)
        self.play(Write(scooter_count))
        self.wait()

        checkmark5 = checkmark.copy()
        checkmark5.next_to(condition5)
        self.play(Write(checkmark5))
        self.wait()
        self.play(FadeOut(condition5, checkmark5))
        self.wait()

        only_scooter_count = MathTex("13", "-", "4", font_size=CIRCLE_FONT_SIZE*scooter_circle.radius*.5)
        only_scooter_count.move_to(scooter_circle, aligned_edge=RIGHT).shift(LEFT*scooter_circle.radius*.2)
        only_scooter = Difference(scooter_circle, ball_circle, color=BLUE_B, stroke_width=12)
        only_scooter.set_z_index(temp_scooter_circle.z_index+1)

        self.play(
            FadeOut(temp_scooter_circle),
            Create(only_scooter, run_time=2)
        )
        self.wait()
        self.play(
            ReplacementTransform(scooter_count, only_scooter_count[0]),
            Write(only_scooter_count[1]),
            TransformFromCopy(scooter_and_ball_count, only_scooter_count[2])
        )
        self.wait()
        self.play(
            Transform(
                only_scooter_count,
                MathTex("9", font_size=CIRCLE_FONT_SIZE*scooter_circle.radius*.9).move_to(only_scooter_count.get_center())
            )
        )
        self.play(FadeOut(only_scooter))
        self.wait()

        # only ball
        condition6 = Tex(condition6_str)
        condition6.to_edge(UP)
        self.play(Write(condition6))
        self.wait()

        self.play(ball_svg.animate.scale(.56).shift(array([ball_circle.radius*.12, ball_circle.radius*(-.4), 0])))
        self.wait()

        temp_ball_circle = ball_circle.copy().set_z_index(2)
        ball_svg.set_z_index(temp_ball_circle.z_index+1)
        self.play(
            FadeIn(temp_ball_circle)
        )
        self.wait()

        ball_count = MathTex("17", font_size=CIRCLE_FONT_SIZE*temp_ball_circle.radius*.7)
        ball_count.move_to(temp_ball_circle, aligned_edge=UP).shift(DOWN*ball_circle.radius*.2).set_z_index(temp_ball_circle.z_index+1)
        self.play(Write(ball_count))
        self.wait()

        checkmark6 = checkmark.copy()
        checkmark6.next_to(condition6)
        self.play(Write(checkmark6))
        self.wait()
        self.play(FadeOut(condition6, checkmark6))
        self.wait()

        # only_ball_count = MathTex("17", "-", "7", "-", "4", font_size=CIRCLE_FONT_SIZE*ball_circle.radius*.35)
        # only_ball_count.move_to(ball_circle, aligned_edge=UP).shift(DOWN*ball_circle.radius*.3)
        only_ball_count = MathTex("6", font_size=CIRCLE_FONT_SIZE*ball_circle.radius*.9)
        only_ball_count.move_to(ball_circle, aligned_edge=UP).shift(DOWN*ball_circle.radius*.25)
        only_ball = Intersection(
            Difference(ball_circle, bicycle_circle),
            Difference(ball_circle, scooter_circle),
            color=BLUE_B, stroke_width=12
        )
        only_ball.set_z_index(temp_ball_circle.z_index+1)

        self.play(
            FadeOut(temp_ball_circle),
            Create(only_ball, run_time=2)
        )
        self.wait()
        # self.play(
        #     ReplacementTransform(ball_count, only_ball_count[0]),
        #     Write(only_ball_count[1]),
        #     TransformFromCopy(bicycle_and_ball_count, only_ball_count[2]),
        #     Write(only_ball_count[3]),
        #     TransformFromCopy(scooter_and_ball_count, only_ball_count[4])
        # )
        # self.wait()
        # self.play(
        #     Transform(
        #         only_ball_count,
        #         MathTex("6", font_size=CIRCLE_FONT_SIZE*ball_circle.radius*.9).move_to(only_ball_count.get_center())
        #     )
        # )
        self.play(
            ReplacementTransform(
                ball_count,
                only_ball_count
            )
        )
        self.play(FadeOut(only_ball))
        self.wait()

        # question 1
        diagram = Group(*self.mobjects)
        diagram.remove(task_number, questions)
        questions.next_to(diagram, buff=1.5)
        self.play(
            Group(diagram, questions).animate(rate_func=rate_functions.linear).scale(.68).to_edge(LEFT, buff=.25).to_edge(UP)
        )
        self.play(questions.animate(rate_func=rate_functions.linear).next_to(diagram))
        self.wait()

        self.play(Circumscribe(question1, fade_out=True))
        self.wait()
        MathTex.set_default(font_size=65)
        answer1 = MathTex("18", "+", "7", "+", "6", "+", "4", "+", "9", "=", "44")
        answer1[-1].set_color(BLUE)
        answer1.next_to(question1, DOWN, aligned_edge=LEFT)
        self.play(
            AnimationGroup(
                TransformFromCopy(only_bicycle_count, answer1[0]),
                Write(answer1[1]),
                TransformFromCopy(bicycle_and_ball_count, answer1[2]),
                Write(answer1[3]),
                TransformFromCopy(only_ball_count, answer1[4]),
                Write(answer1[5]),
                TransformFromCopy(scooter_and_ball_count, answer1[6]),
                Write(answer1[7]),
                TransformFromCopy(only_scooter_count, answer1[8]),
                lag_ratio=.5
            )
        )
        self.wait()
        self.play(Write(answer1[9:]))
        self.wait()

        # question 2
        self.play(Circumscribe(question2, fade_out=True))
        self.wait()
        answer2 = MathTex("0", color=BLUE)
        answer2.next_to(question2[1])
        self.play(Write(answer2))
        self.wait()

        # question 3
        self.play(Circumscribe(question3, fade_out=True))
        self.wait()
        answer3 = MathTex("9", color=BLUE)
        answer3.next_to(question3)
        self.play(TransformFromCopy(only_scooter_count, answer3))
        self.wait()

        # question 4
        self.play(Circumscribe(question4, fade_out=True))
        self.wait()
        answer4 = MathTex("18", color=BLUE)
        answer4.next_to(question4)
        self.play(TransformFromCopy(only_bicycle_count, answer4))
        self.wait()

        # question 5
        self.play(Circumscribe(question5, fade_out=True))
        self.wait()
        answer5 = MathTex("6", color=BLUE)
        answer5.next_to(question5)
        self.play(TransformFromCopy(only_ball_count, answer5))
        self.wait()

        self.wait(2)    
