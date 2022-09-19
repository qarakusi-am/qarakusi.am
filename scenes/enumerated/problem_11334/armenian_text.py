from manim import Tex
from manim import ORANGE

youngest = Tex('Կրտսեր')
second = Tex('Կրտսերից մեծ է $3$ տարով')
third = Tex('Միջնեկը իրենից փոքրից մեծ է $3$ տարով')
fourth = Tex('Միջնեկից մեծ է $3$ տարով')
fifth = Tex('Ավագ', 'ը ևս իրենից փոքրից մեծ է $3$ տարով')
fifth_2 = Tex('Ավագ', 'ը կրտսերից մեծ է $4$ անգամ')
oldest = Tex('Ավագ')

property_1 = Tex("Պայման ", "$1$` Կա ընդհանուր $5$ երեխա։")
property_1[0].set_color(ORANGE)

property_2 = Tex("Պայման ", "$2$` Ամեն երեխա իր նախորդից փոքր է $3$ տարով։")
property_2[0].set_color(ORANGE)

property_3 = Tex("Պայման ", "$3$` Ավագը կրտսերից մեծ է $4$ անգամ։")
property_3[0].set_color(ORANGE)