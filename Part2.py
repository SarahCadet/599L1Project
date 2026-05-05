"""
CSP → Subset Sum Reduction — Manim Animation
=============================================
Tested on Manim Community v0.20.x

Render the full video:
    manim -pql Part2.py CSPToSubsetSum   # fast preview (480p)
    manim -pqh Part2.py CSPToSubsetSum   # high quality (1080p)

Render a single section on its own, e.g.:
    manim -pql csp_to_subset_sum.py Scene03_ItemTypes
"""

from manim import *

# ChatGPT Produced the colors

# ── Colour palette ────────────────────────────────────────────────────────────
C_BG     = "#0f1117"
C_ACCENT = "#4fc3f7"   # light blue  – highlights / titles
C_GOLD   = "#ffd54f"   # gold        – target T / key results
C_GREEN  = "#a5d6a7"   # green       – correct / satisfying
C_RED    = "#ef9a9a"   # red         – wrong / contradiction
C_PURPLE = "#ce93d8"   # purple      – constraint items
C_ORANGE = "#ffb74d"   # orange      – variable items
C_GREY   = "#78909c"   # muted grey  – padding / zero blocks

config.background_color = C_BG


# ─────────────────────────────────────────────────────────────────────────────
# ChatGPT produced: Shared helpers (pure functions, no Scene dependency)
# ─────────────────────────────────────────────────────────────────────────────

def make_block(label: str, width=1.4, height=0.7,
               fill_color=C_GREY, label_color=WHITE, font_size=22) -> VGroup:
    rect = Rectangle(width=width, height=height,
                     fill_color=fill_color, fill_opacity=0.25,
                     stroke_color=fill_color, stroke_width=2)
    tex = Tex(label, font_size=font_size, color=label_color)
    tex.move_to(rect)
    return VGroup(rect, tex)


def make_block_row(labels, colors=None, width=1.4, height=0.7,
                   font_size=22, buff=0.04) -> VGroup:
    if colors is None:
        colors = [C_GREY] * len(labels)
    blocks = [make_block(l, width, height, c, font_size=font_size)
              for l, c in zip(labels, colors)]
    return VGroup(*blocks).arrange(RIGHT, buff=buff)

def labeled_row(prefix, lbls, cols, yshift):
            label = Tex(prefix, font_size=22).shift(LEFT * 4.3 + yshift)
            row = make_block_row(lbls, cols, width=1.6, height=0.65,
                                 font_size=19).shift(RIGHT * 0.5 + yshift)
            return label, row


def sec_title(text: str) -> Tex:
    t = Tex(r"\textbf{" + text + r"}", font_size=34, color=C_ACCENT)
    t.to_edge(UP, buff=0.3)
    return t


# ─────────────────────────────────────────────────────────────────────────────
# Individual standalone scenes (each renderable on its own)
# ─────────────────────────────────────────────────────────────────────────────

class Scene01_CSPRecap(Scene):
    def construct(self):
        title = sec_title("CSP Structure of Instance")
        self.play(Write(title))
        # Box with recap
        box = RoundedRectangle(width=7.5, height=4.5, corner_radius=0.2,
                               stroke_color=C_ACCENT, fill_color=C_ACCENT,
                               fill_opacity=0.06).shift(DOWN * 0.3)
        # One instance of CSP
        psi = Tex(r"CSP Instance $\psi$", font_size=28, color=C_ACCENT)
        #move the label to be right above the box
        psi.next_to(box, UP, buff=0.05)
        #rows within the box
        rows = VGroup(
            Tex(r"$\hat{n} = \lceil n/a \rceil$ variables", font_size=26),
            Tex(r"Variable domain: $[2^a]$", font_size=26),
            Tex(r"$\hat{m} = \hat{n}$ constraints", font_size=26),
            Tex(r"Each variable in $\leq \hat{c}_{k,\varepsilon}\cdot a$ constraints",
                font_size=26, color=C_ORANGE),
            Tex(r"Each constraint uses $\leq \hat{c}_{k,\varepsilon}\cdot a$ variables",
                font_size=26, color=C_PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).move_to(box) # arrange them as a list and set them to be on top of the blue box


        self.play(FadeIn(box), Write(psi))
        self.wait(5)

        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.15), run_time=0.55)
            self.wait(5)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.4)


