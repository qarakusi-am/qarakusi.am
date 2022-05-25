from random import uniform
from manim import *
from aramanim import *

TOTAL=92
MULTIPLICATION=1
INDEX_LIST_ODD=[1, 3, 5, 7]
INDEX_LIST_EVEN=[0, 2, 4, 6]
BUUF_BETWEEN_PLAYERS=1
SCALE_DEMERGER=1.85

N_PLAYER_1=22
N_PLAYER_2=13
N_PLAYER_3=57

TIMES=4

COLOR_PALETTE=['#fa8f6e', '#d4c24e', '#5ff196']

UNIT_SEGMENT_LENGTH=1.35
SEGMENT_LENGTH_TO_VALUE=11/UNIT_SEGMENT_LENGTH
VALUE_TO_SEGMENT_LENGTH=UNIT_SEGMENT_LENGTH/11

DEFAULT_LABEL_STROKE_WIDTH=6
DEFAULT_LABEL_FONT_SIZE=50
RUN_TIME = 2

FOREST_LEFT_X=-5.5
FOREST_RIGHT_X=5.5
FOREST_UP_Y=-2.5
FOREST_DOWN_Y=-3.5


class Antar(Scene):
    def construct(self):
        ### player_1 ### 
        self.player_1 = player_1 = VGroup(*[self.unit_segment() for _ in range(2)]).arrange(RIGHT, buff=0)
        name_1 = Tex(r'Հացենիներ', font_size=DEFAULT_LABEL_FONT_SIZE, tex_template=ARMTEX).set_color(COLOR_PALETTE[0])
        ### player_2 ### 
        self.player_2 = player_2 = VGroup(*[s for s in self.unit_segment_with_additional(2)]).arrange(RIGHT, buff=0)
        name_2 = Tex(r'Թխկիներ', font_size=DEFAULT_LABEL_FONT_SIZE, tex_template=ARMTEX).set_color(COLOR_PALETTE[1])
        ### player_3 ### 
        player_3_list = []
        for _ in range(TIMES):
            player_3_list += self.unit_segment_with_additional(2)
            if _ == TIMES-1:
                player_3_list += [Segment(ORIGIN, VALUE_TO_SEGMENT_LENGTH*SCALE_DEMERGER*5*RIGHT, '5', DEFAULT_LABEL_FONT_SIZE, stroke_width=DEFAULT_LABEL_STROKE_WIDTH, color=RED)]
        self.player_3 = player_3 = VGroup(*player_3_list).arrange(RIGHT, buff=0)
        name_3 = Tex(r'Կաղնիներ', font_size=DEFAULT_LABEL_FONT_SIZE, tex_template=ARMTEX).set_color(COLOR_PALETTE[2])
        ###          ###
        diagram=VGroup(player_1, player_2, player_3).arrange(DOWN, buff=BUUF_BETWEEN_PLAYERS, aligned_edge=LEFT).shift(2*UP+0.75*RIGHT)
        
        ### forest ### 
        forest = VGroup(*[self.get_tree().move_to([uniform(FOREST_LEFT_X, FOREST_RIGHT_X), uniform(FOREST_DOWN_Y, FOREST_UP_Y), 0]) for _ in range(MULTIPLICATION*TOTAL)])
        forest_1 = forest[0:MULTIPLICATION*N_PLAYER_1].set_color(COLOR_PALETTE[0]).set_opacity(0.8).set_stroke(BLACK)
        forest_2 = forest[MULTIPLICATION*N_PLAYER_1:MULTIPLICATION*(N_PLAYER_1+N_PLAYER_2)].set_color(COLOR_PALETTE[1]).set_opacity(0.8).set_stroke(BLACK)
        forest_3 = forest[MULTIPLICATION*(N_PLAYER_1+N_PLAYER_2):MULTIPLICATION*(N_PLAYER_1+N_PLAYER_2+N_PLAYER_3)].set_color(COLOR_PALETTE[2]).set_opacity(0.8).set_stroke(BLACK)       
        ###        ###

        ### segment_1 ###
        self.segment_1 = segment_1=self.from_player_segment(player_1)
        self.segment_2 = segment_2=self.from_player_segment(player_2)
        self.segment_3 = segment_3=self.from_player_segment(player_3)
        name_1.next_to(segment_1, LEFT, buff=0.35)
        name_2.next_to(segment_2, LEFT, buff=0.35)
        name_3.next_to(segment_3, LEFT, buff=0.35)
        ###           ###
        text_1 = Tex(r'\textrm{— ծածկում են որոշակի տարածք}', font_size=DEFAULT_LABEL_FONT_SIZE, tex_template=ARMTEX).next_to(name_1, RIGHT, buff=0.25).align_to(segment_1, LEFT).set_color([COLOR_PALETTE[1], COLOR_PALETTE[0]])
        text_2 = Tex(r'\textrm{— հացենիների կեսից }', r'$2$', r'\textrm{ հա-ով ավելի}', font_size=DEFAULT_LABEL_FONT_SIZE, tex_template=ARMTEX).next_to(name_2, LEFT, buff=0.5).align_to(text_1, LEFT).set_color([COLOR_PALETTE[2], COLOR_PALETTE[1]])
        text_3 = Tex(r'\textrm{— թխկիների քառապատիկից }', r'$5$', r'\textrm{ հա-ով ավելի}', font_size=DEFAULT_LABEL_FONT_SIZE, tex_template=ARMTEX).next_to(name_3, LEFT, buff=0.5).align_to(text_1, LEFT).set_color([COLOR_PALETTE[0], COLOR_PALETTE[2]])
        text_4 = Tex(r'\textrm{Ընդամենը }', r'—  $92$ \textrm{ հա}', font_size=DEFAULT_LABEL_FONT_SIZE, tex_template=ARMTEX).next_to(text_3, DOWN, buff=0.75*BUUF_BETWEEN_PLAYERS, aligned_edge=LEFT).set_color([COLOR_PALETTE[0], COLOR_PALETTE[1]])
        text_4[0].align_to(name_3, RIGHT)
        text_4[1].align_to(text_1, LEFT)
        ### forest animation ###
        self.wait(0.15)
        self.play(
            Write(name_1),
            Write(name_2),
            Write(name_3),
        )
        self.wait()
        self.play(Write(text_1), run_time=RUN_TIME)
        self.wait(2)
        self.play(Write(text_2), run_time=RUN_TIME)
        self.wait(2)
        self.play(Write(text_3), run_time=RUN_TIME)
        self.wait(2)
        self.play(Write(text_4), run_time=RUN_TIME)
        self.wait(2)
        self.add(forest_3, forest_2, forest_1 )
        self.wait(2)
        self.play(FadeOut(text_1))
        self.trees_in_rows(segment_1, forest_1)
        self.wait(2)
        self.play(text_2.animate.shift(0.45*DOWN))
        self.trees_in_rows(segment_2, forest_2)
        
        self.play(forest_2[-MULTIPLICATION*2:].animate(rate_func=rate_functions.there_and_back_with_pause).shift(RIGHT), run_time=RUN_TIME)
        
        self.wait(2)
        self.play(
            self.items_to_segment(forest_1, segment_1),
            run_time=RUN_TIME
        )
        ### # # # # # # # # # ###
        self.wait(2)

        ### diagram animation ###
        ### player_1 animation ###
        self.play(
            self.fade_in_out(player_1, segment_1),
            run_time=RUN_TIME    
        )
        self.wait(2)
        ### player_2 animation ###

        self.play(
            AnimationGroup(
                self.items_to_segment(forest_2[0:-MULTIPLICATION*2-1], player_2[0]),
                self.items_to_segment(forest_2[-MULTIPLICATION*2-1:], player_2[1]),
                ReplacementTransform(text_2[1].copy(), player_2[1].update_label_pos()), lag_ratio=0.6
            ), FadeOut(text_2),
            run_time=2*RUN_TIME
        )
        self.play(text_3.animate.shift(0.45*DOWN))
        self.trees_in_rows(segment_3, forest_3)
        self.wait(2)
        ### player_3 animation ###
        
        self.play(FadeOut(forest_3[:-MULTIPLICATION*7]))
        player_3_1_t = player_2.copy()
        segment_2x4_target = self.x4_plus_5()
        
        self.play(
            self.fade_in_out(player_3[-1], forest_3[-MULTIPLICATION*7:]),
            run_time=RUN_TIME
        )
        player_3[-1].label.add_updater(lambda mob: player_3[-1].update_label_pos())
        self.play(ReplacementTransform(text_3[1].copy(), player_3[-1].update_label_pos()), FadeOut(text_3))
        self.wait()

        ### brace with animation ###
        total_brace = Brace(diagram, RIGHT)
        total_text = DecimalNumber(92, 0, font_size=DEFAULT_FONT_SIZE).next_to(total_brace, RIGHT)
        total_brace

        self.play(Write(total_brace), Write(total_text), FadeOut(text_4), run_time=RUN_TIME)
        self.wait(2)

        ### comparison of parts ###
        rectangle_3=self.rectangle_surround(segment_2x4_target[0], RED)
        rectangle_2=self.rectangle_surround(player_2[0])
        rectangle_1=self.rectangle_surround(player_1[0])
        self.wait(2)
        self.play(
            Create(rectangle_3),
            run_time=RUN_TIME
        )
        self.wait(0.5)
        self.play(
            Create(rectangle_2),
            Create(rectangle_1),
            run_time=RUN_TIME
        )
        self.wait(0.5)
        self.play(
            Uncreate(rectangle_2),
            Uncreate(rectangle_1),
            run_time=RUN_TIME
        )
        self.wait(0.5)
        self.play(
            Uncreate(rectangle_3),
            run_time=RUN_TIME
        )
        self.wait(2)
        ### player_3  animation ###
        self.play(AnimationGroup(*[s.animate(rate_func=rate_functions.there_and_back).shift(0.25*UP) for s in segment_2x4_target], lag_ratio=0.4), run_time=RUN_TIME)
        self.wait(2)
        self.play(player_3_1_t.animate.align_to(player_3, DOWN+LEFT))
        self.remove(segment_2x4_target[0])
        self.play(
            self.fade_in_out(player_3[0:-1], segment_2x4_target[1:]),
            run_time=RUN_TIME
        )
        self.remove(player_3_1_t)
        rectangle_3.become(self.rectangle_surround(player_3[0], PINK))
        self.play(FadeIn(rectangle_3))
        self.play(FadeOut(rectangle_3))
        self.wait(2)
        self.play(AnimationGroup(*[Write(player_3[i].update_label_pos()) for i in INDEX_LIST_ODD], lag_ratio=0.5), run_time=RUN_TIME)
        self.wait(2)
        self.play(
            AnimationGroup(
                *[s.animate(rate_func=rate_functions.there_and_back_with_pause).set_color(PINK) for s in player_3],
                lag_ratio=9.5, run_time=RUN_TIME
            ), run_time=2.5*RUN_TIME
        )

        scis_1 = Scissors(player_2[0].get_edge_center(RIGHT))
        scis_2 = Scissors(player_3[0].get_edge_center(RIGHT))
        scis_3 = Scissors(player_3[2].get_edge_center(RIGHT))
        scis_4 = Scissors(player_3[4].get_edge_center(RIGHT))
        scis_5 = Scissors(player_3[6].get_edge_center(RIGHT))


        group_for_cut = VGroup(player_2[-1], *[player_3[i] for i in INDEX_LIST_ODD], player_3[-1])
        group_for_count = VGroup(
            player_1[0], player_1[1],
            player_2[0],
            player_3[0], player_3[2], player_3[4], player_3[6],
        )
        self.play(AnimationGroup(
            CutIn(scis_1),
            CutIn(scis_2),
            CutIn(scis_3),
            CutIn(scis_4),
            CutIn(scis_5),
            lag_ratio=0.05
        ), run_time=RUN_TIME)
        self.add(
            scis_1,
            scis_2,
            scis_3,
            scis_4,
            scis_5,
        )
        self.play(
            group_for_cut.animate.shift(0.35*UP),
            AnimationGroup(
                CutOut(scis_1),
                CutOut(scis_2),
                CutOut(scis_3),
                CutOut(scis_4),
                CutOut(scis_5),
                lag_ratio=0.05
            ), run_time=RUN_TIME
        )
        self.wait(2)


        formula_1 = MathTex(r'2', r'+', r'2', r'+', r'2', r'+', r'2', r'+', r'2', r'+', r'5', r'=', r'15', font_size=DEFAULT_FONT_SIZE).align_to(player_1, LEFT)
        animation_list=[]
        
        for i in range(6):
            if i == 0:
                animation_list += [ReplacementTransform(player_2[-1].label.copy(), formula_1[0]), Write(formula_1[1])]
            elif i !=5:
                animation_list +=[ReplacementTransform(player_3[2*i-1].label.copy(), formula_1[2*i]), Write(formula_1[2*i+1])]
            else:
                animation_list +=[ReplacementTransform(player_3[-1].label.copy(), formula_1[2*i]), Write(formula_1[2*i+1:])]

        self.play(AnimationGroup(*animation_list, lag_ratio=0.75), run_time=2.5*RUN_TIME)
        self.wait(2)
        formula_2 = MathTex(r'92', r'-', r'15', r'=', r'77', font_size=DEFAULT_FONT_SIZE).next_to(formula_1, DOWN, aligned_edge=LEFT)
        animation_list=[ReplacementTransform(total_text.copy(), formula_2[0]), FadeOut(total_text), Write(formula_2[1])]
        animation_list += [ReplacementTransform(formula_1[-1].copy(), formula_2[2]), Write(formula_2[3:])]

        rectangles = VGroup(*[self.rectangle_surround(s, BLACK).set_fill(BLACK, 0.5).set_stroke(BLACK, DEFAULT_LABEL_STROKE_WIDTH, opacity=0.9) for s in group_for_cut]).set_opacity(0)
        self.play(AnimationGroup(*animation_list, lag_ratio=0.75), *[s.label.animate.set_opacity(0.20) for s in group_for_cut], rectangles.animate.set_opacity(0.80), run_time=1.5*RUN_TIME)
        total_text.set_value(77)
        self.play(ReplacementTransform(formula_2[-1].copy(), total_text))

        self.wait(2)
        formula_3 = MathTex(r'77', r':', r'7', r'=', r'11', font_size=DEFAULT_FONT_SIZE).next_to(formula_2, DOWN, aligned_edge=LEFT)
        self.play(AnimationGroup(*[s.animate(rate_func = rate_functions.there_and_back).shift(0.25*UP) for s in group_for_count], lag_ratio=0.5), run_time=1.5*RUN_TIME)
        self.play(Write(formula_3), run_time=RUN_TIME)
        self.wait(2)
        self.play(AnimationGroup(*[Write(s.update_label_pos()) for s in group_for_count], lag_ratio=0.5), run_time=1.5*RUN_TIME)
        self.wait(2)
        formula_p_1 = MathTex(r'11', r'+', r'11', r'=', r'22', font_size=DEFAULT_FONT_SIZE).next_to(formula_3, DOWN, aligned_edge=LEFT)
        formula_p_2 = MathTex(r'11', r'+', r'2', r'=', r'13', font_size=DEFAULT_FONT_SIZE).next_to(formula_p_1, DOWN, aligned_edge=LEFT)
        formula_p_3_0 = MathTex(
            r'+', r'+',
            r'+', r'+',
            r'+', r'+',
            r'+', r'+', font_size=DEFAULT_FONT_SIZE).next_to(formula_p_2, DOWN, aligned_edge=LEFT)
        labels = VGroup(*[player_3[i].update_label_pos() for i in range(len(player_3)-1)])
        [formula_p_3_0[p].next_to(labels[p], RIGHT, buff=0.15) for p in range(len(formula_p_3_0))]
        VGroup(*[formula_p_3_0[i] for i in INDEX_LIST_ODD]).align_to(formula_p_3_0, DOWN)
        formula_p_3_1 = MathTex(r'92', r'-', r'13', r'-', r'22', r'=', r'57', font_size=DEFAULT_FONT_SIZE).next_to(formula_p_2, DOWN, aligned_edge=LEFT)
        formula_p_3_2 = MathTex(r'4', r'\cdot', r'13', r'+', r'5', r'=', r'57', font_size=DEFAULT_FONT_SIZE).next_to(formula_p_3_1, RIGHT, buff=1)
        [s.label.set_opacity(1) for s in group_for_cut]
        self.remove(rectangles)
        self.play(group_for_cut.animate.shift(0.35*DOWN))
        
        total_text.set_value(92)
        self.play(Write(formula_p_1), run_time=RUN_TIME)
        self.wait(2)
        self.integrate(player_1, segment_1, r'22')
        self.wait(2)        
        self.play(Write(formula_p_2), run_time=RUN_TIME)
        self.integrate(player_2, segment_2, r'13')
        self.wait(2)
        self.play(Write(formula_p_3_0), run_time=3*RUN_TIME)
        self.wait(2)
        self.play(Uncreate(formula_p_3_0), run_time=RUN_TIME/1.5)
        self.wait(2)
        self.play(Write(formula_p_3_1[:3]), run_time=1.5*RUN_TIME)
        self.play(Write(formula_p_3_1[3:]), run_time=1.5*RUN_TIME)
        self.integrate(player_3, segment_3, r'57')
        self.wait(2)
        self.play(Write(formula_p_3_2), run_time=RUN_TIME)
        self.wait(2)
        ############################
    
    

    def integrate(self, player, segment, label):
        player.clear_updaters()
        segment.set_label(MathTex(label, font_size=DEFAULT_LABEL_FONT_SIZE))
        self.play(
            self.fade_in_out(segment, player),
            ReplacementTransform(VGroup(*[s.label for s in player]), segment.update_label_pos())
        )

    def unit_segment(self):
        return Segment(ORIGIN, UNIT_SEGMENT_LENGTH*RIGHT, r'11', DEFAULT_LABEL_FONT_SIZE, stroke_width=DEFAULT_LABEL_STROKE_WIDTH, color=GREEN)
    
    def unit_segment_with_additional(self, additional):
        label_text="{:,}".format(int(additional))
        s=Segment(ORIGIN, VALUE_TO_SEGMENT_LENGTH*SCALE_DEMERGER*additional*RIGHT, label_text, DEFAULT_LABEL_FONT_SIZE, stroke_width=DEFAULT_LABEL_STROKE_WIDTH, color=YELLOW)
        s.label.add_updater(lambda mob: s.update_label_pos())
        return [self.unit_segment(), s]

    def from_player_segment(self, player):
        return Segment(player.get_edge_center(LEFT), player.get_edge_center(RIGHT), color=GREEN_A, stroke_width=DEFAULT_LABEL_STROKE_WIDTH)
    def get_tree(self):
        tree_target = VGroup(*[Circle(0.1, GREEN, fill_color=GREEN) for _ in range(3)])
        tree_target[0].shift(0.00*RIGHT).set_fill(YELLOW, 0.8)
        tree_target[1].shift(0.1*RIGHT).set_fill(GREEN, 0.8)
        tree_target[2].shift(0.05*RIGHT + 0.1*UP).set_fill(GREEN_E, 0.8)
        tree = Union(tree_target[0], tree_target[1], tree_target[2])
        tree.set_stroke(BLACK, width=2, opacity=0.9)
        return tree
    
    def trees_in_rows(self, player, forest):
        self.play(
            AnimationGroup(
                *[forest[i].animate.move_to(player.point_from_proportion(i/len(forest))) for i in range(len(forest))],
                lag_ratio=0.5
            ),
            run_time=RUN_TIME
        )
    def items_to_segment(self, items, segment):
        return ReplacementTransform(VGroup(items[0], items[-1], items[1:-1],), segment)
    def fade_in_out(self, mob_in, mob_out):
        return AnimationGroup(FadeIn(mob_in, run_time=0.8), FadeOut(mob_out))

    def x4_plus_5(self):
        segment_2x5=VGroup(*[self.segment_2.copy() for _ in range(TIMES)])
        segment_2x5_target=VGroup(*[self.segment_2.copy() for _ in range(len(segment_2x5))]).arrange(RIGHT, buff=0).align_to(self.segment_3, DOWN+LEFT)
        self.play(AnimationGroup(*[ReplacementTransform(segment_2x5[i], segment_2x5_target[i]) for i in range(len(segment_2x5))], lag_ratio=0.5), run_time=RUN_TIME )
        self.wait(2)
        return segment_2x5_target
    def rectangle_surround(self, mob: VMobject, color=PINK):
        x = mob.get_edge_center(RIGHT)[0]-mob.get_edge_center(LEFT)[0]
        y = mob.get_edge_center(UP)[1]-mob.get_edge_center(DOWN)[1]
        rectangle=Rectangle(color, stroke_width=DEFAULT_LABEL_STROKE_WIDTH)
        rectangle.stretch_to_fit_height(1.5*y)
        rectangle.stretch_to_fit_width(x)
        return rectangle.move_to(mob.get_center())

