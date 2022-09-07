from manim import UP, DOWN, LEFT, RIGHT
from manim import VGroup
from manim import MathTex
from manim import YELLOW
from manim import Scene, Write
from manim import UpdateFromAlphaFunc
from manim import Rectangle
from manim import Tex


class Task(VGroup):
    """Կամյական խնդրի ձևակերպում"""

    def __init__(
        self,
        number: MathTex,
        text: VGroup,
        **kwargs
    ):
        super().__init__()

        self.number = number.set_color(YELLOW)
        self.text = text.arrange(DOWN, aligned_edge=LEFT)

        self.add(self.number, self.text.align_to(self.number, UP))
        self.arrange(RIGHT, aligned_edge=UP)


class QarakusiScene(Scene):
    def task_number_box(self, text):
        text = Tex(text, font_size=35)
        box = Rectangle(width=text.width+.4, height=text.height+.4, stroke_width=1.5)
        text.move_to(box.get_center())
        return VGroup(text, box).to_edge(LEFT+UP, buff=.2)
    
    def write_task(
        self,
        task: Task,
        run_time=7
    ):
        self.play(Write(task.number))
        self.play(Write(task.text, run_time=run_time))

    def move_task_up(
        self,
        task: Task
    ):
        [x_number_0, y_number_0, z_number_0] = task.number.get_center()
        [x_text_0, y_text_0, z_text_0] = task.text.get_center()
        y_up_number_0 = task.number.get_edge_center(UP)[1]
        y_up_text_0 = task.text.get_edge_center(UP)[1]
        [x_number_1, y_number_1, z_number_1] = [-6, 24 / 7, 0]
        [x_text_1, y_text_1, z_text_1] = [
            x_text_0,
            24 / 7 + (y_up_number_0 - y_number_0) - (y_up_text_0 - y_text_0),
            z_text_0
        ]

        def go_up(
            task: Task,
            t
        ):
            pos_number = [x_number_0 * (1-t) + x_number_1 * t,
                          y_number_0 * (1-t) + y_number_1 * t,
                          z_number_0 * (1-t) + z_number_1 * t]
            task.number.move_to(pos_number).set_opacity(1-t/2)
            pos_text = [x_text_0 * (1-t) + x_text_1 * t,
                        y_text_0 * (1-t) + y_text_1 * t,
                        z_text_0 * (1-t) + z_text_1 * t]
            task.text.move_to(pos_text).set_opacity(1-t/3)

        self.play(UpdateFromAlphaFunc(task, go_up))

    def play_task(
        self,
        task: Task,
        run_time=8
    ):
        self.write_task(task, run_time=run_time - 2)
        self.wait()
        self.move_task_up(task)
