#Ща мы будем работать с excel файлами и сможем чего-нибудь анализировать

import csv 
from matplotlib import pyplot as plt

filename='sitka_weather_07-2018_simple.csv' # Файл находится в Extra FIles в generating data
with open (filename) as f:
  reader=csv.reader(f)
  header_row=next(reader)
  #for index, column_header in enumerate(header_row): #enemurate служит для того, чтобы возвращать индекс каждого элемента и его значение при переборке списка
  #  print (index, column_header)

  highs=[]
  for row in reader:
    high=int(row[5])
    highs.append(high)

plt.style.use('seaborn')
fig,ax=plt.subplots()
ax.plot(highs, c="red")

plt.title("daily high temps", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
