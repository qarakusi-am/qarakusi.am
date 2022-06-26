
from manim import *
from aramanim import *

#diagram config
BUUF_BETWEEN_PLAYERS = 0.75

#segmen config
UNIT_SEGMENT_LENGTH = 1.2
UNIT_SEGMENT_VALUE = 31000
DEFAULT_LABEL_STROKE_WIDTH = 6
VALUE_TO_SEGMENT_LENGTH = UNIT_SEGMENT_LENGTH / UNIT_SEGMENT_VALUE
SCALE_DEMERGER = 4.75
##

DEFAULT_LABEL_FONT_SIZE = 73

##color
COLOR_PALETTE = [
    '#44D492',
    '#88F7E2',
    '#F5EB67',
    '#FFA15C',
    '#FA233E'
]
##

##names
NAME_0 = r'Ընդամենը'
NAME_1 = r'Բաճկոն'
NAME_2 = r'Շալվար'
NAME_3 = r'Կոշիկ'
## 

##texts
TEXT_0 = [r'― $240000$ դրամ']
TEXT_2 = [r'― Բաճկոնի կեսից ', r'$10000$', r'-ով ավելի']
TEXT_3 = [r'― Շալվարի կեսից ', r'$8000$', r'-ով ավելի']

##animation config
RUN_TIME = 2
WAIT_TIME = 1.5
MEDIUM_LAG_RATIO = 0.55
SMALL_LAG_RATIO = 0.25
BIG_LAG_RATIO = 0.75

##main functions

def unit_segment():
    label_text = r"{:,}".format(int(UNIT_SEGMENT_VALUE))
    s = Segment(
        ORIGIN, UNIT_SEGMENT_LENGTH*RIGHT,
        label_text, DEFAULT_LABEL_FONT_SIZE/2,
        stroke_width=DEFAULT_LABEL_STROKE_WIDTH, color=COLOR_PALETTE[1]
    )
    s.label.add_updater(lambda mob: s.update_label_pos())
    return s

def segment_from_value(value):
    label_text = r"{:,}".format(int(value))
    s = Segment(
        ORIGIN, VALUE_TO_SEGMENT_LENGTH*SCALE_DEMERGER*value*RIGHT,
        label_text, DEFAULT_LABEL_FONT_SIZE/2,
        stroke_width=DEFAULT_LABEL_STROKE_WIDTH, color=COLOR_PALETTE[4]
    )
    s.label.add_updater(lambda mob: s.update_label_pos())
    return s

def unit_segment_with_additional(additional):
    label_text = r"{:,}".format(int(additional))
    s = Segment(
        ORIGIN, VALUE_TO_SEGMENT_LENGTH*SCALE_DEMERGER*additional*RIGHT,
        label_text, DEFAULT_LABEL_FONT_SIZE/2,
        stroke_width=DEFAULT_LABEL_STROKE_WIDTH, color=COLOR_PALETTE[4]
    )
    s.label.add_updater(lambda mob: s.update_label_pos())
    return [unit_segment(), s]

def from_player_segment(player):
    s = Segment(
        player.get_edge_center(LEFT),
        player.get_edge_center(RIGHT),
        stroke_width=DEFAULT_LABEL_STROKE_WIDTH
    )
    return s

def surround_object(mob, buff = 0.1):
    mob_width = mob.get_edge_center(RIGHT)[0] - mob.get_edge_center(LEFT)[0]
    mob_height = mob.get_edge_center(UP)[1] - mob.get_edge_center(DOWN)[1]
    round_rect_width = mob_width + 2 * buff
    round_rect_height = mob_height + 2 * buff
    round_rect = RoundedRectangle()
    round_rect.stretch_to_fit_height(round_rect_height)
    round_rect.stretch_to_fit_width(round_rect_width)
    round_rect.move_to(mob)
    return round_rect
def fade_in_out(mob_in, mob_out):
        return AnimationGroup(FadeIn(mob_in, run_time=0.8), FadeOut(mob_out))

