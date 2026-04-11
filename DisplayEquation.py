from manim import *

class DisplayEquation(Scene):
    def construct(self) -> None:
        equation = MathTex(r"(x + 1)(x + 2)^2")

        self.play(Write(equation))
        self.wait(2)