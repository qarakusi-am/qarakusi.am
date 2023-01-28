from manim import Scene, FadeIn, Tex, Write, Line, GrowFromEdge, VGroup, Transform, Indicate, Rectangle, ReplacementTransform, FadeOut, AnimationGroup, Table, CounterclockwiseTransform, SurroundingRectangle, always_redraw
from manim import ORIGIN, UP, LEFT, RIGHT, DOWN, UL, DL
from manim import LIGHT_BROWN, BLACK, WHITE
from objects import SimpleSVGMobject
from qarakusiscene import TaskNumberBox
from random import choice, random
import numpy as np
from .text import *

class Problem12662(Scene):
    def construct(self):
        # task number
        taskNumber = TaskNumberBox(taskNumberString)
        self.play(FadeIn(taskNumber))
        self.wait()

        # door animation
        door = SimpleSVGMobject("door")
        door.scale(3)
        self.play(FadeIn(door))
        self.wait()

        # դռների համարակալում միանիշ թվերով
        door_number1 = Tex("$1$", font_size=50)
        door_number1.align_to(door, UP).shift(DOWN)
        number1_background = Rectangle(LIGHT_BROWN, .5, .33)
        number1_background.move_to(door_number1.get_center()).set_opacity(1)
        self.play(FadeIn(number1_background))
        self.wait()
        self.play(Indicate(number1_background, scale_factor=1.5))
        self.wait()
        self.play(Write(door_number1))
        self.wait()
        
        new_door_number = Tex("$3$", font_size=50)
        new_door_number.move_to(number1_background.get_center())
        self.play(Transform(door_number1, new_door_number))
        self.wait()
        
        new_door_number = Tex("$5$", font_size=50)
        new_door_number.move_to(number1_background.get_center())
        self.play(Transform(door_number1, new_door_number))
        self.wait()

        # դռների համարակալում երկնիշ թվերով
        number2_background = number1_background.copy()
        number2_background.next_to(number1_background, buff=.1)
        door_number2 = Tex("$3$", font_size=50)
        door_number2.move_to(number2_background.get_center())
        VGroup(number2_background, door_number2).set_opacity(0)
        self.play(
            VGroup(
                number1_background, door_number1,
                number2_background, door_number2
            ).animate.move_to(number1_background.get_center()).set_opacity(1)
        )
        self.wait()

        new_door_number = Tex("$2$", font_size=50)
        new_door_number.move_to(number1_background.get_center())
        self.play(Transform(door_number1, new_door_number))
        self.wait()
        
        new_door_number = Tex("$0$", font_size=50)
        new_door_number.move_to(number2_background.get_center())
        self.play(Transform(door_number2, new_door_number))
        self.wait()

        # doors in building
        doors = VGroup(
            *[door.copy() for _ in range(45)]
        ).arrange_in_grid(9, 5, buff=.4).move_to(door.get_center())
        self.play(
            FadeOut(
                number1_background,
                number2_background,
                door_number1,
                door_number2
            )
        )
        self.wait()
        self.play(
            FadeIn(doors),
            VGroup(
                door,
                doors
            ).animate.scale(.13)
        )
        self.remove(door)
        door.scale(1/.13)
        self.wait()

        # բոլոր դռների համարակալում
        door_numbers = []
        for door_index in range(len(doors)):
            number = Tex(f"${door_index+1}$").move_to(doors[len(doors)-1-door_index].get_center()).scale(.7)
            door_numbers.append(number)
        
        self.play(
            AnimationGroup(
                *[Write(number) for number in door_numbers],
                lag_ratio=.5,
                run_time=2
            )
        )
        self.wait()

        # առանձնացնել միանիշ և երկնիշ թվերը
        line1 = Line(ORIGIN, LEFT*4.1)
        line1.to_edge(LEFT).shift(UP*.5)
        mianish_tex = Tex(mianish_str)
        mianish_tex.next_to(line1, UP, aligned_edge=LEFT)
        self.play(Write(mianish_tex))
        self.play(GrowFromEdge(line1, LEFT))
        self.wait()

        line2 = Line(ORIGIN, RIGHT*4.1)
        line2.to_edge(RIGHT).align_to(line1, UP)
        erknish_tex = Tex(erknish_str)
        erknish_tex.next_to(line2, UP, aligned_edge=LEFT)
        self.play(Write(erknish_tex))
        self.play(GrowFromEdge(line2, LEFT))
        self.wait()

        # 1-ը տեղափոխել միանիշների տակ
        mianish_tver = VGroup(
            *[
                Tex(f"${tex}$", font_size=70)
                for tex in range(1, 10)
            ]
        )
        mianish_tver.arrange_in_grid(3, 3, buff=(.55, .55)).next_to(line1, DOWN, buff=.65)
        for num in mianish_tver:
            direction = choice([UP, DOWN, LEFT, RIGHT])
            value = random()
            num.shift(direction*value)
        mianish_tver.scale(.7)
        mianish_tver_doors = VGroup(
            *[
                door.copy().scale(.14).move_to(mianish_tver[number].get_center())
                for number in range(9)
            ]
        )
        
        number1 = VGroup(
            doors[-1],
            door_numbers[0]
        )
        self.play(Indicate(door_numbers[0]), scale_factor=1.5)
        self.wait()
        self.play(
            ReplacementTransform(
                number1,
                VGroup(
                    mianish_tver_doors[0],
                    mianish_tver[0]
                )
            )
        )
        self.wait()
        
        # 16-ը տեղափոխել երկնիշների տակ
        erknish_tver = VGroup(
            *[
                Tex(f"${tex}$", font_size=60)
                for tex in range(10, 46)
            ]
        )
        erknish_tver.arrange_in_grid(6, 7, buff=(.35, .35))
        for num in erknish_tver:
            direction = choice([UP, DOWN, LEFT, RIGHT])
            value = random()
            num.shift(direction*value)
        erknish_tver.scale(.6).next_to(line2, DOWN, aligned_edge=LEFT).to_edge(DOWN)
        erknish_tver[28].shift(RIGHT)
        erknish_tver_doors = VGroup(
            *[
                door.copy().scale(.14).move_to(erknish_tver[number].get_center())
                for number in range(36)
            ]
        )
        
        number16 = VGroup(doors[-16], door_numbers[15])
        self.play(Indicate(door_numbers[15]), scale_factor=1.5)
        self.wait()
        self.play(
            ReplacementTransform(
                number16,
                VGroup(
                    erknish_tver_doors[6],
                    erknish_tver[6]
                )
            )
        )
        self.wait()
        
        # 38-ը տեղափոխել երկնիշների տակ
        number38 = VGroup(
            doors[-38],
            door_numbers[37]
        )
        self.play(Indicate(door_numbers[37]), scale_factor=1.5)
        self.wait()
        self.play(
            ReplacementTransform(
                number38,
                VGroup(
                    erknish_tver_doors[28],
                    erknish_tver[28]
                )
            )
        )
        self.wait()
        
        # 5-ը տեղափոխել միանիշների տակ
        number5 = VGroup(
            doors[-5],
            door_numbers[4]
        )
        self.play(Indicate(door_numbers[4]), scale_factor=1.5)
        self.wait()
        mianish_tver_doors[4] = always_redraw(lambda: mianish_tver_doors[4].move_to(mianish_tver_doors[4].get_center()))
        mianish_tver[4] = always_redraw(lambda: mianish_tver[4].move_to(mianish_tver[4].get_center()))
        self.play(
            ReplacementTransform(
                number5,
                VGroup(
                    mianish_tver_doors[4],
                    mianish_tver[4]
                )
            )
        )
        self.wait()

        # սորտավորել մնացած թվերը
        mnacac_mianish_tver = VGroup(
            *door_numbers[1:4],
            *door_numbers[5:9]
        )
        mianish_tver_doors[0].set_z_index(mianish_tver.z_index+1)
        mianish_tver[0].set_z_index(mianish_tver_doors[4].z_index+1)
        mianish_tver_doors[4].set_z_index(mianish_tver.z_index+1)
        mianish_tver[4].set_z_index(mianish_tver_doors[4].z_index+1)
        self.play(
            *[
                ReplacementTransform(doors[-i-1], mianish_tver_doors[i])
                for i in range(1, 9) if i != 4
            ],
            ReplacementTransform(
                mnacac_mianish_tver,
                VGroup(
                    mianish_tver[1:4],
                    mianish_tver[5:10]
                )
            )
        )
        self.wait()

        mnacac_erknish_tvery = VGroup(
            *door_numbers[9:15],
            *door_numbers[16:37],
            *door_numbers[38:]
        )
        self.play(
            *[
                ReplacementTransform(doors[-i], erknish_tver_doors[i-10])
                for i in range(10, 46) if i != 16 and i != 38
            ],
            ReplacementTransform(
                mnacac_erknish_tvery,
                VGroup(
                    erknish_tver[:6],
                    erknish_tver[7:28],
                    erknish_tver[29:]
                )
            )
        )
        self.wait()

        # arranging doors and numbers
        new_mianish_tver = mianish_tver.copy()
        new_mianish_tver.arrange_in_grid(3, 3, buff=(.55, .55)).next_to(line1, DOWN, buff=.65),
        new_mianish_tver_doors = VGroup(
            *[
                door.copy().scale(.14).move_to(new_mianish_tver[number].get_center())
                for number in range(9)
            ]
        )
        new_erknish_tver = erknish_tver.copy()
        new_erknish_tver.arrange_in_grid(6, 7, buff=(.35, .7))
        new_erknish_tver_doors = VGroup(
            *[
                door.copy().scale(.14).move_to(new_erknish_tver[number].get_center())
                for number in range(36)
            ]
        )
        VGroup(new_erknish_tver, new_erknish_tver_doors).scale(.7).next_to(line2, DOWN, aligned_edge=LEFT).to_edge(DOWN, buff=.07)
        self.play(
            Transform(mianish_tver_doors, new_mianish_tver_doors),
            Transform(mianish_tver, new_mianish_tver),
            Transform(erknish_tver_doors, new_erknish_tver_doors),
            Transform(erknish_tver, new_erknish_tver)
        )
        self.wait()

        # table
        table = Table(
            [
                ["1", "1-9", "9", "9 ⋅ 1"],
                ["2", "10-45", "36", "36 ⋅ 2"]
            ],
            row_labels=[
                Tex(mianish_str),
                Tex(erknish_str)
            ],
            col_labels=[
                Tex(table_col_label1_str),
                Tex(table_col_label2_str),
                Tex(table_col_label3_str),
                Tex(table_col_label4_str)
            ],
            top_left_entry=Tex(top_left_entry_str),
            include_outer_lines=True
        )
        table.scale(.65).to_edge(UP, buff=.88)
        black_rect = Rectangle(BLACK, 4, 13)
        black_rect.set_opacity(1)
        black_rect.align_to(table.get_cell((1, 2)), UL).shift(RIGHT*.05+UP)

        # moving "միանիշ" and "երկնիշ" into table
        VGroup(line1, line2).set_z_index(black_rect.z_index+1)
        self.play(
            AnimationGroup(
                AnimationGroup(
                    ReplacementTransform(
                        mianish_tex,
                        table.get_row_labels()[0]
                    ),
                    line1.animate.align_to(table.get_cell((2, 1)), DL)
                ),
                AnimationGroup(
                    ReplacementTransform(
                        erknish_tex,
                        table.get_row_labels()[1]
                    ),
                    line2.animate.align_to(table.get_cell((3, 1)), DL)
                ),
                AnimationGroup(
                    FadeIn(table),
                    FadeIn(black_rect, run_time=.05)
                ),
                lag_ratio=1
            )
        )
        self.wait()
        
        self.remove(
            table.get_rows()[1][1],
            table.get_rows()[2][1]
        )
        self.play(black_rect.animate.align_to(table.get_cell((1, 3)), UL).shift(RIGHT*.05+UP))
        self.wait()

        # ցույց տալ քանի թվանշան են օգտագործում միանիշ թվերով դռները
        mianish_door = mianish_tver_doors[1].copy()
        self.play(
            mianish_door.animate.scale(4.3).move_to(VGroup(mianish_tver_doors, erknish_tver_doors).get_center())
        )
        self.wait()
        mianish_number_background = number1_background.copy().move_to(mianish_door.get_center()).shift(UP).scale(.8)
        self.play(FadeIn(mianish_number_background))
        self.wait()
        self.play(Indicate(mianish_number_background))
        self.wait()

        # replacing number_background to "1" in table
        self.play(
            ReplacementTransform(
                mianish_number_background,
                table.get_rows()[1][1]
            ),
            FadeOut(mianish_door)
        )
        self.wait()

        # ցույց տալ քանի թվանշան են օգտագործում երկնիշ թվերով դռները
        erknish_door = erknish_tver_doors[1].copy()
        self.play(
            erknish_door.animate.scale(6.5).move_to(VGroup(mianish_tver_doors, erknish_tver_doors).get_center())
        )
        self.wait()
        erknish_numbers_background = VGroup(
            number1_background.copy(),
            number1_background.copy().next_to(number1_background, buff=.1)
        ).move_to(erknish_door.get_center()).shift(UP*1.1).scale(.8)
        self.play(FadeIn(erknish_numbers_background))
        self.wait()
        self.play(Indicate(erknish_numbers_background))
        self.wait()
        self.play(
            ReplacementTransform(
                erknish_numbers_background,
                table.get_rows()[2][1]
            ),
            FadeOut(erknish_door)
        )
        self.wait()

        # replacing doors to "1-9"
        self.remove(
            table.get_rows()[1][2],
            table.get_rows()[2][2]
        )
        self.play(black_rect.animate.align_to(table.get_cell((1, 4)), UL).shift(RIGHT*.05+UP))
        self.wait()
        self.play(
            ReplacementTransform(
                VGroup(
                    mianish_tver,
                    mianish_tver_doors
                ),
                table.get_rows()[1][2]
            )
        )
        self.wait()

        # replacing doors to "10-45"
        self.play(
            ReplacementTransform(
                VGroup(
                    erknish_tver,
                    erknish_tver_doors
                ),
                table.get_rows()[2][2]
            )
        )
        self.wait()

        # removing line1, line2 and scaling and moving center
        self.remove(line1, line2)
        self.play(
            VGroup(
                table,
                black_rect
            ).animate.scale(1.2).shift(DOWN*1.5+RIGHT)
        )

        # count of numbers
        self.remove(
            table.get_rows()[1][3],
            table.get_rows()[2][3]
        )
        self.play(black_rect.animate.align_to(table.get_cell((1, 5)), UL).shift(UP))
        self.wait()
        self.play(Write(table.get_rows()[1][3]))
        self.wait()
        self.play(Write(table.get_rows()[2][3]))
        self.wait()

        # թվանշանների քանակ
        self.remove(
            table.get_rows()[1][4],
            table.get_rows()[2][4]
        )
        self.play(black_rect.animate.shift(RIGHT*4))
        self.wait()
        
        # 9 * 1
        temp = table.get_rows()[1][3].copy()
        self.play(
            CounterclockwiseTransform(
                temp,
                table.get_rows()[1][4][0][0],
                path_arc=np.pi/2
            )
        )
        self.wait()
        self.add(table.get_rows()[1][4][0][0])
        self.remove(temp)

        self.play(Write(table.get_rows()[1][4][0][1]))
        self.wait()

        temp = table.get_rows()[1][1].copy()
        self.play(
            CounterclockwiseTransform(
                temp,
                table.get_rows()[1][4][0][2],
                path_arc=np.pi/1.5
            )
        )
        self.wait()
        self.add(table.get_rows()[1][4][0][2])
        self.remove(temp)

        # 36 * 2
        temp = table.get_rows()[2][3].copy()
        self.play(
            CounterclockwiseTransform(
                temp,
                table.get_rows()[2][4][0][:2]
            )
        )
        self.wait()
        self.add(table.get_rows()[2][4][0][:2])
        self.remove(temp)

        self.play(Write(table.get_rows()[2][4][0][2]))
        self.wait()

        temp = table.get_rows()[2][1].copy()
        self.play(
            CounterclockwiseTransform(
                temp,
                table.get_rows()[2][4][0][3],
                path_arc=np.pi/2
            )
        )
        self.wait()
        self.add(table.get_rows()[2][4][0][3])
        self.remove(temp)

        # transforming "9*1" to "9"
        temp = Tex("$9$")
        temp.match_height(table.get_rows()[1][4]).move_to(table.get_rows()[1][4].get_center())
        self.play(
            Transform(
                table.get_rows()[1][4],
                temp
            )
        )
        self.wait()

        # transforming "36*2" to "72"
        temp = Tex("$72$")
        temp.match_height(table.get_rows()[2][4]).move_to(table.get_rows()[2][4].get_center())
        self.play(
            Transform(
                table.get_rows()[2][4],
                temp
            )
        )
        self.wait()

        # total
        total_tex = Tex(total_str, "$9$", " $+$ ", "$72$", font_size=65)
        total_rect = SurroundingRectangle(total_tex, color=WHITE)
        VGroup(total_rect, total_tex).next_to(table, DOWN, 0, aligned_edge=RIGHT)

        self.play(FadeIn(total_rect))
        self.wait()
        self.play(Write(total_tex[0]))
        self.wait()

        self.play(
            ReplacementTransform(
                table.get_rows()[1][4].copy(),
                total_tex[1]
            ),
            ReplacementTransform(
                table.get_rows()[2][4].copy(),
                total_tex[3]
            ),
            Write(total_tex[2])
        )
        self.wait()

        temp = Tex("$81$", font_size=65)
        temp.move_to(total_tex[1:].get_center())
        self.play(
            Transform(
                total_tex[1:],
                temp
            )
        )

        self.wait(2)