class Scene02_CoreIdea(Scene):
    def construct(self):
        title = sec_title("Core Idea")
        self.play(Write(title))
        self.wait(4)
        #CSP
        csp_box = RoundedRectangle(width=3, height=1.2, corner_radius=0.15,
                                   stroke_color=C_ORANGE, fill_color=C_ORANGE,
                                   fill_opacity=0.12)
        csp_label = Tex(r"CSP $\psi$", font_size=30, color=C_ORANGE).move_to(csp_box)
        csp = VGroup(csp_box, csp_label).shift(LEFT * 3.5 + UP * 1.5)

        # ->
        arrow = Arrow(LEFT * 1.4, RIGHT * 1.4, color=WHITE, buff=0.1).shift(UP * 1.5)

        # Subset Sum
        ss_box = RoundedRectangle(width=3.6, height=1.2, corner_radius=0.15,
                                  stroke_color=C_ACCENT, fill_color=C_ACCENT,
                                  fill_opacity=0.12)
        ss_label = Tex(r"Subset Sum $(Z,T)$", font_size=26, color=C_ACCENT).move_to(ss_box)
        ss = VGroup(ss_box, ss_label).shift(RIGHT * 3.5 + UP * 1.5)

        #fading in the top
        self.play(FadeIn(csp, shift=LEFT * 0.2))
        self.play(GrowArrow(arrow))
        self.play(FadeIn(ss, shift=RIGHT * 0.2))

        self.wait(12)

        examples = VGroup(
            Tex(r"$x = 8\;\mapsto\;11$", font_size=24, color=C_ORANGE),
            Tex(r"$y = 9\;\mapsto\;12$", font_size=24, color=C_ORANGE),
        ).arrange(RIGHT, buff=1.2).shift(UP * 0.3)

        self.play(FadeIn(examples))
        self.wait(3)

        principles = VGroup(
            Tex(r"Assignments $\longrightarrow$ Numbers", font_size=25, color=C_GREEN),
            Tex(r"Consistency $\longrightarrow$ Addition", font_size=25, color=C_GREEN),
            Tex(r"Subset sums to $T \iff$ CSP satisfiable", font_size=25, color=C_GOLD),
        ).arrange(DOWN, buff=0.38).shift(DOWN * 1.7)

        for p in principles:
            self.play(FadeIn(p, shift=UP * 0.08), run_time=0.6)
            self.wait(3)
    
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.4)


class Scene03_ItemTypes(Scene):
    def construct(self):
        title = sec_title("Integer Item Types")
        self.play(Write(title))
        self.wait(2)

        divider = DashedLine(UP * 2.8, DOWN * 2.8, color=C_GREY, dash_length=0.14)
        self.play(FadeIn(divider))
        self.wait(2)

        var_title = Tex(r"\underline{Variable Items}", font_size=28, color=C_ORANGE)
        var_title.shift(LEFT * 3.3 + UP * 1.8)


        var_notation = Tex(r"$z(x,\,\alpha) \leftarrow$ notation", font_size=24, color=C_ORANGE)
        var_notation.next_to(var_title, DOWN, buff=0.3)


        var_ex = VGroup(
            Tex(r"$z(x_1,4)$: assign $x_1=4$", font_size=21),
            Tex(r"$z(x_1,5)$: assign $x_1=5$", font_size=21),
            Tex(r"$z(x_2,2)$: assign $x_2=2$", font_size=21),
            Tex(r"$z(x_2,3)$: assign $x_2=3$", font_size=21),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22).next_to(var_notation, DOWN, buff=0.6)


        con_title = Tex(r"\underline{Constraint Items}", font_size=28, color=C_PURPLE)
        con_title.shift(RIGHT * 3.0 + UP * 1.8)


        con_notation = Tex(r"$z(c,\,\alpha_1,\alpha_2,\ldots) \leftarrow $ notation", font_size=24, color=C_PURPLE)
        con_notation.next_to(con_title, DOWN, buff=0.3)


        con_ex = VGroup(
            Tex(r"$z(c_1,1,2)$", font_size=21),
            Tex(r"$c_1=(x_1\neq x_2)$", font_size=21, color=C_GREY),
            Tex(r"$z(c_2,5,3)$", font_size=21),
            Tex(r"$c_2=(x_1{=}5\Rightarrow x_2{=}3)$", font_size=21, color=C_GREY),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22).next_to(con_notation, DOWN, buff=0.6)


        self.play(Write(var_title))
        self.wait(2)

        for v in var_ex:
            self.play(FadeIn(v, shift=RIGHT * 0.1),
                      run_time=0.45)
            self.wait(2)

        self.play(Write(con_title))
        self.wait(2)

        for c in con_ex:
            self.play(FadeIn(c, shift=LEFT * 0.1),
                      run_time=0.45)
            self.wait(2)

        self.play(FadeIn(var_notation), FadeIn(con_notation))
        self.wait(4)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.4)


