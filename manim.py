from manim import *
import numpy as np

config.background_color = BLACK
FONT = "EB Garamond"

def add_shadow(mobject, offset=0.05, shadow_color=GRAY):
    shadow = mobject.copy().set_color(shadow_color).shift(DOWN*offset + RIGHT*offset)
    return VGroup(shadow, mobject)

class TrinityMathScene(ThreeDScene):
    def show_verse(self, text, reference, duration=4):
        verse = Text(f"\"{text}\"", font=FONT, color=WHITE).scale(0.6).to_edge(DOWN)
        ref = Text(f"- {reference}", font=FONT, color=GRAY_A).scale(0.4).next_to(verse, DOWN)

        self.play(FadeIn(verse, shift=UP*0.5), FadeIn(ref, shift=UP*0.5))
        self.wait(duration)
        self.play(FadeOut(verse, shift=DOWN*0.5), FadeOut(ref, shift=DOWN*0.5))

    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        title = Text("Tanrı Birdir", font=FONT, color=WHITE).scale(1.8)
        title_with_shadow = add_shadow(title)
        self.play(Write(title_with_shadow))
        self.wait(1.5)
        self.play(FadeOut(title_with_shadow, shift=DOWN*0.5))

        self.show_verse("Ey İsrail, dinle: Tanrımız RAB, tek RAB'dir!", "Yasa 6:4")

        eq1 = MathTex(r"\text{Tanrı} = \text{Baba} = \text{Oğul} = \text{Kutsal Ruh}", color=WHITE).scale(1.2)
        eq1.set_glow(0.8)
        self.play(Write(eq1))
        self.wait(2)

        self.move_camera(phi=65 * DEGREES, theta=75 * DEGREES, run_time=3, rate_func=smooth)

        neq1 = MathTex(
            r"\text{Baba} \neq \text{Oğul},\quad \text{Oğul} \neq \text{Ruh},\quad \text{Ruh} \neq \text{Baba}",
            color=GRAY_A
        ).scale(0.8).next_to(eq1, DOWN, buff=0.5)
        self.play(Write(neq1))
        self.wait(3)

        self.play(
            ReplacementTransform(eq1, neq1.copy().set_color(WHITE).scale(1.2).move_to(eq1.get_center())),
            FadeOut(neq1)
        )
        self.play(FadeOut(neq1))

        set_eq = MathTex(
            r"\text{Tanrı} = \{ \text{Baba}, \text{Oğul}, \text{Kutsal Ruh} \}", color=WHITE
        ).scale(1.1)
        set_eq.set_glow(0.6)

        self.play(ReplacementTransform(neq1.copy(), set_eq))
        self.wait(2)

        self.show_verse(
            "Gökte tanıklık eden üç kişi var: Baba, Söz ve Kutsal Ruh. Ve bu üçü birdir.",
            "1. Yuhanna 5:7"
        )
        self.play(FadeOut(set_eq))

        ousia = MathTex(
            r"|\text{Ousia}| = 1,\quad |\text{Hipostaz}| = 3", color=BLUE_B
        ).scale(1.1)
        ousia.set_glow(0.7)

        self.play(FadeIn(ousia, shift=UP*0.3))
        self.wait(2)
        self.play(FadeOut(ousia, shift=DOWN*0.3))

        math_model = MathTex(
            r"T(x) = f_1(x) + f_2(x) + f_3(x), \quad T=\text{Tanrı},\ f_i=\text{Kişiler}", color=YELLOW
        ).scale(0.9)
        math_model.set_glow(0.7)

        self.play(FadeIn(math_model, shift=UP*0.3))
        self.wait(3)
        self.play(FadeOut(math_model, shift=DOWN*0.3))

        axes3d = ThreeDAxes(x_range=[-3, 3], y_range=[-3, 3], z_range=[-3, 3])
        v1 = Vector([2, 0, 0], color=BLUE)
        v2 = Vector([-1, 1.5, 1], color=RED)
        v3 = Vector([-1, -1.5, -1], color=GREEN)
        sum_text = Text("v₁ + v₂ + v₃ = TANRI", font=FONT, color=YELLOW).scale(0.6).to_edge(DOWN)

        self.play(Create(axes3d))
        self.play(GrowArrow(v1), GrowArrow(v2), GrowArrow(v3))
        self.play(Write(sum_text))
        self.wait(3)

        self.move_camera(phi=45 * DEGREES, theta=135 * DEGREES, run_time=4, rate_func=smooth)

        self.play(FadeOut(axes3d), FadeOut(v1), FadeOut(v2), FadeOut(v3), FadeOut(sum_text))

        euler = MathTex(r"e^{ix} = \cos x + i \sin x \Rightarrow |e^{ix}| = 1", color=WHITE)
        note = Text("Üç bileşenli ama tek öz.", font=FONT, color=GRAY_A).scale(0.6).next_to(euler, DOWN)
        euler.set_glow(0.6)

        self.play(FadeIn(euler, shift=UP*0.3))
        self.play(FadeIn(note, shift=UP*0.2))
        self.wait(3)
        self.play(FadeOut(euler, shift=DOWN*0.3), FadeOut(note, shift=DOWN*0.3))

        god = Text("TANRI", font=FONT, color=YELLOW).move_to([0, 2, 0])
        father = Text("BABA", font=FONT, color=BLUE).move_to([-2, -1, 1])
        son = Text("OĞUL", font=FONT, color=RED).move_to([2, -1, -1])
        spirit = Text("KUTSAL RUH", font=FONT, color=GREEN).move_to([0, -2, 0])

        links = [
            Line(god.get_center(), father.get_center(), color=YELLOW),
            Line(god.get_center(), son.get_center(), color=YELLOW),
            Line(god.get_center(), spirit.get_center(), color=YELLOW),
            Line(father.get_center(), son.get_center(), color=GRAY),
            Line(son.get_center(), spirit.get_center(), color=GRAY),
            Line(spirit.get_center(), father.get_center(), color=GRAY),
        ]

        self.play(FadeIn(god, father, son, spirit))
        self.play(*[Create(line) for line in links])
        self.wait(3)

        for _ in range(2):
            for line in links:
                self.play(line.animate.set_stroke(width=6), run_time=0.4, rate_func=smooth)
                self.play(line.animate.set_stroke(width=2), run_time=0.4, rate_func=smooth)
            self.move_camera(phi=60 * DEGREES, theta=90 * DEGREES, run_time=3, rate_func=smooth)
            self.move_camera(phi=75 * DEGREES, theta=45 * DEGREES, run_time=3, rate_func=smooth)

        self.play(FadeOut(god, father, son, spirit), *[FadeOut(line) for line in links])

        final = Text(
            "“Rab İsa'nın lütfu, Tanrı'nın sevgisi ve Kutsal Ruh'un paydaşlığı hepinizle olsun.”",
            font=FONT, color=WHITE
        ).scale(0.7)
        ref = Text("2. Korintliler 13:14", font=FONT, color=GRAY_A).scale(0.5).next_to(final, DOWN)
        self.play(FadeIn(final, shift=UP*0.3), FadeIn(ref, shift=UP*0.3))
        self.wait(4)
        self.play(FadeOut(final, shift=DOWN*0.3), FadeOut(ref, shift=DOWN*0.3))
