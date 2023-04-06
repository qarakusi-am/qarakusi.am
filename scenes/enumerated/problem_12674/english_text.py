TASK_NUMBER_STR = "P. 12674"
LEFT_CAR_SPEAD = r"80\text{ km/h}"
RIGHT_CAR_SPEAD = r"70\text{ km/h}"
MEETING_MOMENT = r"\text{Meeting moment}"
BEFORE_MEETING_2 = r"\text{ minutes before the meeting}"
ONE_HOUR_ROAD = r"\text{ Car's pass distance in one hour}"
KM_80 = r"80\text{km}"
KM_70 = r"70\text{km}"
PLUS = r"\text{+}"
EQUAL = r"\text{ = }"
KM_150 = r"\text{150km}"

from manim import RIGHT
from manim import MathTex, Group
from manim import always_redraw, ValueTracker


t = ValueTracker()
before_meeting_clock = always_redraw(lambda:MathTex(int(t.get_value())
                                                    ).move_to([-3, 0.5, 0]).scale(1.2))
before_meeting_2 = MathTex(BEFORE_MEETING_2).move_to(before_meeting_clock).scale(1.2).shift(4 * RIGHT)
before_meeting_group = Group(before_meeting_2, before_meeting_clock)

left_car_spead = MathTex(LEFT_CAR_SPEAD)
right_car_spead = MathTex(RIGHT_CAR_SPEAD)