class Scene04_OnePerType(Scene):
    def construct(self):

        title = sec_title("Ensuring One Item Per Type")
        self.play(Write(title))
        self.wait(1)

        var_group = VGroup(
            Tex(r"$x_1 = 4$", font_size=30, color=C_ORANGE),
            Tex(r"$x_1 = 5$", font_size=30, color=C_ORANGE),
        ).arrange(RIGHT, buff=1.5).shift(UP * 1.2)

        con_group = VGroup(
            Tex(r"$c_1 = (1,2)$", font_size=30, color=C_PURPLE),
            Tex(r"$c_1 = (2,1)$", font_size=30, color=C_PURPLE),
        ).arrange(RIGHT, buff=1.5).shift(UP * 0.1)
        
        for v in var_group:
            self.play(FadeIn(v))
            self.wait(0.5)
        
        for c in con_group:
            self.play(FadeIn(c))
            self.wait(0.5)

        self.wait(2)

        def big_cross(mob):
            return VGroup(
                Line(mob.get_corner(UL), mob.get_corner(DR), color=C_RED, stroke_width=5),
                Line(mob.get_corner(UR), mob.get_corner(DL), color=C_RED, stroke_width=5),
            )
        self.play(
            Create(big_cross(var_group[0])), 
            Create(big_cross(var_group[1])),
            Create(big_cross(con_group[0])),
            Create(big_cross(con_group[1])), 
            )
        
        self.wait(2)

        note = Tex(r"Solution must pick \textbf{exactly one} item per type",
                   font_size=25, color=C_GOLD).shift(DOWN * 1.4)
        self.play(Write(note))

        blank_row = make_block_row(["", "", "", ""], font_size=22, width=1.7)
        blank_row.shift(DOWN * 2.6)

        for blk in blank_row:
            self.play(FadeIn(blk), run_time=0.2)
            self.wait(0.5)

        self.wait(3)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.4)


