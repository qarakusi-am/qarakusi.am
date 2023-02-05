from manim import Scene, FadeIn, Tex, MathTex, Write, VGroup, AnimationGroup, Transform, Indicate, Table, ReplacementTransform, Group, Wiggle
from manim import UL, UP, UR, DOWN, RIGHT, LEFT, ORIGIN
from qarakusiscene import TaskNumberBox
from objects import BagOfMandarins, SimpleSVGMobject
from numpy import pi, array
from .text import *

COUNT_FONTSIZE = 70

class Problem10343(Scene):
    def construct(self):
        # task number
        taskNumber = TaskNumberBox(taskNumberString)
        self.play(FadeIn(taskNumber))
        self.wait()

        # մանդարիններ
        bag_of_mandarins = BagOfMandarins(svg_index=3)
        bag_of_mandarins.scale(1.5)
        count_of_mandarins = MathTex("125", font_size=COUNT_FONTSIZE)
        count_of_mandarins.move_to(bag_of_mandarins.get_center())
        VGroup(
            bag_of_mandarins,
            count_of_mandarins
        ).to_edge(UL).shift(DOWN*1.6+RIGHT)

        # խնձորներ
        box_of_apples = SimpleSVGMobject("apples_with_box")
        box_of_apples.scale(.8)
        count_of_apples = MathTex("178", font_size=COUNT_FONTSIZE)
        count_of_apples.move_to(box_of_apples.get_center()).shift(DOWN*.3)
        VGroup(
            box_of_apples,
            count_of_apples
        ).next_to(bag_of_mandarins, DOWN, aligned_edge=RIGHT)

        # բանաններ
        box_of_bananas = SimpleSVGMobject("bananas_with_box")
        box_of_bananas.scale(.9)
        count_of_bananas = MathTex("45", font_size=COUNT_FONTSIZE)
        count_of_bananas.move_to(box_of_bananas.get_center())
        matrix = array(
            [
                [5.5, -.85],
                [-.5, 1.6]
            ]
        ).T
        matrix[0]/=matrix[0].dot(matrix[0])**.5
        matrix[1]/=matrix[1].dot(matrix[1])**.5
        matrix/=1.2
        count_of_bananas.apply_matrix(matrix).shift(DOWN*.31+LEFT*.25)
        VGroup(
            box_of_bananas,
            count_of_bananas
        ).next_to(box_of_apples, DOWN, aligned_edge=RIGHT)

        # FadeIn mandarins, aplles and bananas
        self.play(
            AnimationGroup(
                AnimationGroup(
                    FadeIn(bag_of_mandarins),
                    Write(count_of_mandarins),
                    lag_ratio=.6
                ),
                AnimationGroup(
                    FadeIn(box_of_apples),
                    Write(count_of_apples),
                    lag_ratio=.6
                ),
                AnimationGroup(
                    FadeIn(box_of_bananas),
                    Write(count_of_bananas),
                    lag_ratio=.6
                ),
                lag_ratio=.7
            )
        )

        # սկուտեղ
        empty_tray = SimpleSVGMobject("tray")
        fruits_for_tray = SimpleSVGMobject("fruits_for_tray")
        fruits_for_tray.match_width(empty_tray).next_to(empty_tray, UP, buff=0).shift(DOWN*.2)
        empty_tray.set_z_index(fruits_for_tray.z_index+1)
        tray = VGroup(fruits_for_tray, empty_tray).scale(.7)
        tray.to_edge(RIGHT)

        self.play(FadeIn(tray[1]))

        # 4 մանդարին
        mandarin = SimpleSVGMobject("mandarin")
        mandarin.scale(.3)
        mandarins_4x = VGroup(*[mandarin.copy() for _ in range(4)])
        mandarins_4x.arrange().next_to(bag_of_mandarins, buff=.4)
        bag_of_mandarins.set_z_index(bag_of_mandarins.z_index+1)
        count_of_mandarins.set_z_index(count_of_mandarins.z_index+1)
        self.play(
            AnimationGroup(
                *[
                    ReplacementTransform(
                        mandarin.copy().move_to(bag_of_mandarins.get_center()).set_z_index(bag_of_mandarins.z_index-1),
                        mandarins_4x[i],
                        path_arc=-pi/2
                    )
                    for i in range(4)
                ],
                lag_ratio=.4,
                run_time=1.3
            )
        )
        self.wait()

        # 6 խնձոր
        apple = SimpleSVGMobject("green_apple")
        apple.scale(1.5)
        apples_6x = VGroup(*[apple.copy() for _ in range(6)])
        apples_6x.arrange().next_to(box_of_apples).align_to(mandarins_4x, LEFT)
        box_of_apples.set_z_index(box_of_apples.z_index+1)
        count_of_apples.set_z_index(count_of_apples.z_index+1)
        self.play(
            AnimationGroup(
                *[
                    ReplacementTransform(
                        apple.copy().move_to(box_of_apples.get_center()).set_z_index(bag_of_mandarins.z_index-1),
                        apples_6x[i],
                        path_arc=-pi/2
                    )
                    for i in range(6)
                ],
                lag_ratio=.4,
                run_time=1.5
            )
        )
        self.wait()

        # 2 բանան
        banana = SimpleSVGMobject("banana")
        banana.scale(1.6)
        bananas_2x = VGroup(*[banana.copy() for _ in range(2)])
        bananas_2x.arrange().next_to(box_of_bananas).align_to(mandarins_4x, LEFT)
        box_of_bananas.set_z_index(box_of_bananas.z_index+1)
        count_of_bananas.set_z_index(count_of_bananas.z_index+1)
        self.play(
            AnimationGroup(
                *[
                    ReplacementTransform(
                        banana.copy().move_to(box_of_bananas.get_top()).set_z_index(bag_of_mandarins.z_index-1),
                        bananas_2x[i],
                        path_arc=-pi/4
                    )
                    for i in range(2)
                ],
                lag_ratio=.4,
                run_time=.5
            )
        )
        self.wait()
        
        # transforming copies of fruits to tray with fruits
        self.play(
            ReplacementTransform(
                VGroup(
                    mandarins_4x,
                    apples_6x,
                    bananas_2x
                ).copy(),
                tray[0]
            )
        )
        self.wait()

        # table
        table = Table(
            [
                ["125", "4", "125:4=31 (1 "+remainder_str+")"],
                ["178", "6", "178:6=29 (4 "+remainder_str+")"],
                ["45", "2", "45:2=22 (1 "+remainder_str+")"]
            ],
            row_labels=[
                mandarin.copy(),
                apple.copy(),
                banana.copy()
            ],
            col_labels=[
                Tex(quantity_str),
                Tex(tray_str),
                SimpleSVGMobject("trays_with_fruits").scale(.7)
            ],
            top_left_entry=Tex(fruit_str),
            include_outer_lines=True,
            v_buff=.55,
            h_buff=.65
        )
        tray_in_table = tray.copy().scale(.5)
        tray_in_table.move_to(table.col_labels[1])
        table.col_labels[1].set_opacity(0)

        # transform tray, 4x mandarins, 6x aplles and 2x bananas to parts of table
        self.play(
            ReplacementTransform(
                    tray,
                    tray_in_table
            ),
            mandarins_4x.animate.scale(.8).next_to(table.get_rows()[1][1], buff=.7),
            apples_6x.animate.scale(.8).next_to(table.get_rows()[2][1]).align_to(
                mandarins_4x.copy().scale(.8).next_to(table.get_rows()[1][1], buff=.7),
                LEFT
            ),
            bananas_2x.animate.scale(.8).next_to(table.get_rows()[3][1]).align_to(
                mandarins_4x.copy().scale(.8).next_to(table.get_rows()[1][1], buff=.7),
                LEFT
            )
        )
        self.wait()
        self.play(
            AnimationGroup(
                ReplacementTransform(
                    mandarins_4x,
                    table.get_rows()[1][2]
                ),
                ReplacementTransform(
                    apples_6x,
                    table.get_rows()[2][2]
                ),
                ReplacementTransform(
                    bananas_2x,
                    table.get_rows()[3][2]
                ),
                lag_ratio=.6
            )
        )
        self.wait()

        # transform bags and numbers to parts of table
        self.play(
            AnimationGroup(
                AnimationGroup(
                    AnimationGroup(
                        ReplacementTransform(
                            bag_of_mandarins,
                            table.row_labels[0]
                        ),
                        ReplacementTransform(
                            count_of_mandarins,
                            table.get_rows()[1][1]
                        )
                    ),
                    AnimationGroup(
                        ReplacementTransform(
                            box_of_apples,
                            table.row_labels[1]
                        ),
                        ReplacementTransform(
                            count_of_apples,
                            table.get_rows()[2][1]
                        )
                    ),
                    AnimationGroup(
                        ReplacementTransform(
                            box_of_bananas,
                            table.row_labels[2]
                        ),
                        ReplacementTransform(
                            count_of_bananas,
                            table.get_rows()[3][1]
                        )
                    ),
                    lag_ratio=0
                ),
                FadeIn(
                    table[1:],
                    table.col_labels[0],
                    table.top_left_entry
                ),
                lag_ratio=.4
            )
        )
        self.wait()

        # Քանի՞ սկուտեղ կլինի
        self.play(FadeIn(table.col_labels[2]))
        self.wait()

        # mandarins
        tex1 = MathTex("125", ":", "4", "= 31 (1 \\text{"+remainder_str+"})", font_size=55)
        tex1.align_to(table.get_rows()[1][3], UL)

        self.play(
            ReplacementTransform(
                table.get_rows()[1][1].copy(),
                tex1[0],
                path_arc=pi/2
            )
        )
        self.wait()

        self.play(Write(tex1[1]))
        self.play(
            ReplacementTransform(
                table.get_rows()[1][2].copy(),
                tex1[2],
                path_arc=pi/2
            )
        )
        self.wait()

        self.play(Write(tex1[3]))
        self.wait()

        # apples
        tex2 = MathTex("178", ":", "6", "= 29 (4 \\text{"+remainder_str+"})", font_size=55)
        tex2.align_to(table.get_rows()[2][3], UL)

        self.play(
            ReplacementTransform(
                table.get_rows()[2][1].copy(),
                tex2[0],
                path_arc=pi/2
            )
        )
        self.wait()

        self.play(Write(tex2[1]))
        self.play(
            ReplacementTransform(
                table.get_rows()[2][2].copy(),
                tex2[2],
                path_arc=pi/2
            )
        )
        self.wait()

        self.play(Write(tex2[3]))
        self.wait()

        # bananas
        tex3 = MathTex("45", ":", "2", "= 22 (1 \\text{"+remainder_str+"})", font_size=55)
        tex3.align_to(table.get_rows()[3][3], UL)

        self.play(
            ReplacementTransform(
                table.get_rows()[3][1].copy(),
                tex3[0],
                path_arc=pi/2
            )
        )
        self.wait()

        self.play(Write(tex3[1]))
        self.play(
            ReplacementTransform(
                table.get_rows()[3][2].copy(),
                tex3[2],
                path_arc=pi/2
            )
        )
        self.wait()

        self.play(Write(tex3[3]))
        self.wait()

        # transform "125 : 4 = 31(1մն.)" to "31 (1մն.)"
        new_tex1 = MathTex("31", font_size=75)
        remainder1 = MathTex("(1\\text{"+remainder_str+"})", font_size=75).next_to(new_tex1)
        VGroup(new_tex1, remainder1).move_to(tex1.get_center())
        self.play(Transform(tex1, VGroup(new_tex1, remainder1)))
        self.wait()

        # transform "178 : 6 = 29(4մն.)" to "29 (4մն.)"
        new_tex2 = MathTex("29", font_size=75)
        remainder2 = MathTex("(4\\text{"+remainder_str+"})", font_size=75).next_to(new_tex2)
        VGroup(new_tex2, remainder2).move_to(tex2.get_center())
        self.play(Transform(tex2, VGroup(new_tex2, remainder2)))
        self.wait()

        # transform "45 : 2 = 22(1մն.)" to "22 (1մն.)"
        new_tex3 = MathTex("22", font_size=75)
        remainder3 = MathTex("(1\\text{"+remainder_str+"})", font_size=75).next_to(new_tex3)
        VGroup(new_tex3, remainder3).move_to(tex3.get_center())
        self.play(ReplacementTransform(tex3, VGroup(new_tex3, remainder3)))
        self.wait()

        self.play(Indicate(VGroup(new_tex3, remainder3)))
        self.wait()

        # scaling table and moving up left corner
        table = Group(*[obj for obj in self.mobjects])
        table.remove(taskNumber)
        self.play(table.animate.scale(.6).to_edge(UL).shift(DOWN*.8))
        remainder3_copy = remainder3.copy()
        self.wait()

        # tray x22
        self.play(Wiggle(new_tex3))
        self.wait()
        trays_22x = VGroup(*[tray.copy().scale(.7) for _ in range(22)])
        trays_22x.arrange_in_grid(2).move_to(ORIGIN).to_edge(DOWN)
        self.play(ReplacementTransform(new_tex3.copy(), trays_22x))
        self.wait()

        # ցույց տալ ինչ է մնացել սկուտեղները լցնելուց հետո
        banana_1x = banana.copy().scale(1.2).to_corner(UR).shift(DOWN*1.7+LEFT*2)
        self.play(remainder3_copy.animate.move_to(banana_1x.get_center()))
        self.wait()
        self.play(ReplacementTransform(remainder3_copy, banana_1x))
        self.wait()

        apples_46x = SimpleSVGMobject("green_apples").scale(.7).next_to(banana_1x, LEFT, buff=.4)
        self.play(FadeIn(apples_46x))
        self.wait()

        mandarins_37x = SimpleSVGMobject("mandarins").scale(2).next_to(banana_1x, RIGHT, buff=.4)
        self.play(FadeIn(mandarins_37x))
        self.wait()

        self.wait(2)