def integrate(player, segment, label):
    player.clear_updaters()
    segment.set_label(MathTex(label, font_size=DEFAULT_LABEL_FONT_SIZE/2))
    animation = AnimationGroup(
        fade_in_out(segment, player),
        ReplacementTransform(VGroup(*[s.update_label_pos() for s in player]), segment.update_label_pos())
    )
    return animation


class TaskWithParts(Scene):
    def construct(self):
        ##############
        name_0 = Tex(NAME_0, font_size=DEFAULT_LABEL_FONT_SIZE/2, tex_template=ARMTEX)
        text_0 = Tex(*TEXT_0, font_size=DEFAULT_LABEL_FONT_SIZE/2, tex_template=ARMTEX)
        ### Defining main mobjects
        line = Line(3*UP + 0.75*RIGHT, 3*DOWN + 0.75*RIGHT)
        #self.add(line)

        ### participant_1 ### 
        participant_1 = VGroup(*[unit_segment() for _ in range(4)])
        participant_1.arrange(RIGHT, buff = 0)
        participant_1_nontarget = from_player_segment(participant_1)
        participant_1_nontarget_2 = VGroup(from_player_segment(participant_1[0:2]), from_player_segment(participant_1[2:]))

        
        name_1 = Tex(NAME_1, font_size=DEFAULT_LABEL_FONT_SIZE/2, tex_template=ARMTEX)
        name_1.set_color(COLOR_PALETTE[0])

        ### participant_2 ###
        participant_2 = VGroup(*[unit_segment(), *unit_segment_with_additional(10000)])
        participant_2.arrange(RIGHT, buff = 0)
        
        participant_2_nontarget = VGroup(from_player_segment(participant_2[:2]), segment_from_value(10000))
        participant_2_nontarget.arrange(RIGHT, buff = 0)

        name_2 = Tex(NAME_2, font_size=DEFAULT_LABEL_FONT_SIZE/2, tex_template=ARMTEX)
        name_2.set_color(COLOR_PALETTE[2])

        text_2 = Tex(*TEXT_2, font_size=DEFAULT_LABEL_FONT_SIZE/2, tex_template=ARMTEX)
        text_2.set_color(COLOR_PALETTE[2])
        ### participant_3 ###
        participant_3 = VGroup(*unit_segment_with_additional(13000)).arrange(RIGHT, buff = 0)
        participant_3_nontarget = VGroup(*unit_segment_with_additional(5000), segment_from_value(8000))
        participant_3_nontarget.arrange(RIGHT, buff = 0)

        name_3 = Tex(NAME_3, font_size=DEFAULT_LABEL_FONT_SIZE/2, tex_template=ARMTEX)
        name_3.set_color(COLOR_PALETTE[4])

        text_3 = Tex(*TEXT_3, font_size=DEFAULT_LABEL_FONT_SIZE/2, tex_template=ARMTEX)
        text_3.set_color(COLOR_PALETTE[4])

        ### diagram ###
        diagram = VGroup(participant_1, participant_2, participant_3)
        diagram.arrange(DOWN, buff = BUUF_BETWEEN_PLAYERS, aligned_edge=LEFT)
        diagram.next_to(line, LEFT, buff=0.95).shift(2*UP)
        participant_1_nontarget.align_to(participant_1, UP+LEFT)
        participant_1_nontarget_2.align_to(participant_1, UP+LEFT)
        participant_2_nontarget.align_to(participant_2, UP+LEFT)
        participant_3_nontarget.align_to(participant_3, UP+LEFT)
        #participant_3_nontarget.align_to()
                
        name_1.next_to(participant_1, LEFT, buff=0.45)
        name_2.next_to(participant_2, LEFT, buff=0.45)
        name_3.next_to(participant_3, LEFT, buff=0.45)
        name_0.next_to(name_3, DOWN, buff=BUUF_BETWEEN_PLAYERS, aligned_edge=RIGHT)

        text_0.next_to(name_0, RIGHT, buff=0.45)
        text_2.next_to(name_2, RIGHT, buff=0.45)
        text_3.next_to(name_3, RIGHT, buff=0.45)
        
        self.play(AnimationGroup(
            Write(name_0),
            Write(text_0),
            lag_ratio=0.98
        ))
        self.wait(WAIT_TIME)
        
        self.play(AnimationGroup(
            Write(name_1),
            Write(name_2),
            Write(name_3),
            lag_ratio=0.85
        ))

        self.wait(WAIT_TIME)
        self.play(Write(text_2))
        self.wait(WAIT_TIME)
        self.play(Write(text_3))
        self.wait(WAIT_TIME)
        self.play(Create(participant_1_nontarget))
        self.wait(WAIT_TIME)
        participant_2_nontarget[0].save_state()
        participant_2_nontarget[0].align_to(participant_1, UP+LEFT)
        self.play(
            fade_in_out(participant_1_nontarget_2, participant_1_nontarget),
            Restore(participant_2_nontarget[0]),
            FadeOut(text_2[0])
        )
        self.play(
            Create(participant_2_nontarget[1]),
            Write(participant_2_nontarget[1].update_label_pos()),
            FadeOut(text_2[1], text_2[2])
        )
        self.wait(WAIT_TIME)

        participant_3_nontarget[0].save_state()
        participant_3_nontarget[1].save_state()

        participant_3_nontarget[0].align_to(participant_2_nontarget[0], LEFT + UP)
        participant_3_nontarget[1].align_to(participant_2_nontarget[1], LEFT + UP)

        self.play(
            fade_in_out(participant_2[:2], participant_2_nontarget[0])
        )
        self.wait(WAIT_TIME)
        
        self.play(
            Restore(participant_3_nontarget[0]),
            Restore(participant_3_nontarget[1]),
            FadeOut(text_3[0]),
            run_time = 2
        )
        self.play(
            Write(participant_3_nontarget[1].update_label_pos()),
            Create(participant_3_nontarget[2]),
            Write(participant_3_nontarget[2].update_label_pos()),
            FadeOut(text_3[1], text_3[2])
        )
        self.wait(WAIT_TIME)
        self.play(
            fade_in_out(participant_3, participant_3_nontarget),
            TransformMatchingShapes(VGroup(
                    participant_3_nontarget[2].update_label_pos(),
                    participant_3_nontarget[1].update_label_pos()
                ), participant_3[1].update_label_pos())
        )
        
        self.wait(WAIT_TIME)
        total_brace = Brace(diagram, RIGHT, buff=0.1)
        total = MathTex("240000").scale(0.7).rotate(-90*DEGREES).next_to(total_brace, RIGHT, buff=0.1)
        total_brace.add(total)

        self.play(AnimationGroup(*[s.animate(rate_func = rate_functions.there_and_back).shift(0.2*UP) for s in participant_1_nontarget_2], lag_ratio=0.8))
        self.wait(WAIT_TIME)
        self.play(participant_2[:2].animate(rate_func = rate_functions.there_and_back).shift(0.2*UP))
        self.wait(WAIT_TIME/2)
        self.play(fade_in_out(participant_1, participant_1_nontarget_2))
        self.wait(WAIT_TIME)

        self.play(Write(total_brace), FadeOut(name_0, text_0))
        self.wait(WAIT_TIME)


        count = VGroup(*[MathTex(r"{:,}".format(int(i))).scale(0.7).set_color(YELLOW).set_opacity(0) for i in range(1, 8, 1)])
        list_to_count = [
            participant_1[0], participant_1[1], participant_1[2], participant_1[3],
            participant_2[0], participant_2[1],
            participant_3[0]
        ]
        for i in range(len(list_to_count)):
            count[i].next_to(list_to_count[i], DOWN, buff=0)

        formula_1 = MathTex(r"240000-10000-5000-8000=217000").scale(0.8).next_to(name_3, DOWN, buff=0.75, aligned_edge=LEFT)
        formula_2 = MathTex(r"217000:7 = 31000").scale(0.8).next_to(formula_1, DOWN, buff=0.5, aligned_edge=LEFT)
        formula_3 = MathTex(r"4 \cdot 31000 = 124000").scale(0.8).next_to(formula_2, DOWN, buff=0.5, aligned_edge=LEFT)
        formula_4 = MathTex(r"2 \cdot 31000 + 10000 = 72000").scale(0.8).next_to(formula_3, DOWN, buff=0.5, aligned_edge=LEFT)
        formula_5 = MathTex(r"31000 + 13000 = 44000").scale(0.8).next_to(formula_4, DOWN, buff=0.5, aligned_edge=LEFT)
        self.play(
            participant_3[-1].animate.align_to(participant_1, RIGHT),
            participant_2_nontarget[-1].animate.align_to(participant_1, RIGHT),
            Write(formula_1)
        )
        
        
        self.wait(WAIT_TIME)
        self.play(AnimationGroup(
            *[
                AnimationGroup(
                    count[i].animate(rate_func= rate_functions.there_and_back).set_opacity(1),
                    list_to_count[i].animate(rate_func= rate_functions.there_and_back).shift(0.2*UP).set_color(YELLOW),
                )
                for i in range(len(list_to_count))
            ],
            lag_ratio=0.7
        ))
        self.wait(WAIT_TIME)
        self.play(Write(formula_2))
         
        self.wait(WAIT_TIME)

        self.play(
            Write(participant_3[0].update_label_pos())
        )

        self.wait(WAIT_TIME)

        self.play(Write(formula_3))
        participant_1_nontarget.set_color(COLOR_PALETTE[0])
        participant_1_nontarget.set_label(MathTex(r"124000").scale(0.8))
        self.play(
            fade_in_out(participant_1_nontarget, participant_1),
            Write(participant_1_nontarget.label)
        )
        self.wait(WAIT_TIME)
        self.play(Write(formula_4), participant_2_nontarget[-1].animate.next_to(participant_2[1], RIGHT, buff = 0))
        segment_2 = from_player_segment(participant_2).set_color(COLOR_PALETTE[2])
        segment_2.set_label(MathTex(r"72000").scale(0.8))
        self.play(
            fade_in_out(segment_2, VGroup(participant_2, participant_2_nontarget[-1], participant_2_nontarget[-1].label)),
            Write(segment_2.label)
        )
        self.wait(WAIT_TIME)
        self.play(Write(formula_5), participant_3[-1].animate.next_to(participant_3[0], RIGHT, buff = 0))
        segment_3 = from_player_segment(participant_3).set_color(COLOR_PALETTE[4])
        segment_3.set_label(MathTex(r"44000").scale(0.8))
        self.play(
            fade_in_out(segment_3, VGroup(participant_3, participant_3[-1].label, participant_3[0].label)),
            Write(segment_3.label)
        )
        self.wait(WAIT_TIME)



        

