from open_street_map import DATA, MAP_FILE_PATH
from folium import Map, Marker, FeatureGroup, Icon


def main():
    longitudes = DATA.LON
    latitudes = DATA.LAT
    elevations = DATA.ELEV

    map = Map(location=[33.99, -99.09], zoom_start=6, tiles="Mapbox Bright")

    features = FeatureGroup(name="Volcanoes")

    for lat, lon, elev in zip(latitudes, longitudes, elevations):
        features.add_child(Marker(location=[lat, lon], popup="{} m".format(elev), icon=Icon(color="green")))

    map.add_child(features)

    map.save(MAP_FILE_PATH)


if __name__ == '__main__':
    main()
