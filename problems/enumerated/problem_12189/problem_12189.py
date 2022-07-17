from manim import *

# diagram config
from problems.aramanim import Segment, DEFAULT_LABEL_FONT_SIZE, ARMTEX

BUUF_BETWEEN_PLAYERS = 0.75

# segmen config
UNIT_SEGMENT_LENGTH = 2
UNIT_SEGMENT_VALUE = 9
DEFAULT_LABEL_STROKE_WIDTH = 6
VALUE_TO_SEGMENT_LENGTH = UNIT_SEGMENT_LENGTH / UNIT_SEGMENT_VALUE
SCALE_DEMERGER = 1
SMALL_LABEL_FONT_SIZE = 20
##

##color
COLOR_PALETTE = [
    '#88F7E2',
    '#44D492',
    '#F5EB67',
    '#FFA15C',
    '#FA233E'
]
##

##names
NAME_1 = r'Արմեն'
NAME_2 = r'Վազգեն'
##

##texts
TEXT_2 = [r'Արմենի սնկերի քանակից 13-ով ավելի է']
TEXT_3 = [r'Եթե Վազգենը ունենար ևս 5 սունկ,',
          r'ապա նրա սնկերի քանակը կլիներ Արմենի սնկերի քանակի եռապատիկի չափ']

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
        ORIGIN, UNIT_SEGMENT_LENGTH * RIGHT,
        label_text, DEFAULT_LABEL_FONT_SIZE,
        stroke_width=DEFAULT_LABEL_STROKE_WIDTH, color=COLOR_PALETTE[1]
    )
    s.label.add_updater(lambda mob: s.update_label_pos())
    return s


def segment_from_value(value):
    label_text = r"{:,}".format(int(value))
    s = Segment(
        ORIGIN, VALUE_TO_SEGMENT_LENGTH * SCALE_DEMERGER * value * RIGHT,
        label_text, DEFAULT_LABEL_FONT_SIZE,
        stroke_width=DEFAULT_LABEL_STROKE_WIDTH, color=COLOR_PALETTE[4]
    )
    s.label.add_updater(lambda mob: s.update_label_pos())
    return s


