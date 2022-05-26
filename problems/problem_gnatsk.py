from manim import *
from aramanim import *

LOKOMOTIV = SVGMobject('mardatar.svg')

MARDATAR = SVGMobject('mardatar_vagon.svg').scale_to_fit_height(
    LOKOMOTIV.get_edge_center(UP)[1] - LOKOMOTIV.get_edge_center(DOWN)[1]
)
BERNATAR = SVGMobject('bernatar_vagon.svg').scale_to_fit_height(
    LOKOMOTIV.get_edge_center(UP)[1] - LOKOMOTIV.get_edge_center(DOWN)[1]
)

N_MARDATAR = 7
N_BERNATAR = 20
L_MARDATAR = 11
L_BERNATAR = 7

INDEX_LIST_ODD = [1, 3, 5, 7, 9, 11, 13]

BUUF_BETWEEN_PLAYERS = 1.5
UNIT_SEGMENT_LENGTH = 0.5
VALUE_TO_SEGMENT_LENGTH = 1/5
SCALE_DEMERGER = 1


DEFAULT_LABEL_STROKE_WIDTH = 6

COLOR_PALETTE = ['#fa8f6e', '#d4c24e', '#5ff196']


class Gnatsk(Scene):
    def construct(self):
        
        bernatar_group = VGroup(
            *[BERNATAR.copy() for _ in range(N_BERNATAR)]
        ).scale(0.5).arrange(RIGHT, buff=0.1)
        
        mardatar_group = VGroup(
            *[MARDATAR.copy() for _ in range(N_MARDATAR)]
        ).scale(0.5).arrange(RIGHT, buff=0.1)
        lokomotiv_group = VGroup(LOKOMOTIV).scale(0.5)
        
        gnatsk_group = VGroup(
            bernatar_group,
            mardatar_group,
            lokomotiv_group
        ).arrange(RIGHT, buff=0.1)
        
        start = gnatsk_group.get_edge_center(LEFT)
        end = gnatsk_group.get_edge_center(RIGHT)
        self.play(
            gnatsk_group.move_to(start).shift(7.5*LEFT+3*DOWN).animate.move_to(end).shift(6.5*LEFT+3*DOWN),
            run_time=5
        )
        start = gnatsk_group.get_edge_center(LEFT)
        bottom = gnatsk_group.get_edge_center(DOWN)
        self.wait(0.5)
        self.play(gnatsk_group.animate.scale_to_fit_width(13).align_to(start, LEFT).align_to(bottom, DOWN))
        self.wait(0.2)

        ### player_1 ### 
        player_1 = VGroup(*[self.unit_segment() for _ in range(N_BERNATAR)]).arrange(RIGHT, buff=0)
        name_1 = Tex(r'Բեռնատար', font_size=DEFAULT_LABEL_FONT_SIZE, tex_template=ARMTEX).set_color(COLOR_PALETTE[0])
        ### player_2 ### 
        player_2_list = []
        for _ in range(N_MARDATAR):
            player_2_list += self.unit_segment_with_additional(L_MARDATAR-L_BERNATAR)
        player_2 = VGroup(*player_2_list).arrange(RIGHT, buff=0)
        name_2 = Tex(r'Մարդատար', font_size=DEFAULT_LABEL_FONT_SIZE, tex_template=ARMTEX).set_color(COLOR_PALETTE[1])

        ## diagram ##
        diagram = VGroup(player_1, player_2).arrange(DOWN, buff=BUUF_BETWEEN_PLAYERS, aligned_edge=LEFT).shift(2*UP +0.5*RIGHT)
        name_1.next_to(player_1, LEFT, buff=0.35)
        name_2.next_to(player_2, LEFT, buff=0.35)
        total_brace = Brace(diagram, RIGHT)
        total_text = DecimalNumber(217, 0, font_size=DEFAULT_FONT_SIZE).next_to(total_brace, RIGHT)

        segment_1 = self.from_player_segment(player_1)
        segment_2 = self.from_player_segment(player_2)
        semi_segment_2 = VGroup(
            *[self.from_player_segment(
                VGroup(player_2_list[2*i], player_2_list[2*i + 1])
            ) for i in range(N_MARDATAR)]
        )

        self.play(Write(name_1))
        self.play(self.items_to_segment(bernatar_group, segment_1))
        self.play(Write(name_2))
        self.play(self.items_to_segment(mardatar_group, segment_2), FadeOut(lokomotiv_group))
        self.play(Write(total_text), Write(total_brace))

        
        count_1 = MathTex(*[r"{:,}".format(int(i+1)) for i in range(N_BERNATAR)]).scale(0.6)
        [count_1[s].next_to(player_1[s], DOWN, buff = 0) for s in range(len(player_1))]

        count_2 = MathTex(*[r"{:,}".format(int(i+1)) for i in range(N_MARDATAR)]).scale(0.6)
        [count_2[s].next_to(semi_segment_2[s], DOWN, buff = 0) for s in range(N_MARDATAR)]

        self.play(self.fade_in_out(player_1, segment_1))
        self.play(Write(count_1))
        self.wait()
        self.play(FadeOut(count_1))
        self.play(self.fade_in_out(semi_segment_2, segment_2))
        self.play(Write(count_2))
        self.wait()
        self.play(FadeOut(count_2))

        player_1_0_target = player_1[0].copy()
        self.play(player_1_0_target.animate.align_to(player_2[0], DOWN + LEFT))
        self.play(FadeIn(player_2[1]))
        self.remove(semi_segment_2[0])
        self.play(Write(player_2[1].update_label_pos()))
        self.play(self.fade_in_out(player_2[2:], semi_segment_2[1:]))
        self.play(AnimationGroup(
                *[Write(player_2[i].update_label_pos()) for i in INDEX_LIST_ODD[1:]], lag_ratio=0.6
            )
        )
        self.wait()
        
        scis_1 = Scissors(player_2[0].get_edge_center(RIGHT))
        scis_2 = Scissors(player_2[2].get_edge_center(RIGHT))
        scis_3 = Scissors(player_2[4].get_edge_center(RIGHT))
        scis_4 = Scissors(player_2[6].get_edge_center(RIGHT))
        scis_5 = Scissors(player_2[8].get_edge_center(RIGHT))
        scis_6 = Scissors(player_2[10].get_edge_center(RIGHT))
        scis_7 = Scissors(player_2[12].get_edge_center(RIGHT))

        group_for_cut = VGroup(*[player_2[i] for i in INDEX_LIST_ODD])

        self.play(AnimationGroup(
            CutIn(scis_1),
            CutIn(scis_2),
            CutIn(scis_3),
            CutIn(scis_4),
            CutIn(scis_5),
            CutIn(scis_6),
            CutIn(scis_7),
            lag_ratio=0.05
        ))
        self.add(
            scis_1,
            scis_2,
            scis_3,
            scis_4,
            scis_5,
            scis_6,
            scis_7,
        )
        self.play(
            group_for_cut.animate.shift(0.35*UP),
            AnimationGroup(
                CutOut(scis_1),
                CutOut(scis_2),
                CutOut(scis_3),
                CutOut(scis_4),
                CutOut(scis_5),
                CutOut(scis_6),
                CutOut(scis_7),
                lag_ratio=0.05
            )
        )
        self.wait(2)

        formula_1 = MathTex(
            r'4', r'+',
            r'4', r'+',
            r'4', r'+',
            r'4', r'+',
            r'4', r'+',
            r'4', r'+',
            r'4', r'=',
            r'28', font_size=DEFAULT_FONT_SIZE
        ).align_to(player_1, LEFT)

        animation_list = []
        for i in range(7):
            animation_list += [ReplacementTransform(player_2[2*i+1].label.copy(), formula_1[2*i]), Write(formula_1[2*i+1])]
        self.play(AnimationGroup(*animation_list, Write(formula_1[-1:]), lag_ratio=0.5), run_time = 5)

        formula_2 = MathTex(r'217', r'-', r'28', r'=', r'189', font_size=DEFAULT_FONT_SIZE).next_to(formula_1, DOWN, aligned_edge=LEFT)

        animation_list=[ReplacementTransform(total_text.copy(), formula_2[0]), FadeOut(total_text), Write(formula_2[1])]
        animation_list += [ReplacementTransform(formula_1[-1].copy(), formula_2[2]), Write(formula_2[3:])]

        rectangle = VGroup(
                self.rectangle_surround(group_for_cut, BLACK).set_fill(BLACK, 0.5).set_stroke(BLACK, DEFAULT_LABEL_STROKE_WIDTH, opacity=0.7)
            ).set_opacity(0)
        self.play(AnimationGroup(*animation_list, lag_ratio=0.75), *[s.label.animate.set_opacity(0.30) for s in group_for_cut], rectangle.animate.set_opacity(0.70))
        total_text.set_value(189)
        self.play(ReplacementTransform(formula_2[-1].copy(), total_text))

        self.wait(2)
        count_2.become(MathTex(*[r"{:,}".format(int(i+21)) for i in range(N_MARDATAR)]).scale(0.6))
        [count_2[s].next_to(player_2[2*s], DOWN, buff = 0) for s in range(N_MARDATAR)]
        
        self.play(Write(count_1))
        self.play(Write(count_2))

        self.play(Flash(count_2[-1]), FadeOut(count_1))
        

        formula_3 = MathTex(r'189', r':', r'27', r'=', r'7', font_size=DEFAULT_FONT_SIZE).next_to(formula_2, DOWN, aligned_edge=LEFT)
        self.play(FadeOut(count_2), Write(formula_3))

        self.play(rectangle.animate.set_opacity(0), *[s.label.animate.set_opacity(1) for s in group_for_cut], FadeOut(total_text))
        total_text.set_value(217)
        self.play(group_for_cut.animate.align_to(player_2, DOWN), FadeIn(total_text))
        
        formula_4 = MathTex(r'7', r'+', r'4', r'=', r'11', font_size=DEFAULT_FONT_SIZE).next_to(formula_3, DOWN, aligned_edge=LEFT)
        self.play(Write(formula_4))
        self.wait()
        


    def unit_segment(self):
        return Segment(ORIGIN, UNIT_SEGMENT_LENGTH*RIGHT, r'7', DEFAULT_LABEL_FONT_SIZE, stroke_width=DEFAULT_LABEL_STROKE_WIDTH, color=COLOR_PALETTE[0])
    
    def unit_segment_with_additional(self, additional):
        label_text="{:,}".format(int(additional))
        s=Segment(ORIGIN, VALUE_TO_SEGMENT_LENGTH*SCALE_DEMERGER*additional*RIGHT, label_text, DEFAULT_LABEL_FONT_SIZE, stroke_width=DEFAULT_LABEL_STROKE_WIDTH, color=COLOR_PALETTE[1])
        s.label.add_updater(lambda mob: s.update_label_pos())
        return [self.unit_segment(), s]

    def from_player_segment(self, player):
        return Segment(
            player.get_edge_center(LEFT),
            player.get_edge_center(RIGHT),
            color=GREEN_A, stroke_width=DEFAULT_LABEL_STROKE_WIDTH
        )
    
    def items_to_segment(self, items, segment):
        return ReplacementTransform(VGroup(items[0], items[-1], items[1:-1],), segment)

    def fade_in_out(self, mob_in, mob_out):
        return AnimationGroup(FadeIn(mob_in, run_time=0.8), FadeOut(mob_out))

    def rectangle_surround(self, mob: VMobject, color=PINK):
        x = mob.get_edge_center(RIGHT)[0]-mob.get_edge_center(LEFT)[0]
        y = mob.get_edge_center(UP)[1]-mob.get_edge_center(DOWN)[1]
        rectangle=Rectangle(color, stroke_width=DEFAULT_LABEL_STROKE_WIDTH)
        rectangle.stretch_to_fit_height(1.5*y)
        rectangle.stretch_to_fit_width(x)
        return rectangle.move_to(mob.get_center())