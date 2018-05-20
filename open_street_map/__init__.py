import pandas as pd

DATA_VOLCANO = pd.read_csv("Volcanoes_USA.txt")

with open("world.json", encoding="utf-8-sig") as f:
    DATA_POPULATION = f.read()

MAP_FILE_PATH = "map.html"
