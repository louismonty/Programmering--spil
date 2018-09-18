import math
import os

from random import randint

time = randint(1,20)
print("A car is in a race and the green light is turning on, the car reaches 40km/h at",time,"seconds")

geuss = float(input("At which acceleration do you the think the car will gain?: "))

acceleration = ((40/3.6)/time)
print(acceleration, "m/s^2")

delevation = abs(acceleration - geuss)
print("\n You were off by ", delevation, "m/s^2")

deviation_percentage = int((abs(acceleration - geuss)/time)*100)
print("You´r devition in percentage is", deviation_percentage,"%")

if deviation_percentage < 10:
    print("Very good")

os.system("pause")