#        text_2.next_to(name_2, RIGHT, buff=0.45)
#        text_3.next_to(name_3, RIGHT, buff=0.45)
#
#        participant_2_label = participant_2[-1].update_label_pos().copy()
#        participant_2_nontarget.align_to(participant_2, LEFT + UP)
#        participant_2_target[-1].update_label_pos()
#        participant_2_target[-2].update_label_pos()
#
#        round_rect = surround_object(participant_1)
#        round_rect.set_color(COLOR_PALETTE[4])
#
#        #brace_3 = Brace(participant_3[1:3], DOWN)
#        #brace_3.label = MathTex(r'11', font_size=DEFAULT_LABEL_FONT_SIZE, tex_template=ARMTEX)
#        #brace_3.label.next_to(brace_3, DOWN, buff = 1.5 * DEFAULT_MOBJECT_TO_MOBJECT_BUFFER)
#
#        participant_3_compp = VGroup(
#            participant_3[0].copy(),
#            from_player_segment(participant_3[1:3])
#        )
#        participant_3_compp.set_color(WHITE)
#        participant_3_compp[1].set_label(MathTex(r'11', font_size=DEFAULT_LABEL_FONT_SIZE, tex_template=ARMTEX))
#        participant_3_compp_target = participant_3[0:3].copy()
#        participant_3_compp_target.set_color(WHITE)
#        participant_3_compp_target.shift(DOWN)
#
#
#        segment_1 = from_player_segment(participant_1)
#        segment_1.set_color(COLOR_PALETTE[0])
#        segment_2 = from_player_segment(participant_2)
#        segment_2.set_color(COLOR_PALETTE[2])
#        segment_3 = from_player_segment(participant_3[0:3])
#        segment_3.set_color(COLOR_PALETTE[4])
#        segment_3_nontarget = from_player_segment(participant_2)
#        segment_3_semi_half = from_player_segment(participant_3[0:3])
#        segment_3_left_half = from_player_segment(participant_3)
#        segment_3_right_half = segment_3_left_half.copy().next_to(segment_3_left_half, RIGHT, buff = 0)
#
#        brace_total = Brace(diagram, RIGHT)
#        brace_total.label = MathTex(r'71', font_size=DEFAULT_LABEL_FONT_SIZE, tex_template=ARMTEX)
#        brace_total.label.next_to(brace_total, RIGHT)
#        ##############
#
#        self.play(
#            AnimationGroup(
#                Write(name_2),
#                Write(name_1),
#                Write(name_3),
#                lag_ratio = MEDIUM_LAG_RATIO
#            ), run_time = 2.5 * RUN_TIME
#        )
#        self.wait(WAIT_TIME)
#        self.play(Write(text_2), run_time = 2 * RUN_TIME)
#        self.wait(WAIT_TIME)
#        self.play(Create(participant_1), run_time = RUN_TIME)
#        self.wait(WAIT_TIME)
#        self.play(
#            FadeOut(text_2[0], text_2[-1], run_time = 0.2 * RUN_TIME),
#            Create(participant_2, run_time = 3.5 * RUN_TIME),
#            ReplacementTransform(text_2[1], participant_2[-1].update_label_pos(), run_time = 1.5 * RUN_TIME)
#        )
#        self.wait(WAIT_TIME)
#        self.play(Write(text_3), run_time = 2 * RUN_TIME)
#        self.play(Create(round_rect), run_time = 0.5 * RUN_TIME)
#        self.play(round_rect.animate.set_color(PINK), run_time = 0.5 * RUN_TIME)
#        self.play(FadeOut(round_rect), run_time = 1.5 * RUN_TIME)
#        self.wait(WAIT_TIME)
#        self.play(
#            segment_3_nontarget.animate.align_to(segment_3, LEFT + DOWN),
#            text_3.animate.shift(DOWN), run_time = RUN_TIME
#        )
#        self.play(
#            fade_in_out(VGroup(segment_3_left_half, segment_3_right_half),
#            segment_3_nontarget), run_time = 0.8 * RUN_TIME
#        )
#        self.play(
#            segment_3_right_half.animate.shift(RIGHT).set_opacity(0),
#            run_time = RUN_TIME
#        )
#        self.remove(segment_3_right_half)
#        self.play(
#            fade_in_out(VGroup(segment_3_semi_half, participant_3[-1]), segment_3_left_half),
#            ReplacementTransform(text_3[1], participant_3[-1].update_label_pos()),
#            FadeOut(text_3[0], text_3[2]),
#            run_time = 0.5 * RUN_TIME
#        )
#        self.play(FadeOut(participant_3[-1].label, participant_3[-1]))        
#        self.wait(WAIT_TIME)
#        self.play(
#            AnimationGroup(
#                fade_in_out(participant_2_target, participant_2),
#                ReplacementTransform(
#                    participant_2[-1].label,
#                    VGroup(participant_2_target[-1].label, participant_2_target[-2].label)
#                ),
#                lag_ratio = SMALL_LAG_RATIO
#            ), run_time = 1.5 * RUN_TIME
#        ) 
#        self.wait(WAIT_TIME)
#
#        participant_3_nontarget = participant_2_target[0:2].copy()
#        participant_3_nontarget.add(participant_2_target[-2].copy())
#        
#        participant_3_nontarget[-1].label.add_updater(
#            lambda mob: participant_3_nontarget[-1].update_label_pos()
#        )
#
#        self.add(participant_3_nontarget[-1].update_label_pos())
#
#        self.play(
#            FadeOut(segment_3_semi_half),
#            AnimationGroup(
#                *[nontarget.animate.align_to(target, LEFT + UP)
#                for nontarget, target in zip(participant_3_nontarget, participant_3)],
#                lag_ratio = SMALL_LAG_RATIO
#            ), run_time = RUN_TIME
#        )
#        self.wait(WAIT_TIME)
#        participant_3[-1].update_label_pos()
#        participant_3[-2].update_label_pos()
#        self.play(
#            AnimationGroup(
#                fade_in_out(participant_2, participant_2_target),
#                ReplacementTransform(
#                    VGroup(participant_2_target[-1].label, participant_2_target[-2].label),
#                    participant_2_label
#                ),
#                lag_ratio = SMALL_LAG_RATIO
#            ),
#            AnimationGroup(
#                fade_in_out(participant_3, participant_3_nontarget),
#                ReplacementTransform(
#                    participant_3_nontarget[-1].label,
#                    VGroup(participant_3[-1].label, participant_3[-2].label)
#                ),
#                lag_ratio = SMALL_LAG_RATIO
#            ), run_time = 1.5 * RUN_TIME
#        )
#        self.wait(WAIT_TIME)
#        self.play(
#            participant_3[-1].animate.shift(DOWN).set_opacity(0),
#            participant_3[-1].label.animate.shift(DOWN).set_opacity(0),
#            run_time = RUN_TIME
#        )
#        self.remove(participant_3[-1], participant_3[-1].label)
#        participant_3.remove(participant_3[-1])
#        self.wait(WAIT_TIME)
#
#        player_2 = VGroup(name_2, participant_2, participant_2_label)
#        dashline_left = DashedLine(
#            participant_1.get_left(),
#            participant_3.get_left(),
#            stroke_width = DEFAULT_LABEL_STROKE_WIDTH
#        )
#        dashline_left.set_color(COLOR_PALETTE[0])
#        dashline_left.set_opacity(0.8)
#        dashline_right = dashline_left.copy()
#        dashline_right.align_to(participant_1, RIGHT)
#        dashline = VGroup(dashline_left, dashline_right)
#
#        #self.play(
#        #    player_2.animate.set_opacity(0),
#        #    Create(dashline),
#        #    run_time = 0.5 * RUN_TIME
#        #)
#        participant_3_copy = participant_3[0:3].copy()
#        participant_3_copy.set_color(WHITE)
#        self.play(
#            player_2.animate.set_opacity(0),
#            ReplacementTransform(participant_1[0].copy(), participant_3_compp[0]),
#            participant_3[0:3].animate.shift(DOWN),
#            run_time = 0.75 * RUN_TIME
#        )
#
#
#
#        self.play(
#            Create(participant_3_compp[1]),
#            Write(participant_3_compp[1].update_label_pos()),
#            run_time = 0.5 * RUN_TIME
#        )
#
#        self.wait(WAIT_TIME)
#        #self.play(
#        #    Write(brace_3),
#        #    Write(brace_3.label),
#        #    FadeOut(dashline),
#        #    run_time = RUN_TIME
#        #)
#        
#
#        s_down = Scissors(participant_3[2].get_left()).scale(0.9)
#        s_up = Scissors(participant_3_copy[2].get_left()).scale(0.9)
#        formula_0 = MathTex(r'11', r'-', r'2', r'=', r'9', font_size=DEFAULT_LABEL_FONT_SIZE, tex_template=ARMTEX)
#        formula_0.align_to(participant_3_compp[1].update_label_pos(), LEFT + UP)
#        #formula_0.align_to(brace_3.label, LEFT + UP)
#        #formula_0.align_to(brace_3.label, LEFT + UP)
#        #self.play(
#        #    FadeOut(brace_3),
#        #    run_time = 0.5 * RUN_TIME
#        #)
#        
#        self.play(CutIn(s_down), run_time = 0.75 * RUN_TIME)
#        self.play(
#            FadeOut(s_down),
#            participant_3[2].animate.shift(0.2 * RIGHT),
#            #Write(formula_0[1:]),
#            run_time = 1.5 * RUN_TIME
#        )
#        self.play(
#            CutIn(s_up),
#            fade_in_out(participant_3_copy, participant_3_compp),
#            run_time = 0.75 * RUN_TIME
#        )
#        self.play(
#            FadeOut(s_up),
#            participant_3_copy[2].animate.shift(0.2 * RIGHT),
#            Write(formula_0[1:]),
#            run_time = 1.5 * RUN_TIME
#        )
#
#        self.wait(WAIT_TIME)
#        self.play(
#            ReplacementTransform(formula_0[-1], participant_3[1].update_label_pos()),
#            FadeOut(formula_0[0:2], formula_0[3], participant_3_compp[1].label),
#            participant_3[2].animate.shift(0.2 * LEFT),
#            run_time = 0.5 * RUN_TIME
#        )
#
#        self.play(
#            FadeOut(participant_3_copy, formula_0[2]),
#            participant_3.animate.shift(UP),
#            run_time = 0.5 * RUN_TIME
#        )
#
#        self.play(player_2.animate.set_opacity(1), run_time = 0.5 * RUN_TIME)
#        self.wait(WAIT_TIME)
#
#        #self.play(
#        #    ReplacementTransform(formula_0[2], participant_3[1].update_label_pos()),
#        #    FadeOut(formula_0[0:2], brace_3.label),
#        #    participant_3[2].animate.shift(0.2 * LEFT),
#        #    run_time = 0.5 * RUN_TIME
#        #)
#
#        self.wait(WAIT_TIME)
#        self.play(
#            Write(participant_1[0].update_label_pos()),
#            participant_1.animate.set_color(COLOR_PALETTE[0]),
#            run_time = RUN_TIME
#        )
#        self.wait(WAIT_TIME)
#        participant_2[-1].label.become(participant_2_label)
#        self.remove(participant_2_label)
#        self.add(participant_2[-1].label)
#        formula_1 = MathTex(r'4', r'\cdot 9 + 6 =', r'42', font_size=DEFAULT_LABEL_FONT_SIZE, tex_template=ARMTEX)
#        formula_1.next_to(participant_3, DOWN, aligned_edge = LEFT, buff = 2 * DEFAULT_MOBJECT_TO_MOBJECT_BUFFER)
#        self.play(
#            Write(formula_1),
#            integrate(participant_2, segment_2, r'42'),
#            run_time = 1.5 * RUN_TIME
#        )
#        self.wait(WAIT_TIME)
#        formula_2 = MathTex(r'2', r'\cdot 9 + 2 =', r'20', font_size=DEFAULT_LABEL_FONT_SIZE, tex_template=ARMTEX)
#        formula_2.next_to(formula_1, DOWN, aligned_edge = LEFT)
#        self.play(
#            Write(formula_2),
#            integrate(participant_3, segment_3, r'20'),
#            run_time = 1.5 * RUN_TIME
#        )
#        self.wait(WAIT_TIME)
#        formula_3 = MathTex(r'9', r'+', r'42', r'+', r'20', r'=', r'71', font_size=DEFAULT_LABEL_FONT_SIZE, tex_template=ARMTEX)
#        formula_3.next_to(formula_2, DOWN, aligned_edge = LEFT)
#        self.play(
#            AnimationGroup(
#                Write(formula_3[0]),
#                Write(formula_3[1]),
#                ReplacementTransform(formula_1[-1].copy(), formula_3[2]),
#                Write(formula_3[3]),
#                ReplacementTransform(formula_2[-1].copy(), formula_3[4]),
#                Write(formula_3[5]), Write(formula_3[6]),
#                lag_ratio = BIG_LAG_RATIO
#            ),
#            run_time = 4 * RUN_TIME
#        )
#        self.play(
#            Write(brace_total),
#            ReplacementTransform(formula_3[-1].copy(), brace_total.label),
#            run_time = RUN_TIME
#        )
#        self.play(
#            Circumscribe(brace_total.label),
#            brace_total.label.animate.set_color(COLOR_PALETTE[1]),
#            run_time = RUN_TIME
#        )
#        self.wait(2 * WAIT_TIME)