class Scene05_Blocks(Scene):
    def construct(self):

        title = sec_title("Block 1 — Item Count")
        self.play(Write(title))
        self.wait(1)

        init_colors = [C_GREY] * 4

        
        
        vi_label, vi_row = labeled_row(r"Variable item:",   ["—","—","—","—"], init_colors, UP*1.1)
        ci_label, ci_row = labeled_row(r"Constraint item:", ["—","—","—","—"], init_colors, UP*0.1)
        T_label,  T_row  = labeled_row(r"Target $T$:",      ["—","—","—","—"], init_colors, DOWN*0.9)

        self.play(FadeIn(VGroup(vi_label, vi_row)), FadeIn(VGroup(ci_label, ci_row)))
        self.play(FadeIn(VGroup(T_label, T_row)))

        self.wait(1)

        brace = Brace(vi_row[0], UP, color=WHITE)
        brace_label = brace.get_tex(r"O(\log n)  \text{ bits}").set_font_size(19)
        
        self.play(FadeIn(brace))
        self.wait(0.1)
        self.play(Write(brace_label))


        #filled in boxes
        vi_filled = make_block(r"1", width=1.6, height=0.65, 
                               fill_color=C_ACCENT, label_color=C_ACCENT, font_size=19)
        ci_filled = make_block(r"1", width=1.6, height=0.65, 
                               fill_color=C_ACCENT, label_color=C_ACCENT, font_size=19)
        T_filled = make_block(r"$\hat n{+}\hat m$", width=1.6, height=0.65,
                              fill_color=C_GOLD, label_color=C_GOLD, font_size=19)
        
        vi_filled.move_to(vi_row[0])
        ci_filled.move_to(ci_row[0])
        T_filled.move_to(T_row[0])


        self.play(Transform(vi_row[0], vi_filled))
        self.play(Transform(ci_row[0], ci_filled))

        self.wait(1)

        self.play(Transform(T_row[0], T_filled))

        

        note = Tex(r"Only summing $\hat n{+}\hat m$ items of count $1$ hits $\hat n{+}\hat m$ exactly",
                   font_size=22, color=C_GREEN).shift(DOWN * 2.8)
        self.play(Write(note))
        self.wait(2)



        #block 2

        block_two_title = sec_title("Block 2 — Padding")
        
        self.play(
            FadeOut(note), 
            FadeOut(brace), 
            FadeOut(brace_label),
            Transform(title, block_two_title)
        )
        self.wait(1)
        
        vi_b2 = make_block("0", width=1.6, height=0.65, fill_color=C_ACCENT, font_size=19).move_to(vi_row[1])
        ci_b2 = make_block("0", width=1.6, height=0.65, fill_color=C_ACCENT, font_size=19).move_to(ci_row[1])
        T_b2  = make_block("0", width=1.6, height=0.65, fill_color=C_GOLD, font_size=19).move_to(T_row[1])
        
        brace = Brace(vi_row[1], UP, color=WHITE)
        brace_label = brace.get_tex(r"O(\log n)  \text{ bits}").set_font_size(19)
        
        self.play(FadeIn(brace))
        self.wait(0.1)
        self.play(Write(brace_label))
        
        note2 = Tex(r"Zero-padding prevents carry overflow\\from block 3 into block 1",
                   font_size=23, color=C_GREY).shift(DOWN * 2.6)
        self.play(
            Write(note2)      
            )
        
        self.wait(2)

        self.play(
            Transform(vi_row[1], vi_b2),
            Transform(ci_row[1], ci_b2),
            Transform(T_row[1], T_b2)
        )
        self.wait(3)
        #destroying block 2 stuff

        block_three_title = sec_title("Block 3 — Type Bits")
        self.play(
            FadeOut(brace),
            FadeOut(brace_label),
            FadeOut(note2), 
            Transform(title, block_three_title)
        )
        self.wait(2)

        #block 3
        vi_b3 = make_block("[0]*n", width=1.6, height=0.65, fill_color=C_GREY, font_size=19).move_to(vi_row[2])
        ci_b3 = make_block("[0]*n", width=1.6, height=0.65, fill_color=C_GREY, font_size=19).move_to(ci_row[2])
        T_b3  = make_block("[0]*n", width=1.6, height=0.65, fill_color=C_GREY, font_size=19).move_to(T_row[2])

        self.play(
            Transform(vi_row[2], vi_b3),
            Transform(ci_row[2], ci_b3),
            Transform(T_row[2], T_b3)
        )
        brace = Brace(vi_row[2], UP, color=WHITE)
        brace_label = brace.get_tex(r"\hat n + \hat m  \text{ bits}").set_font_size(19)
        
        self.play(FadeIn(brace))
        self.wait(0.1)
        self.play(Write(brace_label))
        self.wait(4)

        vi_b3 = make_block("1[0]*(n-1)", width=1.6, height=0.65, fill_color=C_ACCENT, font_size=19).move_to(vi_row[2])
        ci_b3 = make_block("01[0]*(n-2)", width=1.6, height=0.65, fill_color=C_ACCENT, font_size=19).move_to(ci_row[2])
        T_b3  = make_block("[1]*n", width=1.6, height=0.65, fill_color=C_GOLD, font_size=19).move_to(T_row[2])


        note3 = Tex(
            r"One-hot per item $+$ all-ones target\\$\Rightarrow$ exactly one item of each type",
            font_size=22, color=C_GREEN).shift(DOWN * 2.5)
        self.play(Write(note3))
        self.wait(2)


        self.play(
            Transform(vi_row[2], vi_b3),
            Transform(ci_row[2], ci_b3),
            Transform(T_row[2], T_b3)
        )
        self.wait(5)
        #block 4

        block_four_title = sec_title("Block 4 — More Padding!")
        self.play(
            FadeOut(brace),
            FadeOut(brace_label),
            FadeOut(note3), 
            Transform(title, block_four_title)
        )


        brace = Brace(vi_row[3], UP, color=WHITE)
        brace_label = brace.get_tex(r"O(\log n)  \text{ bits}").set_font_size(19)
        
        self.play(FadeIn(brace))
        self.wait(0.1)
        self.play(Write(brace_label))
        self.wait(2)

        vi_b4 = make_block("0", width=1.6, height=0.65, fill_color=C_ACCENT, font_size=19).move_to(vi_row[3])
        ci_b4 = make_block("0", width=1.6, height=0.65, fill_color=C_ACCENT, font_size=19).move_to(ci_row[3])
        T_b4  = make_block("0", width=1.6, height=0.65, fill_color=C_GOLD, font_size=19).move_to(T_row[3])


        self.play(
            Transform(vi_row[3], vi_b4),
            Transform(ci_row[3], ci_b4),
            Transform(T_row[3], T_b4)
        )
        self.wait(10)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.4)



