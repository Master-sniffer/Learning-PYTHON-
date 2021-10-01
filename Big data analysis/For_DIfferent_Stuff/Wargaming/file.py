#Используйте google colab или jupiter 

import numba
import matplotlib.pyplot as plt
import random 
from random import randint
import math
import numpy as np



# mob 1 - 850 hp; damage 80-90; speed = 1 sec
# mob 2 - 600 hp; damage 160-170; speed = ?

@numba.njit
def delimeter(a, b):
    if (a < b) :
        return delimeter(b, a)
     
    # base case
    if (abs(b) < 0.001) :
        return a
    else :
        return (delimeter(b, a - math.floor(a / b) * b))

@numba.njit
def calculate(time, difference, differ_time, x , y):
    SPEED1=1
    SPEED2=time
    WinMob1=0
    WinMob2=0
    EndSteps=(delimeter(time, SPEED1))
    for i in range (1000):
        HP1=850
        HP2=600
        steps=0.0
        while HP1>0 and HP2>0:
            steps+=(EndSteps)
            steps=round(steps,4)
            
            if (steps%float(SPEED1)==0.0):
                HP2-=randint(80,90)
                
            if (steps%float(SPEED2)==0.0):
                HP1-=randint(160,170)
            
            if (HP2<=0 and HP1>0):
                WinMob1+=1
            
            elif (HP1<=0 and HP2>0):
                WinMob2+=1
            

            
    if (WinMob2!=0 and WinMob1!=0):
      x=np.append(x,time)
      y=np.append(y ,  (abs(WinMob1-WinMob2)))
      if (abs(WinMob1-WinMob2)<difference):
          print ("difference", difference , "\nmob1-mob2",abs(WinMob1-WinMob2) )
          difference= abs(WinMob1-WinMob2)
          differ_time=time
      print ("\n",time)
      print (WinMob1, "Mob 1")
      print (WinMob2,"Mob 2\n")
    return difference, differ_time, x , y

time=0.5
difference=1000
differ_time=0
x=np.array([])
y=np.array([])
while time <=5.0:
    difference, differ_time , x ,y=calculate(round(time,4), difference, differ_time, x, y)
    time+=0.001

print ("time", differ_time,"\ndifference", difference)
plt.plot(x, y)
plt.xlabel('time')
plt.ylabel('differ')
plt.show()
