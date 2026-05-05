"""
Reduction 1 Scenes
"""
from manim import *

C_BG     = "#0f1117"
config.background_color = C_BG

def sec_title(text: str) -> Tex:
    t = Tex(r"\textbf{" + text + r"}", font_size=40, color=WHITE)
    t.to_edge(UP, buff=0.3)
    return t

# CSP definition
class R0_0(Scene):
    def construct(self):
        title = sec_title("What is a Constraint Satisfaction Problem (CSP)?")
        self.play(Write(title))
        self.wait(2)

        b1 = Tex(r"- Variables $x_1, x_2, \dots, x_n$", font_size=40)
        b2 = Tex(r"- Each variable has a domain (e.g. $\mathbb{Z}$ or $\{\text{Sarah}, \text{Manny}\}$)", font_size=40)
        b3 = Tex(r"- Constraints on variables", font_size=40)

        definition = VGroup(b1, b2, b3).arrange(
            DOWN, aligned_edge=LEFT, buff=0.3
        ).next_to(title, DOWN, buff=0.7).to_edge(LEFT, buff=1)

        self.play(Write(b1), run_time = .8)
        self.wait(2)

        self.play(Write(b2))
        self.wait(2)

        self.play(Write(b3))
        self.wait(2)

        question = Tex(
            r"Can we assign values from the domain to our variables to satisfy all constraints?",
            font_size=40,
            color=YELLOW
        ).move_to(DOWN  * 0.5)

        self.play(Write(question))
        self.wait(10)

# CSP example
class R0_1(Scene):
    def construct(self):
        title = sec_title("CSP Example")
        self.play(Write(title))
        self.wait(0.5)

        variables = MathTex(
            r"\text{Variables: } x \in \mathbb{Z}, \quad y \in \mathbb{Z}",
            font_size=34
        ).next_to(title, DOWN, buff=0.8)

        self.play(Write(variables), run_time = .8)
        self.wait(2)

        constraint = MathTex(
            r"\text{Constraint: } x + y = 5",
            font_size=34
        ).next_to(variables, DOWN, buff=0.5)

        self.play(Write(constraint), run_time = .8)
        self.wait(3)

        solution = Tex(
            r"Satisfiable! One assignment that satisfies is $x = 1,\; y = 4$ satisfies the constraint",
            font_size=32,
            color=GREEN
        ).next_to(constraint, DOWN, buff=0.8)

        self.play(Write(solution))
        self.wait(10)

# High Level Overview
class R1(Scene):
    def construct(self):
        title = sec_title("High-Level Overview")
        self.play(Write(title))
        self.wait(0.5)

        ksat_box = Rectangle(width=3.5, height=2.2, color=GREEN)
        ksat_label = Tex(r"k-SAT", font_size=42)

        ksat = VGroup(ksat_box, ksat_label)
        ksat_label.move_to(ksat_box.get_center())
        ksat.move_to(LEFT * 3)

        self.play(FadeIn(ksat))
        self.wait(0.5)

        phi_1 = Tex(r"$\phi_1$", font_size=34)
        phi_2 = Tex(r"$\phi_2$", font_size=34)
        dots = Tex(r"$\vdots$", font_size=40)
        phi_l = Tex(r"$\phi_\ell$", font_size=34)

        phi_group = VGroup(phi_1, phi_2, dots, phi_l).arrange(
            DOWN, buff=0.9
        )

        boxes = VGroup(*[
            SurroundingRectangle(m, buff=0.25)
            for m in phi_group
        ])

        phi_block = VGroup(boxes, phi_group)
        phi_block.next_to(ksat, RIGHT, buff=1.5)

        arrows = VGroup(
            Arrow(ksat.get_right(), phi_1.get_left(), buff=0.1),
            Arrow(ksat.get_right(), phi_2.get_left(), buff=0.1),
            Arrow(ksat.get_right(), dots.get_left(), buff=0.1),
            Arrow(ksat.get_right(), phi_l.get_left(), buff=0.1),
        )

        self.play(
            LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.15),
            LaggedStart(*[FadeIn(m) for m in phi_group], lag_ratio=0.2),
            LaggedStart(*[Create(b) for b in boxes], lag_ratio=0.2),
        )

        self.wait(3)

        self.play(
            ksat.animate.set_color(GREY),
            phi_group.animate.set_color(YELLOW)
        )

        self.wait(10)

