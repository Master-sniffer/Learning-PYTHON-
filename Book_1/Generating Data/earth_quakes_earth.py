import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#filename='eq_data_1_day_m1.json'
filename='eq_data_30_day_m1.json'
with open (filename) as f:
  all_ed_data=json.load(f)

all_ed_dict=all_ed_data['features']
mags , lons , lats, hover_text=[], [], [], []
for eq_data in all_ed_dict:
  title=eq_data['properties']['title']
  mag=eq_data['properties']['mag']
  lon=eq_data['geometry']['coordinates'][0]
  lat=eq_data['geometry']['coordinates'][1]
  mags.append(mag)
  lats.append(lat)
  lons.append(lon)
  hover_text.append(title)

#Ниже приведен один из вариантов , как можно все сделать
#data=[Scattergeo(lon=lons , lat=lats)]  #Отмечаем точки на карте путем ввода широты и долготы
#Или же можно сделать так
data=[{
  'type' : 'scattergeo',
  'lon' : lons,
  'lat' : lats,
  'text' : hover_text, #text выводит инфу в виде подсказки
  'marker' : {
    'size' : [5*mag for mag in mags],
    'color' : mags,
    'colorscale' : 'Viridis', #Может быть Greys YlGnBu Greens и тд
    'reversescale' : True,
    'colorbar' : {'title' : 'Magnitude'},
  },
}]
my_layout= Layout(title="EARTH, BUT NOT SPACE")
fig={'data': data, 'layout' : my_layout}
offline.plot(fig , filename="global_earthquakes.html")
