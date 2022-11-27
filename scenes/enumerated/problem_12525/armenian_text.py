from manim import MathTex, GREEN, ORANGE, VGroup, DOWN, LEFT

problem_condition_str = [
    r'3', r'\textrm{ կողմով եռանկյան մեջ նշված է }', r'10', r'\textrm{ կետ։}',
    r'\textrm{Ապացուցել, որ կարելի է ընտրել դրանցից}',
    r'2', r'\textrm{-ն այնպես, որ դրանցով կազմված}',
    r'\textrm{հատվածի երկարությունը մեծ չլինի }', r'1', r'\textrm{-ից։}'
]

problem_condition = MathTex(*problem_condition_str, font_size=30)
problem_condition.set_color_by_gradient(GREEN, ORANGE)

problem = VGroup(
    VGroup(*problem_condition[:4]),
    VGroup(*problem_condition[4]),
    VGroup(*problem_condition[5:7]),
    VGroup(*problem_condition[7:])
).arrange(DOWN, aligned_edge=LEFT, buff=0.1).move_to([-3.75, 3, 0])