class Scene06_VariableBlocks(Scene):
    def construct(self):

        title = sec_title("Variable Blocks -- Enforcing Consistency")
        self.play(Write(title))
        self.wait(1)

        block_names  = ["count", r"pad$_1$", "type", r"pad$_2$",
                  r"var$_1$", r"var$_2$", r"$\cdots$", r"var$_{\hat n}$"]
        
        colors = [C_ACCENT, C_GREY, C_GREEN, C_GREY,
                  C_ORANGE, C_ORANGE, C_GREY, C_ORANGE]
        
        row = make_block_row(block_names, colors, width=1.22, height=0.62,
                             font_size=15, buff=0.04).shift(UP * 2.2)
        
        self.play(FadeIn(row, shift=UP * 0.15))
        self.wait(2)

        brace = Brace(VGroup(*row[4:]), DOWN, color=C_ORANGE)
        brace_label = brace.get_tex(r"\hat n\ \text{variable blocks}").set_font_size(20)
        self.play(FadeIn(brace), Write(brace_label))
        self.wait(3)


        Q_def = Tex(r"$Q$ = target value for each variable block in $T$",
                    font_size=25, color=C_GOLD).shift(UP * 0.25)
        self.play(Write(Q_def))
        self.wait(6)


        rule_1 = Tex(
            r"Variable item $z(x,\alpha)$: block for $x$ $=$ $Q - d(x)\cdot \alpha$",
            font_size=21, color=C_ORANGE
        )

        rule_2 = Tex(
            r"d(x) = \# constraints has x \quad | \quad $\alpha$ = assigned value",
            font_size=21, color=C_ORANGE
        )

        rule_3 = Tex(
            r"Constraint item using $x$ with $\alpha_i$: block $=$ $\alpha_i$",
            font_size=21, color=C_ORANGE
        )

        rule_4 = Tex(
            r"Constraint item not using $x$: block $= 0$",
            font_size=21, color=C_ORANGE
        )

        left_col = VGroup(rule_1, rule_2).arrange(
            DOWN, aligned_edge=LEFT, buff=0.35
        )

        right_col = VGroup(rule_3, rule_4).arrange(
            DOWN, aligned_edge=LEFT, buff=0.35
        )


        rules = VGroup(left_col, right_col).arrange(
            RIGHT, buff=1.2, aligned_edge=UP
        ).shift(DOWN * 1.2)


        for r in rules:
            self.play(FadeIn(r, shift=RIGHT * 0.1), run_time=0.65)
            self.wait(11)
        
        sum_eq = MathTex(
            r"\text{Block sum} = Q - d(x)\cdot \alpha) + \sum_{i=1}^{d(x)} \alpha_i",
            font_size=24, color=C_GREEN).shift(DOWN * 2.5)
        
        self.play(Write(sum_eq))
        self.wait(5)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.4)


