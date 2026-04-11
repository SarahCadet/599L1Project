from manim import *

from manim import *

class DrawShapes(Scene):
    def construct(self):

        square = Square(color=GREY)
        triangle = Triangle(color=GOLD)

        circle = Circle(radius=1, color=WHITE)
        circle.to_corner(UR)

        self.play(FadeIn(square))
        self.play(FadeIn(triangle))
        
        self.wait(2)

        self.play(
            Rotate(square, angle=80.7 * DEGREES),
            Rotate(triangle, angle=-80.7 * DEGREES),
            run_time=2
        )
        self.wait(2)

        self.play(
            Transform(square, circle),
            run_time=2
        )

        self.wait(2)

        