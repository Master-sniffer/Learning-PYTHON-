import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename='eq_data_1_day_m1.json'
with open (filename) as f:
  all_ed_data=json.load(f)

all_ed_dict=all_ed_data['features']
mags , lons , lats=[], [], []
for eq_data in all_ed_dict:
  mag=eq_data['properties']['mag']
  lon=eq_data['geometry']['coordinates'][0]
  lat=eq_data['geometry']['coordinates'][1]
  mags.append(mag)
  lats.append(lat)
  lons.append(lon)

data=[Scattergeo(lon=lons , lat=lats)] #Отмечаем точки на карте путем ввода широты и долготы
my_layout= Layout(title="EARTH, BUT NOT SPACE")
fig={'data': data, 'layout' : my_layout}
offline.plot(fig , filename="global_earthquakes.html")