class Scene07_AverageFree(Scene):
    def construct(self):

        title = sec_title(r"$k$-Average-Free Sets \& Consistency")
        self.play(Write(title))
        self.wait(1)

        sum_eq = MathTex(
            r"\text{Block sum} = Q - d(x)\cdot \alpha + \sum_{i=1}^{d(x)} \alpha_i",
            font_size=30, color=C_GREEN).shift(UP * 2.2)
        self.play(Write(sum_eq))
        self.wait(4)

        equals = MathTex(
            r"d(x)\cdot \alpha = \sum_{i=1}^{d(x)} \alpha_i",
            font_size=35, color=C_GOLD).shift(UP * 2.2)
        
        self.play(Transform(sum_eq, equals))
        self.wait(5)
        

        arrow_lbl = Tex(r"$\Downarrow$ $\lambda$-average-free property",
                        font_size=33, color=C_GREY).next_to(equals, DOWN, buff=1)
        
        
        self.play(FadeIn(arrow_lbl, shift=DOWN * 0.2))
        self.wait(3)


        definition = Tex(
            r"A set $S$ is \textbf{$k$-average-free} if no $k$ elements of $S$\\have "
            r"an average also in $S$, unless all $k$ values are equal.",
            font_size=28).next_to(arrow_lbl, DOWN, buff=1)
        
        self.play(Write(definition))
        self.wait(6)

        
        lam = Tex(r"$\lambda = \hat{c}_{k,\varepsilon}\cdot a$ = max constraints per variable",
                  font_size=23, color=C_PURPLE).next_to(definition, DOWN, buff=0.8)
        f_map = Tex(r"$f:[2^a]\to S$ maps assignments into a $\lambda$-average-free set",
                    font_size=22, color=C_PURPLE).next_to(lam, DOWN, buff=0.2)
        

        self.play(Write(lam))
        self.wait(8)
        self.play(Write(f_map))
        self.wait(8) 

        ## now we can rewrite the formula as :
        sum_eq_w_f = MathTex(
            r"d(x)\cdot f(\alpha) = \sum_{i=1}^{d(x)} f(\alpha_i)",
            font_size=30, color=C_GREEN).shift(UP * 2.2)
        self.play(Transform(sum_eq, sum_eq_w_f))
        self.wait(7)
                
        result = Tex(r"$f(\alpha_i) = f(\alpha)$ for all $i$ -- \textbf{consistency!}",
                     font_size=28, color=C_GREEN).next_to(arrow_lbl, DOWN, buff=1)
        
        self.play(Transform(definition, result))
        self.wait(5)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.4)


