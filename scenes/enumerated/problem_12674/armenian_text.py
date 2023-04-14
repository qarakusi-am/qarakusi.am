TASK_NUMBER_STR = "Խ. 12674"
LEFT_CAR_SPEAD = r"80\text{ կմ/ժ}"
RIGHT_CAR_SPEAD = r"70\text{ կմ/ժ}"
MEETING_MOMENT = r"\text{Հանդիպման պահը}"
BEFORE_MEETING_1 = r"\text{Հանդիպումից }"
BEFORE_MEETING_2 = r"\text{ րոպե առաջ}"
ONE_HOUR_ROAD = r"\text{ Մեքենայի մեկ ժամվա անցած ճանապարհ}"
KM_80 = r"80\text{կմ}"
KM_70 = r"70\text{կմ}"
PLUS = r"\text{+}"
EQUAL = r"\text{ = }"
KM_150 = r"\text{150կմ}"


from manim import LEFT, RIGHT
from manim import MathTex, Group
from manim import always_redraw, ValueTracker


t = ValueTracker()
before_meeting_1 = MathTex(BEFORE_MEETING_1).move_to([0.780, 0.5, 0]).scale(1.2).shift(2.22 * LEFT)
before_meeting_clock = always_redraw(lambda:MathTex(int(t.get_value())
                                                    ).move_to(before_meeting_1).scale(1.2).shift(2.27  * RIGHT))
before_meeting_2 = MathTex(BEFORE_MEETING_2).move_to(before_meeting_clock).scale(1.2).shift(1.95 * RIGHT)
before_meeting_group = Group(before_meeting_1, before_meeting_2, before_meeting_clock)

left_car_spead = MathTex(LEFT_CAR_SPEAD).scale(1.2)
right_car_spead = MathTex(RIGHT_CAR_SPEAD).scale(1.2)
