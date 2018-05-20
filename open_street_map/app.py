from open_street_map import DATA, MAP_FILE_PATH
from folium import Map, CircleMarker, FeatureGroup, Icon


def color_producer(elevation):

    if elevation < 1000:
        return "green"

    elif  1000 <= elevation < 3000:
        return "orange"

    else:

        return "red"


def main():
    longitudes = DATA.LON
    latitudes = DATA.LAT
    elevations = DATA.ELEV

    map = Map(location=[33.99, -99.09], zoom_start=6, tiles="Mapbox Bright")

    features = FeatureGroup(name="Volcanoes")

    for lat, lon, elev in zip(latitudes, longitudes, elevations):
        features.add_child(CircleMarker(
            location=[lat, lon],
            popup="{} m".format(elev),
            fill_color=color_producer(elev),
            color="grey",
            fill_opacity=0.7,
            radius=6,
            fill=True
        ))

    map.add_child(features)

    map.save(MAP_FILE_PATH)


if __name__ == '__main__':
    main()
