from manim import Text, VGroup, Tex, MathTex
from manim import RED, ORANGE, GREEN
from manim import DOWN, LEFT, UP
from constants import DEFAULT_TASK_FONT_SIZE

problem = Tex("Ուռուցիկ բազմանկյան գագաթները ներկված են առնվազն 3 գույնով, \\\ ", "ընդ որում հարևան գագաթները տարբեր գույների են։ \\\ ",
              "Հնարավո՞ր է այդ բազմանկյունը տրոհել այնպիսի եռանկյունների, \\\ ", "որոնց գագաթները կլինեն տարբեր գույների։", font_size=DEFAULT_TASK_FONT_SIZE)
# for i in range(1, len(problem)):
#     problem[i].align_to(problem[i-1], LEFT)

text_1 = Tex("Մնաց ընդամենը ", "$2$ ", "գույն։")

rule_1 = Tex("$!$", "Ամեն անգամ եռանկյուն անջատելուց հետո \\\ ", 
             "պետք է մնացած գագաթների գույների \\\ ",
             "քանակը լինի $2$-ից ավելի։", font_size=37.5)
for i in range(1, len(rule_1)):
    rule_1[i].align_to(rule_1[i-1], LEFT)
rule_1[0].set_color(RED).scale(3).next_to(rule_1[2], LEFT, buff=0.2)

text_2 = Tex("Միակ ", "նարնջագույն ", "գագաթը։", font_size=37.5)
text_2[1].set_color(ORANGE)

rule_2 = Tex("\\checkmark", "Եթե որևէ գույնի կա ճիշտ $1$ գագաթ, \\\ ",
             "ապա խնդիրը լուծված է։", font_size=37.5)
rule_2[0].set_color(GREEN).scale(2)

question = MathTex("\\exists ?", font_size=40)

