from manim import DOWN, RIGHT, WHITE, LEFT, UP, BLACK, MobjectTable, PI
from manim import Tex, Wiggle, AnimationGroup, ReplacementTransform, VGroup, Brace
from manim import FadeOut, Write
from manim import Scene

from .text import *

UNIT = 0.27

class AttendancePerWeekday(Scene):
    def construct(self):
        minutes =[["$15$"], ["$10$"], ["$15$"], ["$14$"], ["$17$"], ["$14$"], ["$11$"], ["$15$"], ["$14$"], ["$15$"]]
        days = [
            [Tex(january + '$30$'), Tex('$\longrightarrow$')],
            [Tex(january + '$31$'), Tex('$\longrightarrow$')],
            [Tex(february + '$1$'), Tex('$\longrightarrow$')],
            [Tex(february + '$2$'), Tex('$\longrightarrow$')],
            [Tex(february + '$3$'), Tex('$\longrightarrow$')],
            [Tex(february + '$6$'), Tex('$\longrightarrow$')],
            [Tex(february + '$7$'), Tex('$\longrightarrow$')],
            [Tex(february + '$8$'), Tex('$\longrightarrow$')],
            [Tex(february + '$9$'), Tex('$\longrightarrow$')],
            [Tex(february + '$10$'), Tex('$\longrightarrow$')],
        ]

        data = self.get_data_for_table(days, minutes)

        table1 = MobjectTable(
            data[0:5],
            col_labels=[
                Tex(day),
                Tex(time)
            ],
            include_outer_lines=True,
            v_buff=0.5,
            z_index=-5
        )
        table2 = MobjectTable(
            data[5:10],
            col_labels=[
                Tex(day),
                Tex(time)
            ],
            include_outer_lines=True,
            v_buff=0.5,
            z_index=-5
        )

        table1.set_color(BLACK).move_to(LEFT).scale(0.6).shift(UP * 1.5)
        table1.get_horizontal_lines().set_color(WHITE).set_opacity(0)
        table1.get_vertical_lines().set_color(WHITE).set_opacity(0)

        table2.next_to(table1, DOWN).align_to(table1, UP).scale(0.6).shift(DOWN * 1.7)
        scale_factor = 0.6

        for item in data:
            self.play(AnimationGroup(item[0].animate.set_color(WHITE), item[1][0].animate.set_color(WHITE)))
        self.wait()


        brace = Brace(table1.get_rows()[0], color=WHITE)
        self.add(brace.rotate(-1.5 * PI).next_to(data[0][1][0], RIGHT).shift(DOWN * 1.1).stretch(0.65, dim=1))
        consequence_days = Tex(five_consecutive_days)
        self.play(Write(consequence_days.next_to(brace)))
        self.wait()

        week_days = [Tex(monday), Tex(tuesday), Tex(wednesday), Tex(thursday), Tex(friday),
                     Tex(monday), Tex(tuesday), Tex(wednesday), Tex(thursday), Tex(friday)]
        self.play(ReplacementTransform(days[0][0], week_days[0].scale(scale_factor).next_to(days[0][1], LEFT)))
        self.play(Wiggle(week_days[0], n_wiggles=0, scale_value=1.2, run_time=3))
        self.wait()
        self.play(FadeOut(brace, consequence_days))
        self.wait()
        self.play(AnimationGroup(
            *[ReplacementTransform(days[i][0], week_days[i].scale(scale_factor).next_to(days[i][1], LEFT)) for i in
              range(1, len(days))]))
        self.wait()

        self.play(data[5][1][0].animate.next_to(data[0][1][0], RIGHT))
        self.play(
            AnimationGroup(
                days[5][1].animate.set_opacity(0),
                data[5][1][0].animate.set_opacity(0),
                week_days[5].animate.set_color(BLACK).set_opacity(0),
                data[0][1].animate.set_color(WHITE),
            )
        )
        self.wait()
        self.play(AnimationGroup(*[data[i][1][0].animate.next_to(data[i - int(len(days) / 2)][1][0], RIGHT) for i in
                                   range(int(len(days) / 2) + 1, len(days))]))
        self.wait()

        self.play(AnimationGroup(*[AnimationGroup(
            days[i][1].animate.set_opacity(0),
            data[i][1][0].animate.set_opacity(0),
            week_days[i].animate.set_color(BLACK).set_opacity(0),
            data[len(days) - i][1].animate.set_color(WHITE)) for i in range(int(len(days) / 2) + 1, len(days))]))
        self.wait()

        self.play(AnimationGroup(*[data[i][0].animate.remove(days[i][1]) for i in range(int(len(days) / 2))]))
        table1.get_horizontal_lines().set_opacity(1)
        table1.get_vertical_lines().set_opacity(1)

        self.wait()
        for i in range(5):
            week_days[i].set_opacity(0.4)

        self.play(
            AnimationGroup(
                table1.animate.set_opacity(0.4)
            ))
        table1.get_rows()[3].set_opacity(1)
        self.wait(4)

        self.play(table1.animate.set_opacity(1))
        self.wait(2)

    def get_data_for_table(self, days, minutes):
        data = []
        for index in range(len(days)):
            if index < len(days) / 2:
                data.append([VGroup(days[index][0], days[index][1].next_to(days[index][0], RIGHT)),
                             Tex(minutes[index][0] + minute,
                                 " , " + minutes[int(len(minutes) / 2) + index][0] + minute).next_to(
                                 days[index][1], RIGHT)])
            else:
                data.append([VGroup(days[index][0], days[index][1].next_to(days[index][0], RIGHT)),
                             Tex(minutes[index][0] + minute, " , " + minutes[index][0] + minute).next_to(days[index][1],
                                                                                                         RIGHT)])

        return data
