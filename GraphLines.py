from manim import *

class GraphLines(Scene):

    def construct(self):

        axes = Axes(
            x_range=[-8, 8, 1],
            y_range=[-8, 8, 1],
            x_length=8,
            y_length=8,
            axis_config={"include_numbers": True},
        )

        labels = axes.get_axis_labels(x_label="x", y_label="y")

        self.play(Create(axes), Write(labels))
        self.wait(1)

        line_y1 = axes.plot(
            lambda x: 1,
            color=GREEN
        )

        line_x1 = Line(
            axes.c2p(1, -5),
            axes.c2p(1, 5),
            color=RED
        )

        line_x5 = Line(
            axes.c2p(5, -5),
            axes.c2p(5, 5),
            color=BLUE
        )

        label_x1 = MathTex("x=1").next_to(line_x1, UP)
        label_x5 = MathTex("x=5").next_to(line_x5, UP)
        label_y1 = MathTex("y=1").next_to(line_y1, RIGHT)

        self.play(Create(line_x1), Write(label_x1))
        self.wait()

        self.play(Create(line_y1), Write(label_y1))
        self.wait()

        self.play(Create(line_x5), Write(label_x5))
        self.wait(2)

#GraphLines()