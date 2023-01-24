import kivy
from kivy.app import App
from kivy.uix.label import Label
import matplotlib.pyplot as plt
import numpy as np
from kivy.garden.matplotlib import FigureCanvasKivyAgg
from kivy.lang import Builder
import geopandas
import contextily as cx

class MyApp(App):
    def build(self):
        self.str = Builder.load_string("""
BoxLayout:
    layout:layout
    BoxLayout:
        id:layout
        """)
        path = r"C:\Users\g.husband\Downloads\download\layers\POLYLINE.shp"
        gdf = geopandas.read_file(path)
        fig, ax = plt.subplots()
        gdf.plot(ax=ax)
        cx.add_basemap(ax, crs=gdf.crs)
        self.str.layout.add_widget(FigureCanvasKivyAgg(fig))
        return self.str

if __name__ == '__main__':
    MyApp().run()
