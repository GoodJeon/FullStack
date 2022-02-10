import folium

my_loc = folium.Map(location=[37.55531990811339, 126.91638769586095], zoom_start=18)
folium.Marker([37.55488703498594, 126.91640276313012], popup=folium.Popup('멘야준', max_width=100)).add_to(my_loc)

my_loc.save('visual02.html')