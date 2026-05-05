"""
Introduction Scenes
9 total
"""
from manim import *

C_BG     = "#0f1117"
config.background_color = C_BG

def sec_title(text: str) -> Tex:
    t = Tex(r"\textbf{" + text + r"}", font_size=40, color=WHITE)
    t.to_edge(UP, buff=0.3)
    return t

# reduction
class Intro0(Scene):
    def construct(self):
        title = sec_title("CS599 Final Project")
        self.play(Write(title), run_time = .8)

        self.wait(2)

        text = MathTex(r"\text{k-SAT} \leq_{fg} \text{Subset Sum}", font_size=50, color=WHITE)
        self.play(Write(text), run_time = .8)

        self.wait(10)

# subset sum def
class Intro1(Scene):
    def construct(self):
        title = sec_title("Subset Sum")
        self.play(Write(title), run_time = .8)
        self.wait(1)

        part1 = Tex(
            r"Given $n$ integers $x_1, x_2, \dots, x_n \in \mathbb{N}$, "
            r"and a target value $T \in \mathbb{N},$",
            font_size=35,
        )

        self.wait(1)

        part2 = Tex(
            r"determine whether there exists a subset of the integers that sums to $T$",
            font_size=35,
        )

        part1.shift(UP * 0.6)
        part2.shift(DOWN * 0.6)

        self.play(Write(part1), run_time=2)
        self.play(Write(part2), run_time=2)

        self.wait(10)

# k-sat def
class Intro2_0(Scene):
    def construct(self):
        title = sec_title("k-SAT")
        self.play(Write(title))

        definition = Tex(
            r"Given a k-CNF formula with n variables and m clauses, determine whether it is satisfiable.",
            font_size=38
        )

        self.play(Write(definition))
        self.wait(10)

# k-cnf def
class Intro2_1(Scene):
    def construct(self):
        title = sec_title("k-CNF formula")
        self.play(Write(title))

        sz = 50
        
        cnf_label = Tex(
                r"conjunction of disjunction of variables",
            font_size=sz
        ).next_to(title, DOWN*2, buff=0.5)
        self.wait(2)
        self.play(Write(cnf_label))
        self.wait(3)

        base = MathTex(
            r"(\text{clause}) \land (\text{clause})",
            font_size=sz
        ).next_to(cnf_label, DOWN*2, buff=0.8)

        self.play(Write(base))
        self.wait(3)

        mid = MathTex(
            r"(x_1 \lor x_3 \lor x_4) \land (x_2 \lor x_1 \lor x_3)",
            font_size=sz
        ).move_to(base)

        self.play(Transform(base, mid))
        self.wait(3)

        full = MathTex(
            r"(x_1 \lor \neg x_3 \lor x_4)\;\land\;(\neg x_2 \lor x_1 \lor x_3)",
            font_size=sz
        ).move_to(base)

        self.play(Transform(base, full))
        self.wait(10)

# k-cnf satisfiability
class Intro2_2(Scene):
    def construct(self):
        title = sec_title("k-SAT Satisfiability")
        self.play(Write(title))

        sz = 44

        sat_line = Tex(
            r"Satisfiability: is there an assignment of variables "
            r"so that the formula evaluates to True?",
            font_size=35
        ).next_to(title, DOWN*1.5, buff=0.5)

        self.play(Write(sat_line))
        self.wait(1)

        formula = MathTex(
            r"(x_1 \lor \neg x_3 \lor x_4)\;\land\;(\neg x_2 \lor x_1 \lor x_3)",
            font_size=sz
        ).move_to(ORIGIN)

        self.play(Write(formula))
        self.wait(10)

        assignments = VGroup(
            Tex(r"$x_1 = \text{False}$", font_size = sz*.8),
            Tex(r"$x_2 = \text{False}$", font_size = sz*.8),
            Tex(r"$x_3 = \text{False}$", font_size = sz*.8),
            Tex(r"$x_4 = \text{False}$", font_size = sz*.8),
        ).arrange(DOWN, aligned_edge=LEFT)

        assignments.to_edge(DOWN).shift(UP*1)

        self.play(Write(assignments))
        self.wait(3)

        step1 = MathTex(
            r"(F \lor \neg F \lor F)\;\land\;(\neg F \lor F \lor F)",
            font_size=sz
        ).move_to(formula)

        self.play(Transform(formula, step1))
        self.wait(3)

        step2 = MathTex(
            r"(F \lor T \lor F)\;\land\;(T \lor F \lor F)",
            font_size=sz
        ).move_to(formula)

        self.play(Transform(formula, step2))
        self.wait(2)

        step3 = MathTex(
            r"(T)\;\land\;(T)",
            font_size=sz
        ).move_to(formula)

        self.play(Transform(formula, step3))
        self.wait(2)

        final = MathTex(
            r"T",
            font_size=sz,
            color=GREEN
        ).move_to(formula)

        self.play(Transform(formula, final))
        self.wait(3)

