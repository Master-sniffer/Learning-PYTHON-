#import this # delete the first hashtag to see the truth
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

#Stylish look of your diagram

import matplotlib.pyplot as plt
print (plt.style.available) # Выводит доступные стили

plt.style.use('ggplot')
input_values=[1,2,3,4,5] 
squares=[1,4,9,16,25]
fig, ax= plt.subplots()
ax.plot(input_values ,squares, linewidth=3) 

ax.set_title("Square numbers", fontsize=24) 
ax.set_xlabel("Value", fontsize=14) 
ax.set_ylabel("Square of Value", fontsize=14) 

ax.tick_params(axis='both', labelsize=14)
plt.show()

#Marking spec dots and points on the diagram

import matplotlib.pyplot as plt
plt.style.use('ggplot')

fig, ax= plt.subplots()
ax.scatter(2,4, s=200) # scatter (x,y) - указываем на графике точку в этих коордах. s - задает размер точки
ax.set_title("Square numbers", fontsize=24) 
ax.set_xlabel("Value", fontsize=14) 
ax.set_ylabel("Square of Value", fontsize=14) 

ax.tick_params(axis='both', which="Major", labelsize=14)
plt.show() 

#Showing a list of dots by using scatter

import matplotlib.pyplot as plt
x_values=[1,2,3,4,5]
y_values=[1,4,9,16,25]

plt.style.use('ggplot')
fig, ax= plt.subplots()
ax.scatter(x_values, y_values, s=100) # Scatter читает данные так - (1,1), (2,4), (3,9) и тд
ax.set_title("Square numbers", fontsize=24) 
ax.set_xlabel("Value", fontsize=14) 
ax.set_ylabel("Square of Value", fontsize=14) 

ax.tick_params(axis='both', which="Major", labelsize=14)
plt.show() 

#Automatic calculation of the flow of data

import matplotlib.pyplot as plt

x_values=list(range(1,1001))
y_values=[x**2 for x in x_values]

plt.style.use('ggplot')
fig, ax= plt.subplots()
ax.scatter(x_values, y_values, s=10)
ax.set_title("Square numbers", fontsize=24) 
ax.set_xlabel("Value", fontsize=14) 
ax.set_ylabel("Square of Value", fontsize=14) 
ax.tick_params(axis='both', which="Major", labelsize=14)

ax.axis([0,1100,0,1100000]) #axis - нужен для того, чтобы задать ограничения по осям (сначала для X потом для Y) - (Xmin, Xmax, Ymin,Ymax)
plt.show() 

#Using custom colors

ax.scatter(x_values, y_values, c='red' s=10)
#OR
ax.scatter(x_values, y_values,c=(0,0.8,0) s=10)

#Colour map

import matplotlib.pyplot as plt

plt.style.use('ggplot')
fig, ax= plt.subplots()
x_values=list(range(1,1001))
y_values=[x**2 for x in x_values]

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues , s=10)
ax.set_title("Square numbers", fontsize=24) 
ax.set_xlabel("Value", fontsize=14) 
ax.set_ylabel("Square of Value", fontsize=14) 
ax.tick_params(axis='both', which="Major", labelsize=14)

plt.show() 

#Automatic save of the diagrams

plt.savefig('squares_plot.png', bbox_inches='tight')# ВМЕСТО plt.show() 
# Первый аргумент - название файла. Второй аргумент - надо ли убирать пустое пространство или нет, если вы не будете вписывать это в метод, то вы просто сохраните картинку

#Extra Tasks
#1
import matplotlib.pyplot as plt

plt.style.use('ggplot')
fig, ax= plt.subplots()
x_values=list(range(1,6))
y_values=[x**2 for x in x_values]
ax.scatter(x_values, y_values, c="red", s=100)
ax.set_title("Square numbers", fontsize=24) 
ax.set_xlabel("Value", fontsize=14) 
ax.set_ylabel("Square of Value", fontsize=14) 
ax.tick_params(axis='both', which="Major", labelsize=14)

plt.show() 

#2
import matplotlib.pyplot as plt
plt.style.use('ggplot')
fig, ax= plt.subplots()
x_values=list(range(1,5001))
y_values=[x**2 for x in x_values]
ax.scatter(x_values, y_values, c=x_values, cmap=plt.cm.Reds, s=10)
ax.set_title("Square numbers", fontsize=24) 
ax.set_xlabel("Value", fontsize=14) 
ax.set_ylabel("Square of Value", fontsize=14) 
ax.tick_params(axis='both', which="Major", labelsize=14)

plt.show() 

...