class Scene08_QAndBlockSize(Scene):
    def construct(self):
        title = sec_title(r"Choosing $Q$ and Block Size")
        self.play(Write(title))
        self.wait(1)

        B_def = Tex(
            r"Lemma 3.2: $\lambda$-average-free set of size $2^a$ has max value\\$B = "
            r"\lambda^{c/\varepsilon}(2^a)^{1+\varepsilon}$",
            font_size=25, color=WHITE).shift(UP * 2.0)
        self.play(Write(B_def))
        self.wait(12)

        q_steps = VGroup(
            Tex(r"Block values must stay $\geq 0$", font_size=25, color=C_PURPLE),
            MathTex(r"\max\bigl(d(x)\cdot f(\alpha)\bigr) = \lambda B",
                    font_size=25, color=C_PURPLE),
            MathTex(r"Q = \lambda B", font_size=30, color=C_GOLD),
        ).arrange(DOWN, buff=0.38).shift(UP * 0.2)
        for s in q_steps:
            self.play(FadeIn(s, shift=RIGHT * 0.1), run_time=0.6)
            self.wait(9)

        self.wait(2)
        bs_steps = VGroup(
            Tex(r"Max block value $= Q + \lambda B = 2\lambda B$",
                font_size=25, color=C_PURPLE),
            Tex(r"Block Range: $[0,2\lambda B]$", font_size=30, color=C_GOLD),
            MathTex(r"\text{Block size} = \lceil\log(2\lambda B+1)\rceil \text{ bits}",
                    font_size=30, color=C_GOLD),
        ).arrange(DOWN, buff=0.35).shift(DOWN * 1.9)
        
        for s in bs_steps:
            self.play(FadeIn(s, shift=RIGHT * 0.1), run_time=0.65)
            self.wait(8)
        self.wait(4)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.4)


class Scene09_CorrectnessAndComplexity(Scene):
    def construct(self):
        title = sec_title(r"Correctness \& Complexity")
        self.play(Write(title))
        self.wait(5)


        checks = VGroup(
            Tex(r"$\checkmark$ \ Exactly one assignment per variable",
                font_size=25, color=C_GREEN),
            Tex(r"$\checkmark$ \ Exactly one satisfying assignment per clause",
                font_size=25, color=C_GREEN),
            Tex(r"$\checkmark$ \ Global consistency across all items",
                font_size=25, color=C_GREEN),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.38).shift(UP * 1.7)

        for check in checks:
            self.play(FadeIn(check, shift=RIGHT * 0.12), run_time=0.6)
            self.wait(2.5)

        equiv = Tex(r"CSP $\psi \rightarrow$ Subset Sum",
                    font_size=25, color=C_GOLD).shift(UP * 0.3)
        self.play(Write(equiv))
        self.wait(3)

        comp_box = RoundedRectangle(width=9.5, height=3.5, corner_radius=0.2,
                                    stroke_color=C_ACCENT, fill_color=C_ACCENT,
                                    fill_opacity=0.06).shift(DOWN * 2.2)
        comp_title = Tex(r"Time Complexity", font_size=22, color=C_ACCENT)
        comp_title.next_to(comp_box, UP, buff=0.05)
        self.play(FadeIn(comp_box), Write(comp_title))
        self.wait(0.6)

        
        comp_lines = VGroup(
            MathTex(r"\log T = O(\log \hat n)+(\hat n+\hat m)+\hat n(\log B+\log\lambda+O(1))",
                    font_size=19),
            MathTex(r"\leq (1+2\varepsilon)\,n \text{ bits}", font_size=21, color=C_GREEN),
            MathTex(r"\#\text{Variable items} = \hat{n}\cdot 2^a \leq n\cdot 2^a",
                    font_size=19, color=C_PURPLE),
            MathTex(r"\#\text{Constraint items} = \hat{m}\cdot 2^a \leq n\cdot 2^{a\lambda}",
                    font_size=19, color=C_PURPLE),
            MathTex(r"\text{Total over }2^{\varepsilon n}\text{ instances} = "
                    r"\mathrm{poly}(n)\cdot 2^{\varepsilon n}",
                    font_size=21, color=C_GOLD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(comp_box)

        

        for line in comp_lines:
            self.play(FadeIn(line, shift=RIGHT * 0.08), run_time=0.45)
            self.wait(5)

        
        
        self.wait(5)

        equiv2 = Tex(r"K-SAT $\rightarrow$ Subset Sum",
                    font_size=25, color=C_GOLD).shift(UP * 0.3)
        self.play(Transform(equiv, equiv2))
        self.wait(12)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.4)


