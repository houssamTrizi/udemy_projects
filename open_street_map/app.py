from open_street_map import DATA_VOLCANO, MAP_FILE_PATH, DATA_POPULATION
from folium import Map, CircleMarker, FeatureGroup, GeoJson, LayerControl


def color_producer(elevation):
    if elevation < 1000:
        return "green"

    elif 1000 <= elevation < 3000:
        return "orange"

    else:

        return "red"


def main():
    longitudes = DATA_VOLCANO.LON
    latitudes = DATA_VOLCANO.LAT
    elevations = DATA_VOLCANO.ELEV

    map = Map(location=[33.99, -99.09], zoom_start=6, tiles="Mapbox Bright")

    volcano_features = FeatureGroup(name="Volcanoes")

    population_features = FeatureGroup(name="Population")

    for lat, lon, elev in zip(latitudes, longitudes, elevations):
        volcano_features.add_child(CircleMarker(
            location=[lat, lon],
            popup="{} m".format(elev),
            fill_color=color_producer(elev),
            color="grey",
            fill_opacity=0.7,
            radius=6,
            fill=True
        ))
    population_features.add_child(GeoJson(
        DATA_POPULATION,
        style_function=lambda x: {"fillColor": "green" if x["properties"]["POP2005"] < 10000000
        else "orange" if x["properties"]["POP2005"] <= 20000000 else "red"}
    ))

    map.add_child(volcano_features)

    map.add_child(population_features)

    map.add_child(LayerControl())
    map.save(MAP_FILE_PATH)


if __name__ == '__main__':
    main()
