#Making simple figure

import matplotlib.pyplot as plt

squares=[1,4,9,16,25]
fig, ax= plt.subplots() #fig - представляет весь рисунок или набор диаграмм. ax - представляет одну диаграмму на рисунке
ax.plot(squares) # plot - строит что-то осмысленное из того, что мы ему дали

plt.show() # show - открывает окно просмотра matplotlib и в этом окне выводит график
