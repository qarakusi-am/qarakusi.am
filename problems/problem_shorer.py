
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
