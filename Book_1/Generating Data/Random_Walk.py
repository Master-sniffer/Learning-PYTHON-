#RANDOM WALK
# блуждание ака RANDOM WALK - симуляция случайных событий (это проще говоря). Так, к примеру, есть капля дождя, которая передвигается в случайном направлении (тут физика тож играет роль, НО НЕ БУДЕМ ОБ ЭТОМ.). Короч, будет весело, вот увидите

from random import choice
import matplotlib.pyplot as plt

class RandomWalk():
  def __init__(self, num_points=5000):
    self.num_points=num_points

    self.x_values=[0]
    self.y_values=[0]
  
  def fill_walk(self):
    while len(self.x_values) < self.num_points:
      x_direction=choice([1,-1])
      x_distance=choice([0,1,2,3,4])
      x_step=x_direction * x_distance

      y_direction=choice([-1,1])
      y_distance=choice([0,1,2,3,4])
      y_step=y_direction * y_distance

      if x_step ==0 and y_step==0:
        continue
      
      x=self.x_values[-1] + x_step
      y=self.y_values[-1] + y_step

      self.x_values.append(x)
      self.y_values.append(y)

while True:
  rw=RandomWalk()
  rw.fill_walk()
  plt.style.use("classic")
  fix,ax=plt.subplots()
  points_numbers=range(rw.num_points)
  ax.scatter(rw.x_values, rw.y_values, c=points_numbers, cmap=plt.cm.Reds, edgecolors='none', s=15)
  ax.scatter(rw.x_values[-1], rw.y_values[-1], c="blue", edgecolors='None', s=100)
  ax.scatter(rw.x_values[1], rw.y_values[1], c='green', edgecolors='None', s=100)
  plt.show()

  program=str(input("Keep running ? (y/n) ?"))
  if program=='n':
    break
