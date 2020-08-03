#Making simple figure

import matplotlib.pyplot as plt

squares=[1,4,9,16,25]
fig, ax= plt.subplots() #fig - представляет весь рисунок или набор диаграмм. ax - представляет одну диаграмму на рисунке
ax.plot(squares) # plot - строит что-то осмысленное из того, что мы ему дали

plt.show() # show - открывает окно просмотра matplotlib и в этом окне выводит график

#Changing types of writings and thickness in figure

import matplotlib.pyplot as plt

squares=[1,4,9,16,25]
fig, ax= plt.subplots()
ax.plot(squares, linewidth=3) # linewidth - толщина линии

ax.set_title("Square numbers", fontsize=24) # назначение заголовка fontsieze - размер текста
ax.set_xlabel("Value", fontsize=14) # то, что будет написано на оси X
ax.set_ylabel("Square of Value", fontsize=14) # то, что будет написано на оси Y

ax.tick_params(axis='both', labelsize=14) # размер шрифта делений на осях
plt.show()

#Correction of the plot

import matplotlib.pyplot as plt
input_values=[1,2,3,4,5] #это поможет нашей проге понять как всё вычислять
squares=[1,4,9,16,25]
fig, ax= plt.subplots()
ax.plot(input_values ,squares, linewidth=3) 

ax.set_title("Square numbers", fontsize=24) 
ax.set_xlabel("Value", fontsize=14) 
ax.set_ylabel("Square of Value", fontsize=14) 

ax.tick_params(axis='both', labelsize=14)
plt.show()

...
