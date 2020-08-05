#Ща мы будем работать с excel файлами и сможем чего-нибудь анализировать

import csv 
from matplotlib import pyplot as plt
from datetime import datetime

#filename='sitka_weather_07-2018_simple.csv' # Файл находится в Extra FIles в generating data
filename='sitka_weather_2018_simple.csv'
with open (filename) as f:
  reader=csv.reader(f)
  header_row=next(reader)
  #for index, column_header in enumerate(header_row): #enemurate служит для того, чтобы возвращать индекс каждого элемента и его значение при переборке списка
  #  print (index, column_header)

  dates, highs , lows=[], [], []
  for row in reader:
    current_date=datetime.strptime(row[2], "%Y-%m-%d") #"%Y-%m-%d" показывает, что за чем стоит в файле - сначала идет год, потом месяц и день !
    high=int(row[5]) 
    low=int(row[6])
    lows.append(low)
    highs.append(high)
    dates.append(current_date)

plt.style.use('seaborn')
fig,ax=plt.subplots()
ax.plot(dates,highs, c="red")
plt.plot(dates, lows, c ='blue')

plt.title("daily high temps in 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate() #autofmt_xdate нормализует расположение дат на оси х
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
