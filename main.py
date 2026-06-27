from kivy.lang import Builder
from kivymd.app import MDApp

from core.abg_engine import ABGEngine


class ABGApp(MDApp):

    def build(self):
        self.title = "ABG Analyzer Pro"

        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.primary_hue = "700"
        self.theme_cls.theme_style = "Light"

        self.engine = ABGEngine()

        return Builder.load_file("main.kv")


if __name__ == "__main__":
    ABGApp().run()