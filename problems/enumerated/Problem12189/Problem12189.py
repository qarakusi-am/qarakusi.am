from manim import Tex, ApplyWave
from maserovkhndirner import SimpleTwoPartsProblem
from maserovkhndirscene import MaserovKhndirScene
from qarakusiscene import Task
from constants import DEFAULT_TASK_NUMBER_FONT_SIZE, ARMTEX


class Problem1289(MaserovKhndirScene):
    def __init__(self):
        super().__init__()

        self.task = Task(
            Tex('$\\#10674$', font_size=DEFAULT_TASK_NUMBER_FONT_SIZE),
            Tex(
                'Արմենն ու Վազգենը ունեն խնձորներ,'
                'ընդ որում Արմենի խնձորների քանակը '
                'Վազգենի խնձորների քանակի եռապատիկից 5 հատով պակաս է:'
                'Պարզել, թե քանի՞ խնձոր ունեն երկուսով միասին, '
                'եթե Արմենը Վազգենից 13 հատով ավել խնձոր ունի:',
                tex_template=ARMTEX, font_size=DEFAULT_TASK_NUMBER_FONT_SIZE
            )
        )
        self.name_1 = 'Արմեն'
        self.name_2 = 'Վազգեն'
        self.extra_length = 13
        self.total_length = 51
        self.wanted = 'both'

        self.problem = SimpleTwoPartsProblem(
            self.name_1,
            self.name_2,
            self.extra_length,
            self.total_length,
            self.wanted
        )

    def construct(self):
        self.play_task(self.task)
        self.PlayProblemProjecting(self.problem)
        self.PlaySolution(self.problem, indication=ApplyWave)
