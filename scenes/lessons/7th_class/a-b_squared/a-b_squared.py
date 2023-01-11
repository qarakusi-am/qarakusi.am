from manim import GREEN
from manim import UP, LEFT, DOWN, RIGHT, UL, UR, TAU, ORIGIN, PI
from manim import Write, Create, FadeOut, Circumscribe, Indicate, Wiggle
from manim import AnimationGroup, Transform, ReplacementTransform, ClockwiseTransform
from manim import there_and_back, there_and_back_with_pause
from manim import Tex, VGroup, Circle, SurroundingRectangle, DashedLine

from hanrahashiv import ModifyFormula, FormulaModificationsScene
from segment import ConnectionLine

class AMinusBSquared(FormulaModificationsScene):

    def construct(self):
        self.forty_nine_squared = Tex(
            '$49$', '$^2$', ' $=$ ', '$($', '$50$', '$-$', '$1$', '$)$', '$^2$',
            font_size=60
        ) # 49^2 = (50-1)^2

        self.a_minus_b_squared_extended = Tex(
            '$($', '$a$', '$-$', '$b$', '$)$', '$^2$', # 0:6
            ' $=$ ', '$($', '$a$', '$-$', '$b$', '$)$', '$\cdot$', '$($', '$a$', '$-$', '$b$', '$)$', # 6:18
            ' $=$ ', '$a$', '$\cdot$', '$a$', '$+$', '$a$', '$\cdot$', '$($', '$-$', '$b$', '$)$', '$+$', # 18:31
            '$($', '$-$', '$b$', '$)$', '$\cdot$', '$a$', '$+$', '$($', '$-$', '$b$', '$)$', '$\cdot$', '$($', '$-$', '$b$', '$)$', #31:46
            font_size=50
        ) # (a-b)^2 = (a-b)•(a-b) = a•a + a•(-b) + (-b)•a + (-b)•(-b)

        self.a_minus_b_squared = Tex(
            '$($', '$a$', '$-$', '$b$', '$)$', '$^2$', # 0:6
            ' $=$ ', '$a$', '$^2$', '$-$', '$2$', '$a$', '$b$', '$+$', '$b$', '$^2$', # 6:16
            font_size=60
        ) # (a-b)^2 = a^2-2ab+b^2
        self.surr_rect_a_minus_b_squared = SurroundingRectangle(self.a_minus_b_squared, color=GREEN).to_corner(UR)

        self.a_plus_b_squared = Tex(
            '$($', '$a$', '$+$', '$b$', '$)$', '$^2$', # 0:6
            ' $=$ ', '$a$', '$^2$', '$+$', '$2$', '$a$', '$b$', '$+$', '$b$', '$^2$', # 6:16
            font_size=60
        ) # (a+b)^2 = a^2+2ab+b^2

        self.b_minus_a_squared = Tex(
            '$($', '$b$', '$-$', '$a$', '$)$', '$^2$', # 0:6
            ' $=$ ', '$b^2$', '$-$', '$2$', '$b$', '$a$', '$+$', '$a^2$', # 6:14
            font_size=60
        ) # (b-a)^2 = b^2 - 2ba + a^2

        self.recap_and_get_stuck() # 51^2=(50+1)^2=2601, 49^2=(40+9)^2=2401, 49^2=(50-1)^2=???
        self.get_formula() # (a-b)^2=a^2-2ab+b^2
        self.compare_with_square_of_sum() # show difference between two formulas
        self.calculate_forty_nine_squared() # 49^2 = (50-1)^2 = 50^2 - 2•50•1 + 1^2 = 2401
        self.animate_b_minus_a_squared() # show that (b-a)^2=(a-b)^2
        self.exercise_x_minus_3_squared() # (x-3)^2 = x^2-6x+9
        self.last_exercise() # (2-z)^2 = ?

    def recap_and_get_stuck(self):
        """
        Write 51^2 = (50+1)^2 = 50^2+2•50•1+1^2=2601 as we learned in previous lessons
        Use same method to calculate 49^2, get (40+9)^2 = 40^2+2•40•9+9^2=2401
        Try to calculate 49^2 by another approach - (50-1)^2 and get stuck
        """
        # 51^2 = (50+1)^2 = 50^2 + 2•50•1 + 1^2
        fifty_one_squared = Tex(
            '$51^2$', ' $=$ ', '$(50+1)^2$', ' $=$ ', '$50^2 + 2$$\cdot$$50$$\cdot$$1 + 1^2$', ' $=$ ', '$2601$',
            font_size=60
        )
        fifty_one_squared.shift(UP).to_edge(LEFT)
        self.play(Write(fifty_one_squared[0]))
        self.wait(0.25)
        self.play(Write(fifty_one_squared[1:3]))
        self.wait(0.25)
        self.play(Write(fifty_one_squared[3:]))
        self.wait()

        # 49^2 = (40+9)^2 = 40^2 + 2•40•9 + 9^2
        forty_nine_squared_1 = Tex(
            '$49^2$', ' $=$ ', '$(40+9)^2$',
            ' $=$ ', '$40^2$', '$+ 2$$\cdot$$40$$\cdot$$9$', '$+ 9^2$',
            ' $=$ ', '$2401$',
            font_size=60
        ) # 49^2 = (40+9)^2 = 40^2 +2•40•9 + 9^2 = 2401
        forty_nine_squared_1.next_to(fifty_one_squared, DOWN, buff=0.75, aligned_edge=LEFT)
        calculations = VGroup(*Tex('$1600 + 720 + 81$', font_size=60)[0])
        calculations.next_to(forty_nine_squared_1[4:7], DOWN, buff=0.5)

        self.play(Write(forty_nine_squared_1[0]))
        self.wait(0.25)
        self.play(Write(forty_nine_squared_1[1:3]))
        self.wait(0.25)
        for i in [3, 4, 5, 6]:
            self.play(Write(forty_nine_squared_1[i]))
            self.wait(0.25)
        self.play(Write(calculations[0:4]))
        self.wait(0.5)
        self.play(Write(calculations[4:8]))
        self.wait(0.5)
        self.play(Write(calculations[8:]))
        self.wait(0.5)

        self.play(Transform(calculations, Tex('$2401$', font_size=60).move_to(calculations)))
        self.wait()
        self.play(
            Write(forty_nine_squared_1[-2]),
            ReplacementTransform(calculations, forty_nine_squared_1[-1:])
        )
        self.wait()

        # try another approach and get stuck - 49^2=(50-1)^2
        self.forty_nine_squared.next_to(forty_nine_squared_1, DOWN, buff=0.75, aligned_edge=LEFT)
        self.play(Write(self.forty_nine_squared[0:2]))
        self.wait(0.5)
        self.play(Write(self.forty_nine_squared[2:]))
        self.wait()

        self.play(Circumscribe(self.forty_nine_squared[4:7], fade_out=True, run_time=2))
        self.wait()

        self.play(
            AnimationGroup(
                FadeOut(fifty_one_squared, forty_nine_squared_1),
                self.forty_nine_squared.animate.to_corner(UL),
                lag_ratio=0.5
            )
        )
        self.wait()

    def get_formula(self):
        """
        Write (a-b)^2 = (a-b)(a-b)
        Open parenthesis
        Write formula in perfect form
        Final result is (a-b)^2=a^2-2ab+b^2
        """

        def write_beginning_of_formula(): # (a-b)^2 = (a-b)•(a-b) =
            """
                Writes (a-b)^2 =(a-b)•(a-b) =   in 3 steps
            """
            self.play(Write(a_minus_b_squared_extended[0:6])) # (a-b)^2
            self.wait()
            self.play(Write(a_minus_b_squared_extended[6:18])) # (a-b)^2 = (a-b)•(a-b)
            self.wait()
            self.play(Write(a_minus_b_squared_extended[18])) # (a-b)^2 = (a-b)•(a-b) =
            self.wait()

        def bacel_pakagcery(): # (a-b)^2 = (a-b)•(a-b) = a•a + a•(-b) + (-b)•a + (-b)•(-b)
            """
                Opens parenthesis of (a-b)(a-b)
                Writes this formula using ClockwiseTransform and ConnectionLine
                (a-b)^2 = (a-b)•(a-b) = a•a + a•(-b) + (-b)•a + (-b)•(-b)
            """
            conn_line = ConnectionLine(a_minus_b_squared_extended[8], a_minus_b_squared_extended[14])
            # a•a
            self.play(
                AnimationGroup(
                    Create(conn_line),
                    AnimationGroup(
                        ClockwiseTransform(a_minus_b_squared_extended[8].copy(), a_minus_b_squared_extended[19], remover=True),
                        ClockwiseTransform(a_minus_b_squared_extended[14].copy(), a_minus_b_squared_extended[21], remover=True),
                        Write(a_minus_b_squared_extended[20])
                    ),
                    lag_ratio=0.75
                )
            )
            self.add(a_minus_b_squared_extended[19:22])
            self.wait()

            # a•(-b)
            self.play(
                AnimationGroup(
                    Transform(conn_line, ConnectionLine(a_minus_b_squared_extended[8], a_minus_b_squared_extended[16])),
                    AnimationGroup(
                        ClockwiseTransform(a_minus_b_squared_extended[8].copy(), a_minus_b_squared_extended[23], remover=True),
                        ClockwiseTransform(a_minus_b_squared_extended[15:17].copy(), a_minus_b_squared_extended[26:28], remover=True),
                        Write(a_minus_b_squared_extended[22]),
                        Write(a_minus_b_squared_extended[24]),
                        Write(a_minus_b_squared_extended[25]),
                        Write(a_minus_b_squared_extended[28]),
                    ),
                    lag_ratio=0.75
                )
            )
            self.add(a_minus_b_squared_extended[22:29])
            self.wait()

            # (-b)•a
            self.play(
                AnimationGroup(
                    Transform(conn_line, ConnectionLine(a_minus_b_squared_extended[10], a_minus_b_squared_extended[14])),
                    AnimationGroup(
                        ClockwiseTransform(a_minus_b_squared_extended[9:11].copy(), a_minus_b_squared_extended[31:33], remover=True),
                        ClockwiseTransform(a_minus_b_squared_extended[14].copy(), a_minus_b_squared_extended[35], remover=True),
                        Write(a_minus_b_squared_extended[29]),
                        Write(a_minus_b_squared_extended[30]),
                        Write(a_minus_b_squared_extended[33]),
                        Write(a_minus_b_squared_extended[34]),
                    ),
                    lag_ratio=0.75
                )
            )
            self.add(a_minus_b_squared_extended[29:36])
            self.wait()

            # (-b)•(-b)
            self.play(
                AnimationGroup(
                    Transform(conn_line, ConnectionLine(a_minus_b_squared_extended[10], a_minus_b_squared_extended[16])),
                    AnimationGroup(
                        ClockwiseTransform(a_minus_b_squared_extended[9:11].copy(), a_minus_b_squared_extended[38:40], remover=True),
                        ClockwiseTransform(a_minus_b_squared_extended[15:17].copy(), a_minus_b_squared_extended[43:45], remover=True),
                        Write(a_minus_b_squared_extended[36]), # +
                        Write(a_minus_b_squared_extended[37]), # (
                        Write(a_minus_b_squared_extended[40]), # )
                        Write(a_minus_b_squared_extended[41]), # •
                        Write(a_minus_b_squared_extended[42]), # (
                        Write(a_minus_b_squared_extended[45]), # )
                    ),
                    lag_ratio=0.75
                )
            )
            self.add(a_minus_b_squared_extended[36:])
            self.wait(0.25)
            self.play(FadeOut(conn_line))
            self.wait()

        def berel_kataryal_tesqi(): # (a-b)^2 = (a-b)•(a-b) = a^2 - ab -ba + b^2
            """
                Writes the expression we got from bacel_pakagcery in the perfect form
                Writes the formula in final form - (a-b)^2 = a^2-2ab+b^2
            """
            # a•a  ->  a^2
            self.play(Indicate(a_minus_b_squared_extended[19:22], 1.5))
            self.wait(0.1)
            self.play(
                ModifyFormula(
                    a_minus_b_squared_extended,
                    replace_items=[[19, 20, 21]],
                    replace_items_strs=[['$a$', '$^2$']]
                )
            ) # ... = a^2 + a•(-b) + (-b)•a + (-b)•(-b)
            self.wait()

            # a•(-b)  ->  -ab
            self.play(Indicate(a_minus_b_squared_extended[22:28], 1.5))
            self.wait(0.1)
            self.play(
                ModifyFormula(
                    a_minus_b_squared_extended,
                    replace_items=[[22, 23, 24, 25, 26, 27]],
                    replace_items_strs=[['$($', '$-$', '$a$', '$b$', '$)$']]
                )
            ) # ... = a^2 + (-ab) + (-b)•a + (-b)•(-b)
            self.wait()

            self.play(Circumscribe(a_minus_b_squared_extended[19:27], fade_out=True, run_time=1.5))
            self.wait(0.5)
            self.wait(0.1)
            self.play(
                ModifyFormula(
                    a_minus_b_squared_extended,
                    remove_items=[21, 22, 26],
                )
            ) # ... = a^2 - ab + (-b)•a + (-b)•(-b)
            self.wait()

            # (-b)•a  ->  -ab
            self.play(Indicate(a_minus_b_squared_extended[25:31], 1.5))
            self.wait(0.1)
            self.play(
                ModifyFormula(
                    a_minus_b_squared_extended,
                    replace_items=[[24, 25, 26, 27, 28, 29, 30]],
                    replace_items_strs=[['$-$', '$a$', '$b$']]
                )
            ) # ... = a^2 - ab - ab + (-b)•(-b)
            self.wait()

            # (-b)•(-b)  ->  b^2
            self.play(Indicate(a_minus_b_squared_extended[28:], 1.5))
            self.wait(0.25)
            self.play(
                Wiggle(a_minus_b_squared_extended[29], 1.25, 0.02 * TAU),
                Wiggle(a_minus_b_squared_extended[34], 1.25, 0.02 * TAU)
            )
            self.wait(0.25)

            self.play(
                ModifyFormula(
                    a_minus_b_squared_extended,
                    remove_items=[29, 34],
                )
            ) # ... = a^2 - ab - ab + (b)•(b)
            self.wait()

            self.play(
                ModifyFormula(
                    a_minus_b_squared_extended,
                    replace_items=[[28, 29, 30, 31, 32, 33, 34]],
                    replace_items_strs=[['$b$', '$^2$']]
                )
            ) # ... = a^2 - ab - ab + b^2
            self.wait()

            self.play(
                AnimationGroup(
                    Indicate(a_minus_b_squared_extended[22:24], 1.5),
                    Indicate(a_minus_b_squared_extended[25:27], 1.5),
                    lag_ratio=0.5
                )
            )
            self.wait(0.5)
            self.play(
                ModifyFormula(
                    a_minus_b_squared_extended,
                    replace_items=[[22, 23, 24, 25, 26]],
                    replace_items_strs=[['$2$', '$a$', '$b$']]
                )
            ) # ... = a^2 - 2ab + b^2
            self.wait()

            # transform to final form of
            self.a_minus_b_squared.next_to(a_minus_b_squared_extended, DOWN, 0.75, LEFT)
            self.play(
                ReplacementTransform(a_minus_b_squared_extended[:7].copy(), self.a_minus_b_squared[:7]),
                ReplacementTransform(a_minus_b_squared_extended[19:].copy(), self.a_minus_b_squared[7:])
            )
            self.wait()


            self.play(
                AnimationGroup(
                    FadeOut(a_minus_b_squared_extended),
                    self.a_minus_b_squared.animate.move_to(ORIGIN).to_edge(LEFT),
                    lag_ratio=0.5
                )
            )
            self.wait()


        a_minus_b_squared_extended = self.a_minus_b_squared_extended
        a_minus_b_squared_extended.to_edge(LEFT)

        self.add(self.forty_nine_squared.to_corner(UL))

        write_beginning_of_formula() # (a-b)^2 = (a-b)•(a-b) =
        bacel_pakagcery() # (a-b)^2 = (a-b)•(a-b) = a•a + a•(-b) + (-b)•a + (-b)•(-b)
        berel_kataryal_tesqi() # (a-b)^2 = (a-b)•(a-b) = a^2 - 2ab + b^2

    def compare_with_square_of_sum(self):
        """
        Write formula for square of sum - (a+b)^2 = a^2+2ab+b^2
        Show difference in 2 formulas
        Move the formula for square of difference to UpRight corner
        """
        self.add(self.forty_nine_squared.to_corner(UL))
        self.add(self.a_minus_b_squared.move_to(ORIGIN).to_edge(LEFT))

        # read formula
        self.play(
            AnimationGroup(
                Circumscribe(self.a_minus_b_squared[1:4], Circle, fade_out=True, run_time=2),
                Circumscribe(self.a_minus_b_squared[5], Circle, fade_out=True),
                lag_ratio=0.5
            )
        ) # circumscribe a-b and ^2
        self.wait(0.5)
        self.play(Indicate(self.a_minus_b_squared[7:9], 1.5)) # a^2
        self.wait(0.25)
        self.play(Indicate(self.a_minus_b_squared[9], 1.5)) # -
        self.wait(0.25)
        self.play(Indicate(self.a_minus_b_squared[10:13], 1.5)) # 2ab
        self.wait(0.5)
        self.play(Indicate(self.a_minus_b_squared[14:], 1.5)) # b^2
        self.wait()

        # write formula of square of sum - (a+b)^2 = a^2 + 2ab + b^2
        self.play(
            AnimationGroup(
                self.a_minus_b_squared.animate.shift(UP * 0.5),
                Write(self.a_plus_b_squared.next_to(self.a_minus_b_squared, DOWN, 0.5, LEFT)),
                lag_ratio=0.5
            )
        )
        self.wait()

        # compare two formulas
        for formula in [self.a_plus_b_squared, self.a_minus_b_squared]:
            self.play(Circumscribe(formula[1:4], Circle, fade_out=True, run_time=2)) # a+b  /  a-b
            self.wait()
            self.play(Indicate(formula[9:13], 1.5)) # +2ab  /  -2ab
            self.wait()
        
        # move formula for square of difference to UpRight corner
        self.play(
            FadeOut(self.a_plus_b_squared),
            self.a_minus_b_squared.animate.move_to(self.surr_rect_a_minus_b_squared)
        )
        self.play(Create(self.surr_rect_a_minus_b_squared))
        self.wait()

    def calculate_forty_nine_squared(self):
        """
        Calculate 49^2 using formula for square of difference
        49^2 = (50-1)^2 = 50^2 - 2•50•1 + 1^2 = 2401
        Suggest viewer to calculate 51^2=(60-1)^2
        """
        # fix old things so this function can work independently from previous functions
        self.add(self.surr_rect_a_minus_b_squared)
        self.add(self.a_minus_b_squared.move_to(self.surr_rect_a_minus_b_squared))
        self.add(self.forty_nine_squared.to_corner(UL))

        # start 49^2
        self.wait()
        self.play(self.forty_nine_squared.animate.move_to(ORIGIN).to_edge(LEFT))
        self.wait()

        self.remove(self.forty_nine_squared)
        self.forty_nine_squared.remove(*self.forty_nine_squared)
        
        self.forty_nine_squared = exercise = Tex(
            '$49$', '$^2$', ' $=$ ', '$($', '$50$', '$-$', '$1$', '$)$', '$^2$', # 0:9
            ' $=$ ', '$50^2$', '$-$', '$2$$\cdot$$50$$\cdot$$1$', '$+$', '$1^2$', # 9:15
            ' $=$ ', '$2401$', # 15,16
            font_size=60
        ) # 49^2 = (50-1)^2 = 50^2 - 2•50•1 + 1^2 = 2401
        exercise.to_corner(LEFT)
        self.add(exercise[:9]) # 49^2 = (50-1)^2

        self.play(Write(exercise[9])) # =
        self.wait()
        self.play(Write(exercise[10])) # 50^2
        self.wait()
        self.play(Write(exercise[11], run_time=0.5)) # +
        self.wait()
        self.play(Write(exercise[12])) # 2•50•1
        self.wait()
        self.play(Write(exercise[13], run_time=0.5)) # +
        self.wait()
        self.play(Write(exercise[14])) # 1^2
        self.wait()

        calculations = Tex('$2500$', '$-100$', '$+1$', font_size=60) # 2500-100+1
        calculations.next_to(exercise[10:15], DOWN, 0.5)

        for calc in calculations:
            self.play(Write(calc))
            self.wait()
        
        self.play(Transform(calculations, Tex('$2401$', font_size=60).move_to(calculations)))
        self.wait()

        self.play(
            Write(exercise[15]),
            ReplacementTransform(calculations, exercise[16:])
        )
        self.wait()

        self.play(exercise.animate.shift(UP))
        self.wait()

        forty_nine_squared_old_method = Tex(
            '$49^2$', ' $=$ ', '$(40+9)^2$',
            ' $=$ ', '$40^2$', '$+$$2\cdot$$40$$\cdot$$9$', '$+ 9^2$',
            ' $=$ ', '$2401$',
            font_size=60
        ) # 49^2 = (40+9)^2 = 40^2 +2•40•9 + 9^2 = 2401
        forty_nine_squared_old_method.next_to(exercise, DOWN, 0.75, aligned_edge=LEFT)

        self.play(Write(forty_nine_squared_old_method, run_time=3))
        self.wait()

        fifty_one_squared_new_method = Tex('$51^2 = (60-9)^2$', font_size=60)
        fifty_one_squared_new_method.next_to(forty_nine_squared_old_method, DOWN, 0.75, aligned_edge=LEFT)

        self.play(Write(fifty_one_squared_new_method, run_time=2))
        self.wait()

        self.play(FadeOut(forty_nine_squared_old_method, fifty_one_squared_new_method))
        self.wait()
        self.remove(self.forty_nine_squared)

    def animate_b_minus_a_squared(self):
        """
        Open parenthesis in (b-a)^2 by using the formula
        Notice that it's equal to (a-b)^2 
        Explain equality (b-a) = -(a-b)
        """
        # add items form previous functions,
        # so this function can work independently from previous functions
        self.forty_nine_squared = Tex(
            '$49$', '$^2$', ' $=$ ', '$($', '$50$', '$-$', '$1$', '$)$', '$^2$', # 0:9
            ' $=$ ', '$50^2$', '$-$', '$2$$\cdot$$50$$\cdot$$1$', '$+$', '$1^2$', # 9:15
            ' $=$ ', '$2401$', # 15,16
            font_size=60
        ) # 49^2 = (50-1)^2 = 50^2 - 2•50•1 + 1^2 = 2401
        self.forty_nine_squared.to_edge(LEFT).shift(UP)
        self.add(self.forty_nine_squared)

        self.add(self.surr_rect_a_minus_b_squared)
        self.add(self.a_minus_b_squared.move_to(self.surr_rect_a_minus_b_squared))

        # start (b-a)^2
        exercise = self.b_minus_a_squared # (b-a)^2 = b^2 - 2ba + a^2
        exercise.next_to(self.forty_nine_squared, DOWN, 0.75, aligned_edge=LEFT)

        self.play(Write(exercise[:6])) # (b-a)^2
        self.wait()
        self.play(Write(exercise[6])) # (b-a)^2 =
        self.wait(0.5)
        self.play(Write(exercise[7])) # (b-a)^2 = b^2
        self.wait(0.25)
        self.play(Write(exercise[8], run_time=0.5)) # (b-a)^2 = b^2 -
        self.wait(0.25)
        self.play(Write(exercise[9:12])) # (b-a)^2 = b^2 - 2ba
        self.wait(0.25)
        self.play(Write(exercise[12], run_time=0.5)) # (b-a)^2 = b^2 - 2ba +
        self.wait(0.25)
        self.play(Write(exercise[13])) # (b-a)^2 = b^2 - 2ba + a^2
        self.wait()

        self.play(Indicate(exercise[9:12], 1.5))
        self.wait()
        self.rearrange_formula(
            exercise, [*range(10), 11, 10, 12, 13], [10], [11]
        ) # (b-a)^2 = b^2 - 2ab + a^2
        self.wait()
        self.rearrange_formula(
            exercise, [*range(7), 13, 8, 9, 10, 11, 12, 7], [7], [13]
        ) # (b-a)^2 = a^2 - 2ab + b^2
        self.wait()

        formula_copy = self.a_minus_b_squared.copy()
        self.play(Indicate(self.a_minus_b_squared, 1.5))
        self.wait(0.5)
        self.play(formula_copy.animate.next_to(exercise, DOWN, buff=0.5, aligned_edge=LEFT))
        self.wait()

        dividing_line = DashedLine().scale(1.25).rotate(-PI/2).shift(DOWN)
        self.play(Create(dividing_line))
        self.wait()

        # show that (b-a)=-(a-b)
        show_equality = Tex(
            '$b$', '$-$', '$a$', ' $=$ ', '$-$', '$($', '$a$', '$-$', '$b$', '$)$',
            font_size=60
        ) # b-a = -(a-b)
        show_equality.move_to(exercise).shift(7.5 * RIGHT)

        self.play(Indicate(exercise[1:4], 1.5))
        self.wait(0.1)
        self.play(Indicate(formula_copy[1:4], 1.5))
        self.wait()
        self.play(Write(show_equality[:3]))
        self.wait(0.25)
        self.play(Write(show_equality[3]))
        self.wait(0.25)
        self.play(Write(show_equality[4:]))
        self.wait()

        self.fix_formula(show_equality)
        self.play(
            ModifyFormula(
                show_equality,
                add_after_items=[-1, 2, 3, 9],
                add_items_strs=[['$($'], ['$)$', '$^2$'], ['$($'], ['$)$', '$^2$']],
                new_formula_alignment=DOWN
            )
        ) # (b-a)^2 = (-(a-b))^2
        self.wait()
        self.play(
            ModifyFormula(
                show_equality,
                remove_items=[8, 9, 13]
            )
        ) # (b-a)^2 = (a-b)^2
        self.wait()

        # show an example of opposite number have same square   5^2 = (-5)^2
        five_squared = Tex(
            '$5^2$', ' $=$ ', '$(-5)^2$', ' $=$ ', '$25$',
            font_size=60
        ) # 5^2 = (-5)^2
        five_squared.next_to(show_equality, DOWN, buff=0.75)

        self.play(
            AnimationGroup(
                Write(five_squared[0]),
                Write(five_squared[2]),
                lag_ratio=0.75
            )
        )
        self.wait(0.5)
        self.play(Write(five_squared[1]))
        self.wait()
        self.play(Write(five_squared[3:]))
        self.wait()

        self.play(FadeOut(five_squared, dividing_line, show_equality, formula_copy))
        self.wait()
        self.remove(self.forty_nine_squared)

    def exercise_x_minus_3_squared(self):
        """
        Solve exercise (x-3)^2
        Just write = x^2-2•x•3+3^2 and transforms to x^2-6x+9
        """
        # add items form previous functions,
        # so this function can work independently from previous functions
        self.forty_nine_squared = Tex(
            '$49$', '$^2$', ' $=$ ', '$($', '$50$', '$-$', '$1$', '$)$', '$^2$', # 0:9
            ' $=$ ', '$50^2$', '$-$', '$2$$\cdot$$50\cdot$$1$', '$+$', '$1^2$', # 9:15
            ' $=$ ', '$2401$', # 15,16
            font_size=60
        ) # 49^2 = (50-1)^2 = 50^2 - 2•50•1 + 1^2 = 2401
        self.forty_nine_squared.to_edge(LEFT).shift(UP)
        self.add(self.forty_nine_squared)

        self.add(self.surr_rect_a_minus_b_squared)
        self.add(self.a_minus_b_squared.move_to(self.surr_rect_a_minus_b_squared))

        self.b_minus_a_squared.next_to(self.forty_nine_squared, DOWN, 0.75, aligned_edge=LEFT)
        self.add(self.b_minus_a_squared)

        # start (x-3)^2
        x_minus_3_squared = Tex(
            '$(x-3)^2$', ' $=$ ', '$x^2$', '$-$', '$2$$\cdot$$x$$\cdot$$3$', '$+$', '$3^2$',
            font_size=60
        ) # (x-3)^2 = x^2-2•x•3+3^2
        x_minus_3_squared.next_to(self.b_minus_a_squared, DOWN, 0.75, LEFT)

        for tex in x_minus_3_squared:
            self.play(Write(tex))
            self.wait(0.5)

        self.play(
            ModifyFormula(
                x_minus_3_squared,
                replace_items=[[4]],
                replace_items_strs=[['$6x$']]
            )
        ) # (x-3)^2 = x^2-6x+3^2
        self.wait()
        self.play(
            ModifyFormula(
                x_minus_3_squared,
                replace_items=[[6]],
                replace_items_strs=[['$9$']]
            )
        ) # (x-3)^2 = x^2-6x+9
        self.wait()

        self.play(
            FadeOut(
                self.forty_nine_squared,
                self.b_minus_a_squared,
                x_minus_3_squared
            )
        )
        self.wait()

    def last_exercise(self):
        """
        Last exercise for the viewer
        (2-z)^2
        """
        # add formula
        self.add(self.surr_rect_a_minus_b_squared)
        self.add(self.a_minus_b_squared.move_to(self.surr_rect_a_minus_b_squared))

        # write exercise
        exercise = Tex('$(2-z)^2=$', font_size=60)
        exercise.to_edge(LEFT)

        self.play(Write(exercise, run_time=2))
        self.wait()