def unit_segment_with_additional(additional):
    label_text = r"{:,}".format(int(additional))
    s = Segment(
        ORIGIN, VALUE_TO_SEGMENT_LENGTH * SCALE_DEMERGER * additional * RIGHT,
        label_text, DEFAULT_LABEL_FONT_SIZE,
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


def surround_object(mob, buff=0.1):
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

class Problem12189(Scene):
    def construct(self):
        ##############
        ### Defining main mobjects

        ### armenSegments ###
        armenSegments = VGroup(*[unit_segment() for _ in range(1)])
        armenSegments.arrange(RIGHT, buff=0)

        armenName = Tex(NAME_1, font_size=DEFAULT_LABEL_FONT_SIZE, tex_template=ARMTEX)
        armenName.set_color(COLOR_PALETTE[0])

        ### vazgenSegments ###
        vazgenSegments = VGroup(*[unit_segment() for _ in range(1)])
        vazgenSegments.add(segment_from_value(13))
        vazgenSegments.arrange(RIGHT, buff=0)

        ### vazgenSegments ###
        vazgenSegmentsUpdated = VGroup(*[unit_segment() for _ in range(1)])
        vazgenSegmentsUpdated.add(segment_from_value(13))
        vazgenSegmentsUpdated.add(segment_from_value(5))
        vazgenSegmentsUpdated.arrange(RIGHT, buff=0)

        armenSegmentsUpdated = VGroup(*[unit_segment() for _ in range(3)])
        armenSegmentsUpdated.arrange(RIGHT, buff=0)

        vazgenName = Tex(NAME_2, font_size=DEFAULT_LABEL_FONT_SIZE, tex_template=ARMTEX)
        vazgenName.set_color(COLOR_PALETTE[2])

        vazgenStatement = Tex(*TEXT_2, font_size=SMALL_LABEL_FONT_SIZE, tex_template=ARMTEX)
        vazgenStatement.set_color(COLOR_PALETTE[2])

        vazgenNextStatement = Tex(*TEXT_3, font_size=SMALL_LABEL_FONT_SIZE, tex_template=ARMTEX)
        vazgenNextStatement.set_color(COLOR_PALETTE[2])

        ### diagram ###
        diagram = VGroup(armenSegments, vazgenSegments)
        diagram.arrange(DOWN, buff=BUUF_BETWEEN_PLAYERS, aligned_edge=LEFT)
        diagram.shift(2 * UP + 0.15 * LEFT)

        # brace_total = Brace(diagram, RIGHT)
        # brace_total.label = MathTex(r'18', font_size=DEFAULT_LABEL_FONT_SIZE, tex_template=ARMTEX)
        # brace_total.label.next_to(brace_total, RIGHT)

        armenName.next_to(armenSegments, LEFT, buff=0.45)
        vazgenName.next_to(vazgenSegments, LEFT, buff=0.45)

        vazgenStatement.next_to(vazgenName, RIGHT, buff=0.45)
        vazgenNextStatement.next_to(vazgenStatement, DOWN, buff=0.45)

        armenSegmentsUpdated.align_to(armenSegments, LEFT)
        vazgenSegmentsUpdated.align_to(vazgenStatement, LEFT)

        round_rect = surround_object(armenSegments)
        round_rect.set_color(COLOR_PALETTE[4])

        # brace_3 = Brace(vazgenSegmentsUpdated[1:3], DOWN)
        # brace_3.label = MathTex(r'11', font_size=DEFAULT_LABEL_FONT_SIZE, tex_template=ARMTEX)
        # brace_3.label.next_to(brace_3, DOWN, buff = 1.5 * DEFAULT_MOBJECT_TO_MOBJECT_BUFFER)

        segment_1 = from_player_segment(armenSegments)
        segment_1.set_color(COLOR_PALETTE[0])
        segment_2 = from_player_segment(vazgenSegments)
        segment_2.set_color(COLOR_PALETTE[2])
        segment_3 = from_player_segment(armenSegmentsUpdated)
        segment_3.set_color(COLOR_PALETTE[0])
        segment_4 = from_player_segment(vazgenSegmentsUpdated)
        segment_4.set_color(COLOR_PALETTE[0])

        ##############

        # write names
        self.play(
            AnimationGroup(
                Write(armenName),
                Write(vazgenName),
                lag_ratio=MEDIUM_LAG_RATIO
            ), run_time=2.5 * RUN_TIME
        )
        self.wait(WAIT_TIME)

        # create segments
        self.play(Create(armenSegments), run_time=RUN_TIME)
        self.wait(WAIT_TIME)
        self.play(Write(vazgenStatement), run_time=RUN_TIME)
        self.play(
            FadeOut(vazgenStatement[0], vazgenStatement[-1], run_time=0.4 * RUN_TIME),
            Create(vazgenSegments, run_time=3.5 * RUN_TIME),
            ReplacementTransform(vazgenStatement[0], vazgenSegments[-1].update_label_pos(), run_time=1.5 * RUN_TIME)
        )
        self.wait(WAIT_TIME)

        self.play(Write(vazgenNextStatement), run_time=RUN_TIME)

        self.play(
            Create(vazgenSegmentsUpdated, run_time=3.5 * RUN_TIME),
            ReplacementTransform(vazgenStatement[0], vazgenSegmentsUpdated[-1].update_label_pos(), run_time=1.5 * RUN_TIME)
        )

        self.play(
            vazgenSegmentsUpdated.animate.align_to(segment_2, LEFT + DOWN),
        )
        self.wait(WAIT_TIME)

        self.play(
            Create(armenSegmentsUpdated, run_time=3.5 * RUN_TIME),
        )

        self.play(
            armenSegmentsUpdated.animate.align_to(segment_1, LEFT + DOWN),
        )
        self.wait(WAIT_TIME)



