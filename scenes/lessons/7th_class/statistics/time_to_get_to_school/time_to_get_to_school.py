import numpy as np
import statistics
from manim import DOWN, RIGHT, ORIGIN, WHITE, linear, Table, LEFT, UP, RED, BLACK, MobjectTable
from manim import Tex, Wiggle, AnimationGroup, ReplacementTransform, VGroup, TransformFromCopy, Line
from manim import FadeIn, FadeOut, Write
from manim import Scene, Arrow
from objects import SimpleSVGMobject
from hanrahashiv import FormulaModificationsScene, ModifyFormula
from .text import *

UNIT = 0.27

class TimeToGetToSchool(Scene):
    def construct(self):

        school_child_pos = [0, 0, 0]
        school_child = SimpleSVGMobject("people/children/girl_1", color=WHITE).move_to(school_child_pos)

        school_pos = [5.5, 0, 0]
        school = SimpleSVGMobject("buildings/building_3").move_to(school_pos)

        self.play(FadeIn(school_child),
                  FadeIn(school))

        arrow = Arrow(start=ORIGIN,end=school_pos,buff=1).set_length(2)
        self.play(arrow.animate(rate_func=linear, run_time=2))
        self.wait(0.5)

        minutes_for_table_rows = ["$15$","$10$","$15$","$14$","$17$","$14$","$11$","$15$","$14$","$15$"]
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

        data = self.get_data_for_table(days, minutes_for_table_rows)
        minutes = np.array([["15"], ["10"], ["15"], ["14"], ["17"], ["14"], ["11"], ["15"], ["14"], ["15"]])


        table = MobjectTable(
            data,
            col_labels=[
                Tex(day),
                Tex(time)
            ],
            include_outer_lines=True,
            v_buff=0.5,
            z_index=-5
        )

        table.get_horizontal_lines().set_opacity(0)
        table.get_vertical_lines().set_opacity(0)

        # hide those lines of table that may overlay school_child
        for index in range(4, 6):
            table.get_rows()[index].set_opacity(0)

        self.play(AnimationGroup(table.set_color(BLACK).scale(0.6).create(),table.get_rows()[1].animate.set_color(WHITE)))
        self.wait()

        self.play( table.get_rows()[2].animate.set_color(WHITE))
        self.wait()

        self.play(FadeOut(school_child,school,arrow))

        # show hidden lines
        for index in range(4,6):
            table.get_rows()[index].set_opacity(1)

        for index in range(2,len(data)):
            self.play(table.get_rows()[index + 1].animate.set_color(WHITE))

        #did arrow deletion this way, to be faster(simultaneous)

        self.play(AnimationGroup(*[data[i][0].animate.remove(days[i][1]) for i in range(len(days))]))
        self.wait()

        table.get_horizontal_lines().set_opacity(1)
        table.get_vertical_lines().set_opacity(1)

        self.play(table.animate.set_color(WHITE))
        self.wait()

        table.get_rows()[2].set_opacity(1)
        self.play(
            AnimationGroup(
             table.animate.set_opacity(0.4),
             table.get_rows()[2].animate.set_opacity(1))
        )
        table.get_rows()[2].set_opacity(1)
        self.wait(2)

        self.play(
            AnimationGroup(
            table.get_rows()[2].animate.set_opacity(0.4),
            table.get_rows()[3].animate.set_opacity(1))
        )
        self.wait(2)

        self.play(table.animate.set_opacity(1))
        self.wait()

        minutes = [int(numeric_string) for numeric_string in minutes.ravel()]
        minutes.sort()
        first_element, last_element, mode_value, mode_numbers, total_minutes_text = self.get_elements_from_list(minutes)

        self.play(ReplacementTransform(table, total_minutes_text.scale(1.2).shift(LEFT).move_to(DOWN * 2)))
        self.play(AnimationGroup(Wiggle(first_element, scale_value=1.5), Wiggle(last_element, scale_value=1.5)))
        self.wait()

        width_equality = str(minutes[- 1]) + " - " + str(minutes[0]) + " = " + str(
            minutes[len(minutes) - 1] - minutes[0])
        width_text = Tex(width_equality + "  $\longrightarrow$  " + width)
        self.play(Write(width_text.move_to(UP * 3).shift(LEFT * 3)))

        first_equality_sign = Tex(" = ")
        second_equality_sign = Tex(" = ")

        sum_nominator = " + ".join([str(i) for i in minutes])

        scale_factor = .8
        sum_nominator = Tex(sum_nominator)
        sum_fraction_line = Line(ORIGIN)
        sum_denominator = Tex(len(minutes))
        sum_fraction = VGroup(sum_fraction_line, sum_nominator, sum_denominator)
        sum_fraction.scale(scale_factor)

        self.play(TransformFromCopy(total_minutes_text, sum_nominator.next_to(total_minutes_text, UP * 6).shift(LEFT)))
        self.play(FadeIn(sum_fraction_line.next_to(sum_nominator, DOWN).scale(12)),
                  Write(sum_denominator.next_to(sum_fraction_line, DOWN)))
        self.wait()

        result_denominator=Tex(len(minutes))
        result_fraction_line=Line(ORIGIN)
        result_numerator=Tex(str(sum(minutes)))
        result_fraction=VGroup(first_equality_sign.next_to(sum_fraction_line,RIGHT),result_numerator.next_to(sum_nominator,RIGHT).shift(RIGHT),
                               result_fraction_line.next_to(result_numerator,DOWN),
                               result_denominator.next_to(result_fraction_line,DOWN),second_equality_sign.next_to(result_fraction_line,RIGHT))
        quotient=Tex(str(int(sum(minutes)/len(minutes))))

        self.play(Write(result_fraction.scale(scale_factor)))
        self.play(Write(quotient.next_to(result_fraction).scale(scale_factor)))
        self.play(FadeOut(
            result_fraction,
            sum_fraction
        ))
        self.wait(0.4)

        self.play(quotient.animate.next_to(width_text,DOWN).align_to(width_text,LEFT).scale(1/scale_factor))

        average_time_text=Tex(minute+' $\longrightarrow$ '+average_time)
        self.play(Write(average_time_text.next_to(quotient,RIGHT)))
        self.wait()


        self.play(Wiggle(VGroup(mode_numbers[0],mode_numbers[2],mode_numbers[4],mode_numbers[6]).set_color(RED),scale_value=1.2))

        mode_upper_texts=VGroup()
        for item in mode_numbers[::2]:
            mode_text = Tex(mode)
            mode_upper_texts.add(mode_text.next_to(item, UP).scale(0.6))

        mode_text = Tex(str(mode_value) +minute+ " $\longrightarrow$  " +mode)

        self.play(AnimationGroup(Write(mode_upper_texts)))
        self.play(TransformFromCopy(mode_upper_texts,mode_text.next_to(average_time_text,DOWN).align_to(width_text,LEFT)))
        self.wait()

        total_minutes_text.add(mode_upper_texts)
        sorted_time_text=VGroup()
        frequency_table_array=[]
        sorted_time_array=self.get_elements_frequency_array(minutes)

        for sorted_time in sorted_time_array:
            frequency_table_array.append([sorted_time[0].get_tex_string(),sorted_time[1]])
            sorted_time_text.add(sorted_time[0].next_to(sorted_time_text,DOWN).align_to(width_text,LEFT))

        self.play(ReplacementTransform(total_minutes_text,sorted_time_text))

        self.draw_frequency_table(frequency_table_array,sorted_time_text)

    def get_data_for_table(self, days, minutes):
        data = []
        for index in range(len(days)):
            data.append([VGroup(days[index][0], days[index][1].next_to(days[index][0], RIGHT)),
                         Tex(minutes[index] + minute).next_to(days[index][1], RIGHT)])
        return data

    def get_elements_from_list(self, minutes):

        first_element = Tex(str(minutes[0]))
        last_element = Tex(str(minutes[len(minutes) - 1]))
        mode_value = statistics.mode(minutes)
        mode_numbers = Tex('$15$ ', ' $ , $ ', ' $15$ ', ' $ , $ ', ' $15$ ', ' $ , $ ', ' $15$ ', ' $ , $ ')
        numbers_before_mode = ""
        numbers_after_mode = ""

        for index in range(1,len(minutes)-1):
            if minutes[index] < mode_value:
                if numbers_before_mode == "":
                    numbers_before_mode = " , "
                numbers_before_mode += str(minutes[index])
                numbers_before_mode += " , "
            elif minutes[index] > mode_value:
                if numbers_after_mode == "":
                    numbers_after_mode = " , "
                numbers_after_mode += str(minutes[index])
                numbers_after_mode += " , "

        numbers_before_mode = Tex(numbers_before_mode)
        numbers_after_mode = Tex(numbers_after_mode)
        total_minutes_text = VGroup(first_element, numbers_before_mode.next_to(first_element))

        total_minutes_text.add(mode_numbers.next_to(total_minutes_text))
        total_minutes_text.add(numbers_after_mode.next_to(total_minutes_text))
        total_minutes_text.add(last_element.next_to(total_minutes_text))

        return first_element, last_element, mode_value, mode_numbers, total_minutes_text

    def get_elements_frequency_array(self, elements):

        current_element_index = 0
        sorted_array = []
        while current_element_index < len(elements):
            count = elements.count(elements[current_element_index])
            if count == 1:
                sorted_array.append([Tex(str(elements[current_element_index])), str(count)])
            else:
                text = ""
                for index in range(count):
                    text += str(elements[current_element_index])
                    if index != count - 1:
                        text += " ,"
                sorted_array.append([Tex(text), str(count)])
            current_element_index += count

        return sorted_array

    def draw_frequency_table(self, data, position):
        frequency_table = Table(
            data,
            col_labels=[
                Tex(data_str),
                Tex(count)
            ],
            include_outer_lines=True
        )
        self.play(
            AnimationGroup(
                frequency_table.set_color(BLACK).next_to(position, RIGHT).shift(UP * 0.6).scale(0.6).create(),
                frequency_table.get_vertical_lines().animate.set_color(WHITE),
                frequency_table.get_horizontal_lines().animate.set_color(WHITE))
        )

        self.play(frequency_table.get_columns()[0].animate.set_color(WHITE))
        self.wait()

        for index in  range(len(data)):
            self.play(
                TransformFromCopy(
                    frequency_table.get_cell((index + 2, 1)),
                    frequency_table.get_cell((index + 2, 0)),
                )
            )
            self.play(frequency_table.get_rows()[index + 1].animate.set_color(WHITE))

        self.play(frequency_table.get_rows()[0].animate.set_color(WHITE))
        self.wait()

        self.play(Write(Tex(frequency_table_str).scale(0.7).next_to(frequency_table, DOWN)))
        self.wait()
