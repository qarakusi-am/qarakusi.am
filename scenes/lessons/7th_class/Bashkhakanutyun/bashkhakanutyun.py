from manim import*
from .text import text_list

def SpetialTransform(mob_1: VMobject, mob_2: VMobject):
    return AnimationGroup(
        mob_1[0].animate.move_to(mob_1),
        mob_1[1].animate.stretch_to_fit_height(mob_2[0].height).stretch_to_fit_width(mob_2[0].width).move_to(mob_2[0]),
        mob_1[2].animate.stretch_to_fit_height(mob_2[1].height).stretch_to_fit_width(mob_2[1].width).move_to(mob_2[1]))
    
class ConectionLine(VMobject):
    def __init__(self, mob_1: VMobject, mob_2: VMobject, dir = DOWN, alpha = 0.5, color=YELLOW, **kwargs):
        super().__init__(color=color, **kwargs)
        vertex_0 = mob_1.get_edge_center(dir) + alpha/3*dir
        self.start_new_path(vertex_0)
        vertex_1 = vertex_0 + alpha*dir
        vertex_2 = Dot(vertex_1).match_x(mob_2).get_center()
        vertex_3 = mob_2.get_edge_center(dir) + alpha/3*dir
        self.add_points_as_corners([vertex_0, vertex_1, vertex_2, vertex_3])
        

