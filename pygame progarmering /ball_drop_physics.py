import math
from random import randint

def ball_drop_physics():
    height = randint(1,100)
    print("A ball is thrown out of a tower at the height of ",height,"meters")

    guess = float(input("How long du you think it takes the ball to reach the ground?: "))

    time = math.sqrt((-height)/(1/2*(-9.82)))
    print ("\nThe ball hits the ground after ",time, " seconds")

    deviation = abs(time - guess)
    print("\nYou were off by ",deviation," seconds")

    deviation_percentage = int((abs(time - guess) / time) *100)
    print("You'r deviation in percentage is",deviation_percentage,"%")

    if deviation_percentage < 10:
        print("Very good")