# Sparsification Lemma
class R2(Scene):
    def construct(self):
        title = sec_title("Sparsification Lemma")
        self.play(Write(title))
        self.wait(0.5)

        definition = Tex(
            r"We can rewrite any $k$-SAT formula as a disjunction of at most $2^{\varepsilon n}$ sparse $k$-SAT formulas.",
            font_size=30
        ).next_to(title, DOWN, buff=0.8)

        meaning = Tex(
            r"Sparse: each variable appears at most $c_{k,\varepsilon}$ times.",
            font_size=30,
            color=YELLOW
        ).next_to(definition, DOWN, buff=0.4)

        runtime = Tex(
            r"Transformation runs in $\mathrm{poly}(n)\,2^{\varepsilon n}$ time, where $\varepsilon$ is a small constant representing exponential overhead.",
            font_size=30
        ).next_to(meaning, DOWN, buff=0.4)

        self.play(Write(definition))
        self.wait(1)

        self.play(Write(meaning))
        self.wait(1)

        self.play(Write(runtime))
        self.wait(2)

        self.play(FadeOut(meaning), FadeOut(runtime))
        self.wait(0.5)

        cnf1 = MathTex(
            r"(x_1 \lor \neg x_3 \lor x_4)",
            r"\land",
            r"(\neg x_2 \lor x_1 \lor x_3)",
            font_size=36
        )

        arrow = MathTex(r"\rightarrow", font_size=40)

        cnf2 = MathTex(
            r"(x_1)",
            r"\lor",
            r"\Big((\neg x_3 \lor x_4) \land (\neg x_2 \lor x_3)\Big)",
            font_size=36
        )

        group = VGroup(cnf1, arrow, cnf2).arrange(RIGHT, buff=0.6)
        group.move_to(ORIGIN)

        self.play(Write(cnf1))
        self.wait(0.5)

        self.play(Write(arrow))
        self.wait(0.5)

        self.play(Write(cnf2))
        self.wait(0.5)

        cnf2_parts = cnf2.submobjects  

        left = cnf2_parts[0]
        mid = cnf2_parts[1]
        right = cnf2_parts[2]

        self.play(
            left.animate.set_color(BLUE),
            right.animate.set_color(BLUE)
        )
        self.wait(1)

        self.play(mid.animate.set_color(YELLOW))
        self.wait(10)

# Conjunction
class R3(Scene):
    def construct(self):
        # ── k-SAT box ─────────────────────
        ksat_box = Rectangle(width=3.2, height=2, color=WHITE)
        ksat_label = Tex(r"k-SAT", font_size=40)

        ksat = VGroup(ksat_box, ksat_label)
        ksat_label.move_to(ksat_box.get_center())
        ksat.move_to(LEFT * 3 + DOWN * 0.6)

        def make_phi(name):
            label = Tex(name, font_size=34)
            box = SurroundingRectangle(label, buff=0.33, color=BLUE)
            return VGroup(box, label)

        phi_1 = make_phi(r"$\phi_1$")
        phi_2 = make_phi(r"$\phi_2$")
        phi_l = make_phi(r"$\phi_\ell$")

        dots = Tex(r"$\vdots$", font_size=42)

        or1 = Tex(r"$\vee$", font_size=40)
        or2 = Tex(r"$\vee$", font_size=40)

        phi_col = VGroup(
            phi_1,
            or1,
            phi_2,
            dots,
            or2,
            phi_l
        ).arrange(DOWN, buff=0.55)

        phi_col.move_to(RIGHT * 3 + DOWN * 0.6)

        phi_label = Tex(
            r"Each $\phi_i$ is a CSP that corresponds to a sparse CNF instance",
            font_size=28
        ).next_to(phi_col, UP, buff=0.6)

        arrows = VGroup(
            Arrow(ksat.get_right(), phi_1[0].get_left(), buff=0.1),
            Arrow(ksat.get_right(), phi_2[0].get_left(), buff=0.1),
            Arrow(ksat.get_right(), phi_l[0].get_left(), buff=0.1),
        )

        self.play(FadeIn(ksat), FadeIn(phi_col), FadeIn(arrows))
        self.play(Write(phi_label))
        self.wait(5)

        self.play(ksat.animate.set_color(GREEN))
        self.wait(0.3)
        self.play(phi_2.animate.set_color(GREEN))
        self.play(phi_1.animate.set_color(RED))
        self.play(phi_l.animate.set_color(RED))
        self.wait(5)

        self.play(
            ksat.animate.set_color(WHITE),
            phi_col.animate.set_color(WHITE),
            arrows.animate.set_color(WHITE)
        )
        self.wait(3)

        self.play(ksat.animate.set_color(RED))
        self.play(
            phi_col.animate.set_color(RED),
            arrows.animate.set_color(RED)
        )
        self.wait(10)