# surprising connection
class Intro3_0(Scene):
    def construct(self):
        title = sec_title("Reduction?")
        self.play(Write(title))

        text1 = Tex(
            r"Subset Sum and k-SAT seem very different.",
            font_size=32
        ).shift(UP*1.2)

        text2 = Tex(
            r"Subset Sum uses arithmetic logic, while k-SAT uses boolean logic.",
            font_size=32
        ).next_to(text1, DOWN, buff=0.5)

        text3 = Tex(
            r"How can we perform a reduction?",
            font_size=32,
            color=YELLOW
        ).next_to(text2, DOWN, buff=0.6)

        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        self.play(Indicate(text3))
        self.wait(10)

# paper
class Intro3_1(Scene):
    def construct(self):
        title = sec_title("Video Inspiration")
        self.play(Write(title))

        paper = ImageMobject("imgs/paper.png")
        paper.scale(0.9)

        caption = Tex(
            r"\textbf{SETH-Based lower bounds for Subset Sum and Bicriteria Path}",
            font_size=26
        ).next_to(paper, DOWN)

        self.play(FadeIn(paper, shift=LEFT))
        self.play(Write(caption))
        self.wait(10)

# seth
class Intro3_2(Scene):
    def construct(self):
        title = sec_title("Paper's Assumption")
        self.play(Write(title))

        seth = Tex(
            r"\textbf{Strong Exponential Time Hypothesis (SETH)}",
            font_size=34
        ).shift(UP*1.2)

        statement = Tex(
            r"k-SAT cannot be solved in $O(2^{(1-\epsilon)n})$ time "
            r"for any constant $\epsilon > 0$",
            font_size=30
        ).next_to(seth, DOWN, buff=0.5)

        self.play(Write(seth))
        self.play(Write(statement))
        self.wait(3)

        consequence = Tex(
            r"If k-SAT reduces to Subset Sum, then Subset Sum "
            r"cannot be solved in $O(2^{(1-\epsilon)n})$ time under SETH.",
            font_size=30,
            color=YELLOW
        ).next_to(statement, DOWN, buff=0.7)

        self.play(Write(consequence))
        self.wait(10)

class Intro4(Scene):
    def construct(self):
        title = sec_title("Reductions")
        self.play(Write(title))

        ksat = MathTex(r"\text{k-SAT}", font_size=48)
        arrow1 = MathTex(r"\rightarrow", font_size=48)
        csp = MathTex(r"\text{Structured CSP}", font_size=48)
        arrow2 = MathTex(r"\rightarrow", font_size=48)
        subset = MathTex(r"\text{Subset Sum}", font_size=48)

        roadmap = VGroup(ksat, arrow1, csp, arrow2, subset).arrange(RIGHT, buff=0.4)

        self.play(Write(roadmap))
        self.wait(5)

        highlight = SurroundingRectangle(
            VGroup(ksat, arrow1, csp),
            color=YELLOW,
            buff=0.2
        )

        self.play(Create(highlight))
        self.wait(.5)

        self.play(
            highlight.animate.set_color(ORANGE),
            ksat.animate.set_color(YELLOW),
            csp.animate.set_color(YELLOW)
        )

        self.wait(10)