H = 2
RATIO = 1.75
class Distributive(Scene):
    def construct(self):
        self.nostalgy()
        self.texting()
        self.main()
        self.separating()
        self.example()

    def nostalgy(self):
        dist_f = MathTex('a', '(', 'x', '+', 'y',')').scale(1.35)
        dist_ff = MathTex('a', '(', 'x', '+', 'y',')', '=', 'a', 'x', '+', 'a', 'y').scale(1.35)
        a = MathTex('a').scale(0.75)
        b = MathTex('x').scale(0.75)
        c = MathTex('y').scale(0.75)
        sign_eq = MathTex('=').scale(1.35)
        sign_pl = MathTex('+').scale(1.35)
        ab = Rectangle(height=H, width=H/RATIO).set_fill('#628E90', 1)
        ac = Rectangle(height=H, width=(RATIO**2-0.5)*H/RATIO).set_fill('#B73E3E', 1)
        ab_ac = VGroup(ab, ac).arrange(RIGHT, buff=-0.01)
        ab_ac_f = VGroup(ab_ac, dist_f).arrange(UP, buff=0.35)
        left_edg = dist_f[1:].get_edge_center(LEFT)
        dist_f[1].set_color(BLACK)
        dist_f[5].set_color(BLACK)
        VGroup(ab_ac, dist_f[1:]).arrange(UP, buff=0.35)
        ab.add(a.copy().next_to(ab, LEFT, buff = -0.25))
        ab.add(b.next_to(ab.get_edge_center(UP), DOWN, buff = 0.1))
        ac.add(c.next_to(ac.get_edge_center(UP), DOWN, buff = 0.1))
        self.add(ab_ac)
        self.wait()
        self.play(AnimationGroup(
            AnimationGroup(
                ReplacementTransform(ab[2].copy(), dist_f[2]),
                ReplacementTransform(ac[1].copy(), dist_f[4])),
            FadeIn(dist_f[3], scale=1.5),
            lag_ratio=0.5
        ), run_time = 2)
        self.play(AnimationGroup(
            ReplacementTransform(ab[1].copy(), dist_f[0]),
            dist_f[1:].animate.next_to(left_edg, RIGHT, buff = 0).set_color(WHITE),
            lag_ratio=0.2
        ), run_time = 1.75)
        self.wait()
        ab_ac_copy = ab_ac.copy()
        ab_ac.set_z_index(1)
        self.play(
            ab_ac_f.animate.shift(3.25*LEFT),
            ab_ac_copy.animate.shift(3.25*RIGHT),
            run_time = 2)
        ab_ac_copy[1].add(a.set_color('#B73E3E').next_to(ab_ac_copy[1], LEFT, buff = -0.25))
        sign_pl.move_to(ab_ac_copy[1].get_edge_center(LEFT))
        sign_eq.move_to(0.5*(ab_ac.get_edge_center(LEFT) + ab_ac_copy.get_edge_center(RIGHT))).shift(0.25*LEFT)
        self.play(AnimationGroup(
            AnimationGroup(
                ab_ac_copy[0].animate.shift(0.5*LEFT),
                ab_ac_copy[1].animate.shift(0.5*RIGHT),
                ab_ac_copy[1][2].animate.set_color(WHITE).shift(0.5*RIGHT)),            
            FadeIn(sign_pl, scale=1.5),
            FadeIn(sign_eq, scale=1.5),
            lag_ratio=0.25
        ), run_time = 2)
        self.wait()
        dist_ff.align_to(dist_f, DOWN)
        dist_ff[6].match_x(sign_eq)
        dist_ff[7:9].match_x(ab_ac_copy[0])
        dist_ff[9].match_x(sign_pl)
        dist_ff[10:12].match_x(ab_ac_copy[1])
        self.play(AnimationGroup(
            AnimationGroup(
                ReplacementTransform(ab_ac_copy[0][1].copy(), dist_ff[7]),
                ReplacementTransform(ab_ac_copy[0][2].copy(), dist_ff[8]),
                lag_ratio=0.05),
            AnimationGroup(
                ReplacementTransform(ab_ac_copy[1][1].copy(), dist_ff[11]),
                ReplacementTransform(ab_ac_copy[1][2].copy(), dist_ff[10]),
                lag_ratio=0.05),
            FadeIn(dist_ff[9], scale=1.5),
            FadeIn(dist_ff[6], scale=1.5),
            lag_ratio=0.25
        ))
        dist_ff[:6].align_to(dist_f, UL)
        self.remove(dist_f)
        self.add(dist_ff[:6])
        self.wait()
        formula_forever = MathTex('a', '(', 'x', '+', 'y',')', '=', 'a', 'x', '+', 'a', 'y').scale(1.35).shift(2*UP)
        formula_forever[0].set_color('#628E90')
        formula_forever[7].set_color('#628E90')
        formula_forever[10].set_color('#628E90')
        self.play(AnimationGroup(
            ReplacementTransform(dist_ff, formula_forever),
            FadeOut(sign_eq, sign_pl, ab_ac_copy, ab_ac, scale = 1.1),
            lag_ratio = 0.05
        ), run_time = 2)        
        self.wait()
        self.previous_formula = formula_forever
    
    def texting(self):
        previous_formula = self.previous_formula
        formula_forever = MathTex(' ', 'a', ' ', ' ',' ','(', 'x', '+', 'y', ' ', ' ', ')', '=', 'a', 'x', '+', 'a', 'y', ' ').match_height(previous_formula).align_to(previous_formula, UL)
        formula_forever[1].set_color('#628E90')
        formula_forever[13].set_color('#628E90')
        formula_forever[16].set_color('#628E90')
        formula_alt = MathTex('(', 'a', '+', 'b',')','(', 'x', '+', 'y', '+', 'z', ')', '=', ' ', ' ', ' ', ' ', ' ', '?').match_height(previous_formula).align_to(previous_formula, UL)
        formula_alt[1].set_color('#628E90')
        formula_alt[3].set_color('#B73E3E')
        formula_alt.shift(formula_forever[5].get_center() - formula_alt[5].get_center())        
        self.remove(previous_formula)
        self.add(formula_forever)
        texts = Tex(*text_list).scale(2)
        texts[3].match_width(texts[0:3])
        texts[4:6].match_width(texts[0:3])
        VGroup(texts[0:3], texts[3], texts[4:6]).arrange(DOWN).scale(0.7)
        self.play(AnimationGroup(
            FadeIn(texts[0], scale = 3),
            Wait(),
            FadeIn(texts[1], texts[2], shift=LEFT),
            FadeIn(texts[3], shift=UP, scale = 0.5),
            FadeIn(texts[4], shift=RIGHT),
            Wait(0.5),
            FadeIn(texts[5], shift=LEFT, scale = 1.5),
            ReplacementTransform(formula_forever, formula_alt),
            lag_ratio=0.7
        ), run_time = 6.5)
        self.wait(2)
        self.play(FadeOut(texts, formula_alt[12:], scale = 1.1))
        self.wait(0.5)
        self.formula_alt = formula_alt[:12]

    def main(self):
        a = 1.05*1.9
        b = 1.05*1.1
        c = 1.05*1.65
        d = 1.05*1.25
        e = 1.05*1.75
        self.a_text = a_text = MathTex('a').scale(0.75)
        self.b_text = b_text = MathTex('b').scale(0.75)
        self.c_text = c_text = MathTex('x').scale(0.75)
        self.d_text = d_text = MathTex('y').scale(0.75)
        self.e_text = e_text = MathTex('z').scale(0.75)
        h_tip = Line(ORIGIN, 0.25*RIGHT).set_stroke(width = 2)
        w_tip_0 = Line(ORIGIN, 0.25*UP).set_stroke(width = 2)
        w_tip_1 = Line(ORIGIN, 0.25*UP).set_stroke(width = 2)
        self.formula = formula = MathTex('(a+b)','(x+y+z)').to_corner(UL).shift(0.5*RIGHT)
        h_edg = MathTex('a', '+', 'b').scale(0.75).rotate(-PI/2)
        w_edg = MathTex('x', '+', 'y', '+', 'z').scale(0.75)
        rect = Rectangle(height=a+b, width=c+d+e)
        self.play(TransformMatchingShapes(self.formula_alt, formula[:12]))
        self.wait()
        self.play(Create(rect), run_time = 1.5)
        h_edg.next_to(rect.get_edge_center(LEFT), RIGHT, buff=0.1)
        w_edg.next_to(rect.get_edge_center(UP), DOWN, buff=0.1)
        self.play(AnimationGroup(
            ReplacementTransform(formula[0][1:4].copy().set_opacity(0.5), h_edg),
            Wait(),
            ReplacementTransform(formula[1][1:6].copy().set_opacity(0.5), w_edg),
            lag_ratio=0.75
        ), run_time = 3)
        self.wait()
        h_tip.move_to((b*rect.get_corner(UL) + a*rect.get_corner(DL))/(a+b))
        w_tip_0.move_to((c*rect.get_corner(UR) + (d+e)*rect.get_corner(UL))/(c+d+e))
        w_tip_1.move_to(((c+d)*rect.get_corner(UR) + e*rect.get_corner(UL))/(c+d+e))
        self.play(AnimationGroup(
            FadeOut(h_edg[1], scale = 0.2),
            AnimationGroup(
                ReplacementTransform(h_edg[0], a_text.next_to((rect.get_corner(UL)+h_tip.get_center())/2, RIGHT, buff=0.1)),
                ReplacementTransform(h_edg[2], b_text.next_to((rect.get_corner(DL)+h_tip.get_center())/2, RIGHT, buff=0.1))),
            Wait(0.5),
            FadeIn(h_tip, scale=3),
            lag_ratio=0.2

        ))
        self.wait()
        self.play(AnimationGroup(
            FadeOut(w_edg[1], w_edg[3], scale = 0.2),
            AnimationGroup(
                ReplacementTransform(w_edg[0], c_text.next_to((rect.get_corner(UL)+w_tip_0.get_center())/2, DOWN, buff=0.1)),
                ReplacementTransform(w_edg[2], d_text.next_to((w_tip_0.get_center()+w_tip_1.get_center())/2, DOWN, buff=0.1)),
                ReplacementTransform(w_edg[4], e_text.next_to((rect.get_corner(UR)+w_tip_1.get_center())/2, DOWN, buff=0.1))),
            Wait(0.5),
            AnimationGroup(
                FadeIn(w_tip_0, scale=3),
                FadeIn(w_tip_1, scale=3)),
            lag_ratio=0.2

        ))
        self.wait()
        w_line_0 = Line(w_tip_0.get_center(), w_tip_0.get_center() + (a+b)*DOWN)
        w_line_1 = Line(w_tip_1.get_center(), w_tip_1.get_center() + (a+b)*DOWN)
        h_line = Line(h_tip.get_center(), h_tip.get_center() + (c+d+e)*RIGHT)
        self.play(AnimationGroup(
            AnimationGroup(
                Create(h_line),
                FadeOut(h_tip)),
            AnimationGroup(
                Create(w_line_0),
                FadeOut(w_tip_0)),
            AnimationGroup(
                Create(w_line_1),
                FadeOut(w_tip_1)),
            lag_ratio = 0.25
        ), run_time = 2)
        self.wait()
        self.ax = ax = Rectangle(height=a , width=c).set_fill('#628E90', opacity=1).align_to(h_line, DOWN).align_to(w_line_0, RIGHT)
        self.ay = ay = Rectangle(height=a , width=d).set_fill('#50729B', opacity=1).align_to(h_line, DOWN).align_to(w_line_1, RIGHT)
        self.az = az = Rectangle(height=a , width=e).set_fill('#3E55A7', opacity=1).align_to(h_line, DOWN).align_to(w_line_1, LEFT)
        self.bx = bx = Rectangle(height=b , width=c).set_fill('#B73E3E', opacity=1).align_to(h_line, UP).align_to(w_line_0, RIGHT)
        self.by = by = Rectangle(height=b , width=d).set_fill('#C35C34', opacity=1).align_to(h_line, UP).align_to(w_line_1, RIGHT)
        self.bz = bz = Rectangle(height=b , width=e).set_fill('#CF7A29', opacity=1).align_to(h_line, UP).align_to(w_line_1, LEFT)
        a_text.set_z_index(1)
        b_text.set_z_index(1)
        c_text.set_z_index(1)
        d_text.set_z_index(1)
        e_text.set_z_index(1)
        self.play(AnimationGroup(
            FadeIn(ax),
            FadeIn(ay),
            FadeIn(az),
            FadeIn(bx),
            FadeIn(by),
            FadeIn(bz),
            lag_ratio=0.15
        ))
        self.wait()
        self.remove(rect, h_line, w_line_0, w_line_1)

    def separating(self):
        formula = self.formula
        a_text = self.a_text
        b_text = self.b_text
        c_text = self.c_text        
        d_text = self.d_text
        e_text = self.e_text
        a_tc = a_text.copy()
        b_tc = b_text.copy()
        c_tc = c_text.copy()
        d_tc = d_text.copy()
        e_tc = e_text.copy()        
        ax = self.ax
        ay = self.ay
        az = self.az
        bx = self.bx
        by = self.by
        bz = self.bz
        ax_c = ax.copy()
        ay_c = ay.copy()
        az_c = az.copy()
        bx_c = bx.copy()
        by_c = by.copy()
        bz_c = bz.copy()
        rect_0 = VGroup(ax, ay, az, bx, by, bz, a_text, b_text, c_text, d_text, e_text).set_z_index(2)
        rect_1 = VGroup(ax_c, ay_c, az_c, bx_c, by_c, bz_c, a_tc, b_tc, c_tc, d_tc, e_tc)
        self.play(AnimationGroup(
            AnimationGroup(
                rect_0.animate.match_x(formula),
                rect_1.animate.shift(2.75*RIGHT)),
            Indicate(formula, scale_factor=1.5, run_time = 2),
            Wait(0.5),
            lag_ratio=0.25
        ), run_time = 2)
        self.wait()        
        by_c.add(
            b_tc.copy().match_color(by_c).next_to(by_c.get_edge_center(LEFT), RIGHT, buff = 0.1),
            d_tc.copy().match_color(by_c).next_to(by_c.get_edge_center(UP), DOWN, buff = 0.1))
        bz_c.add(
            b_tc.copy().match_color(bz_c).next_to(bz_c.get_edge_center(LEFT), RIGHT, buff = 0.1),
            e_tc.copy().match_color(bz_c).next_to(bz_c.get_edge_center(UP), DOWN, buff = 0.1))
        bx_c.add(
            b_tc,
            c_tc.copy().match_color(bx_c).next_to(bx_c.get_edge_center(UP), DOWN, buff = 0.1))
        ay_c.add(
            a_tc.copy().match_color(ay_c).next_to(ay_c.get_edge_center(LEFT), RIGHT, buff = 0.1),
            d_tc)
        az_c.add(
            a_tc.copy().match_color(az_c).next_to(az_c.get_edge_center(LEFT), RIGHT, buff = 0.1),
            e_tc)
        ax_c.add(
            a_tc,
            c_tc)       
        self.play(
            VGroup(ax_c, bx_c).animate.shift(0.75*LEFT),
            ay_c[1].animate.set_color(WHITE), 
            by_c[1].animate.set_color(WHITE),
            VGroup(az_c, bz_c).animate.shift(0.75*RIGHT),
            az_c[1].animate.set_color(WHITE).shift(0.75*RIGHT), 
            bz_c[1].animate.set_color(WHITE).shift(0.75*RIGHT),
            run_time = 2)
        p_signs = VGroup(*[MathTex('+') for _ in range(7)])
        p_signs[0].move_to(ax_c.get_edge_center(DOWN))
        p_signs[1].move_to(ay_c.get_edge_center(DOWN))
        p_signs[2].move_to(az_c.get_edge_center(DOWN))
        p_signs[3].move_to((ax_c.get_edge_center(RIGHT) + ay_c.get_edge_center(LEFT))/2 + (0.75/2)*UP)
        p_signs[4].move_to((ay_c.get_edge_center(RIGHT) + az_c.get_edge_center(LEFT))/2 + (0.75/2)*UP)
        p_signs[5].move_to((bx_c.get_edge_center(RIGHT) + by_c.get_edge_center(LEFT))/2 + (0.75/2)*DOWN)
        p_signs[6].move_to((by_c.get_edge_center(RIGHT) + bz_c.get_edge_center(LEFT))/2 + (0.75/2)*DOWN)
        eq_sign = MathTex('=').move_to((rect_0.get_edge_center(RIGHT) + rect_1.get_edge_center(LEFT))/2)
        self.play(AnimationGroup(
            AnimationGroup(
                VGroup(ax_c, ay_c, az_c).animate.shift((0.75/2)*UP),
                VGroup(bx_c, by_c, bz_c).animate.shift((0.75/2)*DOWN),
                bx_c[2].animate.set_color(WHITE).shift((0.75/2)*DOWN), 
                by_c[2].animate.set_color(WHITE).shift((0.75/2)*DOWN),
                bz_c[2].animate.set_color(WHITE).shift((0.75/2)*DOWN)),
            FadeIn(eq_sign, scale=1.5),
            #AnimationGroup(
            #    FadeIn(p_signs[0], scale=0.5),
            #    FadeIn(p_signs[1], scale=0.5),
            #    FadeIn(p_signs[2], scale=0.5),
            #    FadeIn(p_signs[3], scale=1.5),
            #    FadeIn(p_signs[4], scale=1.5),
            #    FadeIn(p_signs[5], scale=1.5),
            #    FadeIn(p_signs[6], scale=1.5)),
            lag_ratio=0.25
        ), run_time = 1.5)
        rect = Rectangle().stretch_to_fit_height(rect_0.height).stretch_to_fit_width(rect_0.width)
        rect.set_fill(color=['#CF7A29', '#628E90'], opacity=1)
        ab_xyz = MathTex('(a+b)(x+y', '+z', ')').move_to(rect)
        rect.add(ab_xyz)
        rect.set_z_index(3)
        rect.move_to(rect_0)
        ax_text = MathTex('a', 'x').move_to(ax_c)
        ay_text = MathTex('a', 'y').move_to(ay_c)
        az_text = MathTex('a', 'z').move_to(az_c)
        bx_text = MathTex('b', 'x').move_to(bx_c)
        by_text = MathTex('b', 'y').move_to(by_c)
        bz_text = MathTex('b', 'z').move_to(bz_c)
        self.wait()
        self.play(AnimationGroup(
            AnimationGroup(
                FadeIn(rect),
                FadeOut(rect_0),
                lag_ratio=0.2),
            SpetialTransform(ax_c, ax_text),
            SpetialTransform(ay_c, ay_text),
            SpetialTransform(az_c, az_text),
            SpetialTransform(bx_c, bx_text),
            SpetialTransform(by_c, by_text),
            SpetialTransform(bz_c, bz_text),
            lag_ratio=0.05
        ), run_time = 2)
        self.wait()
        formula_c = MathTex(
            '(', 'a', '+', 'b', ')', '(', 'x', '+', 'y', '+', 'z', ')',
            '=', 'ax', '+', 'ay', '+', 'az', '+', 'bx', '+', 'by', '+', 'bz').scale_to_fit_height(formula.height).align_to(formula, UL)
        self.add(formula_c[:12])
        self.remove(formula)
        formula_c[12].match_x(eq_sign)
        formula_c[13].align_to(ax_c[0], LEFT)
        formula_c[23].align_to(az_c[0], RIGHT)
        for i in range(14, 24):
            j = i - 13
            formula_c[i].match_x(Dot(((10-j)*formula_c[13].get_center() + j*formula_c[23].get_center())/10))
        ax_line = ConectionLine(formula_c[1], formula_c[6], alpha=1/5, color = '#628E90')
        ay_line = ConectionLine(formula_c[1], formula_c[8], alpha=1/5, color = '#628E90')
        az_line = ConectionLine(formula_c[1], formula_c[10], alpha=1/5, color = '#628E90')
        bx_line = ConectionLine(formula_c[3], formula_c[6], alpha=1/5, color = '#B73E3E')
        by_line = ConectionLine(formula_c[3], formula_c[8], alpha=1/5, color = '#B73E3E')
        bz_line = ConectionLine(formula_c[3], formula_c[10], alpha=1/5, color = '#B73E3E')
        formula_c[12:].set_opacity(0.4)
        self.play(FadeIn(formula_c[12:]), lag_ratio=0.1)
        self.wait()
        self.play(AnimationGroup(
                Create(ax_line),
                Wiggle(ax_c),
                formula_c[13].animate.set_opacity(1),
                Wait(),
                lag_ratio=0.35))
        self.play(AnimationGroup(
                ReplacementTransform(ax_line, ay_line),
                Wiggle(ay_c),
                formula_c[15].animate.set_opacity(1),
                formula_c[14].animate.set_opacity(1),
                lag_ratio=0.35))
        self.play(AnimationGroup(
                ReplacementTransform(ay_line, az_line),
                Wiggle(az_c),
                formula_c[17].animate.set_opacity(1),
                formula_c[16].animate.set_opacity(1),
                lag_ratio=0.35))
        self.play(Uncreate(az_line))
        self.wait(0.5),
        self.play(AnimationGroup(
                Create(bx_line),
                Wiggle(bx_c),
                formula_c[19].animate.set_opacity(1),
                formula_c[18].animate.set_opacity(1),
                lag_ratio=0.35))
        self.play(AnimationGroup(
                ReplacementTransform(bx_line, by_line),
                Wiggle(by_c),
                formula_c[21].animate.set_opacity(1),
                formula_c[20].animate.set_opacity(1),
                lag_ratio=0.35))
        self.play(AnimationGroup(
                ReplacementTransform(by_line, bz_line),
                Wiggle(bz_c),
                formula_c[23].animate.set_opacity(1),
                formula_c[22].animate.set_opacity(1),
                lag_ratio=0.35))
        self.play(Uncreate(bz_line), formula_c[12].animate.set_opacity(1))
        self.wait()
        az_line_ = ConectionLine(formula_c[1], formula_c[10], dir=UP, alpha=1/5, color = '#3E55A7')
        bz_line_ = ConectionLine(formula_c[3], formula_c[10], alpha=1/5, color = '#CF7A29')
        self.play(AnimationGroup(
            AnimationGroup(
                Create(az_line_),
                Create(bz_line_)),
            AnimationGroup(
                formula_c[17].animate.set_color('#3E55A7').scale(1.05),
                formula_c[23].animate.set_color('#CF7A29').scale(1.05)),
            AnimationGroup(
                Wiggle(az_c),
                Wiggle(bz_c)),
            lag_ratio=0.5,            
        ), run_time=3)
        self.play(FadeOut(az_line_, bz_line_))
        formula_c_alt = MathTex(
            '(', 'a', '+', 'b', ')', '(', 'x', '+', 'y', ' ', ' ', ')',
            '=', 'ax', '+', 'ay', ' ', ' ', '+', 'bx', '+', 'by', ' ', ' ').scale_to_fit_height(formula.height).align_to(formula, UL)
        formula_c_alt[:12].align_to(formula, UR)
        formula_c_alt[12].match_x(eq_sign)
        formula_c_alt[13].match_x(formula_c[13])
        formula_c_alt[14].match_x(formula_c[14])
        formula_c_alt[15].match_x(formula_c[15])
        formula_c_alt[16].match_x(formula_c[15])
        formula_c_alt[17].match_x(formula_c[15])
        formula_c_alt[18].match_x(formula_c[16])
        formula_c_alt[19].match_x(formula_c[17])
        formula_c_alt[20].match_x(formula_c[18])
        formula_c_alt[21].match_x(formula_c[19])
        formula_c_alt[22].match_x(formula_c[19])
        formula_c_alt[23].match_x(formula_c[19])
        rect_alt = Rectangle().stretch_to_fit_height(rect_0.height).stretch_to_fit_width(VGroup(ax, ay).width)
        rect_alt.align_to(ax, UL).match_x(formula_c_alt[:12])
        rect_alt.set_fill(color=['#CF7A29', '#628E90'], opacity=1)
        ab_xyz_alt = MathTex('(a+b)(x+y', ' ', ')').move_to(rect_alt)
        rect_alt.add(ab_xyz_alt)
        rect_alt.set_z_index(3)
        self.play(
            ReplacementTransform(formula_c, formula_c_alt),
            ReplacementTransform(rect, rect_alt),
            VGroup(ay_c, by_c).animate.align_to(formula_c[19], RIGHT),
            FadeOut(VGroup(az_c, bz_c), shift = 0.6*RIGHT),run_time = 2)
        self.wait()
        formula_alt = MathTex(
            '(', 'a', '+', 'b', ')', '(', 'x', '+', 'y', ')',
            '=', 'ax', '+', 'ay', '+', 'bx', '+', 'by').scale_to_fit_height(formula.height).align_to(formula, UL)
        formula_alt[0:10].align_to(formula, UR)
        formula_alt[10].match_x(formula_c[12])
        formula_alt[11].match_x(formula_c[13])
        formula_alt[12].match_x(formula_c[14])
        formula_alt[13].match_x(formula_c[15])
        formula_alt[14].match_x(formula_c[18])
        formula_alt[15].match_x(formula_c[19])
        formula_alt[16].match_x(formula_c[20])
        formula_alt[17].match_x(formula_c[21])
        self.remove(formula_c_alt)
        self.add(formula_alt)
        self.formula_forever = formula_forever = MathTex(
            '(', 'a', '+', 'b', ')', '(', 'x', '+', 'y', ')',
            '=', 'ax', '+', 'ay', '+', 'bx', '+', 'by').scale(1.5).shift(1.5*UP)
        formula_forever[1].set_color('#628E90')
        formula_forever[11][0].set_color('#628E90')
        formula_forever[13][0].set_color('#628E90')
        formula_forever[3].set_color('#B73E3E')
        formula_forever[15][0].set_color('#B73E3E')
        formula_forever[17][0].set_color('#B73E3E')
        self.play(AnimationGroup(
            FadeOut(rect_alt, eq_sign, ax_c, ay_c, bx_c, by_c, scale = 0.85),
            ReplacementTransform(formula_alt, formula_forever),
            lag_ratio=0.2
        ),run_time = 2)
        self.wait()

    def example(self):
        formula_forever = self.formula_forever
        formula_example = MathTex(
            '(', 'x', '^2', '+', '2', 'x', 'y', ')', #7
            '(', '7', 'x', '+', 'y', ')',  #13
            '=', 'x', '^2', '7', 'x', '+', 'x', '^2', 'y', #22
            '+', '2', 'x', 'y', '7', 'x', '+', '2', 'x', 'y', 'y' #33
        ).scale(1.3)
        formula_example.next_to(formula_forever, DOWN)
        self.play(AnimationGroup(
            formula_forever.animate.to_corner(UR).scale(0.7),
            Write(formula_example[:14])
        ))
        self.wait()
        ax_line = ConectionLine(formula_example[1:3], formula_example[9:11], alpha=1/5, color = '#628E90')
        ay_line = ConectionLine(formula_example[1:3], formula_example[12], alpha=1/5, color = '#628E90')
        bx_line = ConectionLine(formula_example[4:7], formula_example[9:11], alpha=1/5, color = '#B73E3E')
        by_line = ConectionLine(formula_example[4:7], formula_example[12], alpha=1/5, color = '#B73E3E')
        self.play(AnimationGroup(
            Create(ax_line),
            Wait(0.2),
            AnimationGroup(
                FadeIn(formula_example[15:17], shift = 0.05*RIGHT, scale = 1.1),
                FadeIn(formula_example[17:19], shift = 0.05*LEFT, scale = 1.1)),
            FadeIn(formula_example[14].set_opacity(0.25), scale = 0.5),
            lag_ratio=0.25
        ), run_time = 3)
        self.wait(0.25)
        self.play(AnimationGroup(
            ReplacementTransform(ax_line, ay_line),
            Wait(0.2),
            AnimationGroup(
                FadeIn(formula_example[20:22], shift = 0.05*RIGHT, scale = 1.1),
                FadeIn(formula_example[22], shift = 0.05*LEFT, scale = 1.1)),
            FadeIn(formula_example[19], scale = 0.5),
            lag_ratio=0.25
        ), run_time = 3)
        self.wait(0.25)
        self.play(Uncreate(ay_line))
        self.play(AnimationGroup(
            Create(bx_line),
            Wait(0.2),
            AnimationGroup(
                FadeIn(formula_example[24:27], shift = 0.05*RIGHT, scale = 1.1),
                FadeIn(formula_example[27:29], shift = 0.05*LEFT, scale = 1.1)),
            FadeIn(formula_example[23].set_opacity(0.5), scale = 0.5),
            lag_ratio=0.25
        ), run_time = 3)
        self.wait(0.25)
        self.play(AnimationGroup(
            ReplacementTransform(bx_line, by_line),
            Wait(0.2),
            AnimationGroup(
                FadeIn(formula_example[30:33], shift = 0.05*RIGHT, scale = 1.1),
                FadeIn(formula_example[33], shift = 0.05*LEFT, scale = 1.1)),
            FadeIn(formula_example[29], scale = 0.5),
            lag_ratio=0.25
        ), run_time = 3)
        self.wait(0.25)
        self.play(
            Uncreate(by_line),
            formula_example[14].animate.set_opacity(1))
        self.wait()