# transition
class R3_5(Scene):
    def construct(self):
        # ── φ box ─────────────────────────
        phi_box = SurroundingRectangle(
            Tex(r"$\phi_i$", font_size=40),
            buff=0.5
        )
        phi_label = Tex(r"$\phi_i$", font_size=40).move_to(phi_box)

        phi = VGroup(phi_box, phi_label)
        phi.scale(1.5)

        self.play(FadeIn(phi))
        self.wait(10)

# Phi Details
class R4(Scene):
    def construct(self):
        title = sec_title(r"$\phi_i$ Details")
        self.play(Write(title))
        self.wait(0.6)

        main = Tex(
            r"Reminder: Each $\phi_i$ is a CSP instance corresponding to a sparse k-SAT formula",
            font_size=34
        ).next_to(title, DOWN, buff=0.8)

        self.play(Write(main))
        self.wait(3)

        transition = Tex(
            r"CSP variables: \textbf{supervariables} that represent blocks of size a of k-SAT boolean variables",
            font_size=30,
        ).next_to(main, DOWN, buff=0.6)

        self.play(Write(transition))
        self.wait(5)

        xs = VGroup(*[
            Tex(rf"$x_{i}$", font_size=28)
            for i in range(1, 10)
        ]).arrange(RIGHT, buff=0.25).shift(UP * 0.3)

        self.play(FadeIn(xs))
        self.wait(5)

        y1 = VGroup(xs[0], xs[1], xs[2])
        y2 = VGroup(xs[3], xs[4], xs[5])
        y3 = VGroup(xs[6], xs[7], xs[8])

        b1 = SurroundingRectangle(y1, color=BLUE, buff=0.15)
        b2 = SurroundingRectangle(y2, color=GREEN, buff=0.15)
        b3 = SurroundingRectangle(y3, color=RED, buff=0.15)

        labels = VGroup(
            Tex(r"$y_1$", color=BLUE),
            Tex(r"$y_2$", color=GREEN),
            Tex(r"$y_3$", color=RED),
        ).arrange(RIGHT, buff=2).shift(DOWN * 0.6)

        self.play(Create(b1), Create(b2), Create(b3))
        self.play(Write(labels))
        self.wait(5)

        final = Tex(
            r"Supervariable $y_2$ corresponds to $x_4, x_5, x_6$",
            font_size=30,
            color=GREEN
        )
        final.next_to(labels, DOWN, buff=0.6)

        self.play(Write(final))
        self.wait(5)

        extra = Tex(
            r"Each CSP will have $\hat{n} = \lceil n/a \rceil$ variables.",
            font_size=28
        )

        extra.next_to(final, DOWN, buff=0.4)

        self.play(Write(extra))
        self.wait(5)

        extra2 = Tex(
            r"The domain of each variable is a bit string of size $a$. So $|D| = 2^a$",
            font_size=28
        )

        extra2.next_to(extra, DOWN, buff=0.4)

        self.play(Write(extra2))
        self.wait(10)


