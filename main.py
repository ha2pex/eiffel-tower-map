import os
os.system("pip install folium")

import folium, branca

map = folium.Map([48.858376, 2.295138], 20)
map.add_child(folium.LatLngPopup())

folium.Marker([48.858376, 2.295138], "Eiffel Tower is there").add_to(map)
map.show_in_browser
map.save("index.html")