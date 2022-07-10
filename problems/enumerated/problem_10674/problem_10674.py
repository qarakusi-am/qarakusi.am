from manim import ApplyWave
from maserovkhndirner import SimpleTwoPartsProblem
from maserovkhndirscene import MaserovKhndirScene
from qarakusiscene import Task
from .text import problem_statement, problem_number
from .text import first_name, second_name, extra_length, total_length, part


class Problem10674(MaserovKhndirScene):
    def __init__(self):
        super().__init__()

        print(problem_statement)
        self.task = Task(
            problem_number,
            problem_statement
        )

        self.name_1 = first_name
        self.name_2 = second_name
        self.extra_length = extra_length
        self.total_length = total_length
        self.wanted = 'both'

        self.problem = SimpleTwoPartsProblem(
            self.name_1,
            self.name_2,
            part,
            self.extra_length,
            self.total_length,
            self.wanted
        )

    def construct(self):
        self.play_task(self.task)
        self.PlayProblemProjecting(self.problem)
        self.PlaySolution(self.problem, indication=ApplyWave)
