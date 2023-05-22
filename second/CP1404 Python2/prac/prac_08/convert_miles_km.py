from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window


class ConvertMilesKmApp(App):
    """ ConvertMilesKmApp is a Kivy App for converting miles to km """
    message = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        # Window.size = (100, 50)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = "54.72"
        return self.root

    def handle_convert(self, value):
        """ handle calculation (could be button press or toher call), output result to label widget"""
        try:
            result = round(float(value) * 1.60934, 2)
            self.message = str(result)
        except ValueError:
            pass

ConvertMilesKmApp().run()