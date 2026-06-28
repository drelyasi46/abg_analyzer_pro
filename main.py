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

    def analyze(self):
        try:
            screen = self.root

            ph = float(screen.ids.ph.text)
            pco2 = float(screen.ids.pco2.text)
            hco3 = float(screen.ids.hco3.text)

            na = float(screen.ids.na.text) if screen.ids.na.text else None
            k = float(screen.ids.k.text) if screen.ids.k.text else None
            cl = float(screen.ids.cl.text) if screen.ids.cl.text else None
            albumin = float(screen.ids.albumin.text) if screen.ids.albumin.text else None
            lactate = float(screen.ids.lactate.text) if screen.ids.lactate.text else None

            result = self.engine.analyze(
                ph=ph,
                pco2=pco2,
                hco3=hco3,
                na=na,
                k=k,
                cl=cl,
                albumin=albumin,
                lactate=lactate,
            )

            screen.ids.result.text = str(result)

        except Exception as e:
            screen.ids.result.text = f"Error:\n{e}"


if __name__ == "__main__":
    ABGApp().run()