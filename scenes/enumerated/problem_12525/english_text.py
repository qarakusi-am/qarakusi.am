from manim import MathTex, GREEN, ORANGE, VGroup, DOWN, LEFT

problem_condition_str = [
    r'There\ are\ 10\ points\ inside\ an',
    r'equilateral\ triangle\ with\ side\ 3.',
    r'Prove\ that\ we\ can\ find\ 2\ points,\ such\ that',
    r'the\ distance\ between\ them\ is\ less\ than\ 1.'
]

problem_condition = MathTex(*problem_condition_str, font_size=30)
problem_condition.set_color_by_gradient(GREEN, ORANGE)

problem = VGroup(
    problem_condition[0],
    problem_condition[1],
    problem_condition[2],
    problem_condition[3]
).arrange(DOWN, aligned_edge=LEFT, buff=0.1).move_to([-3.75, 3, 0])
