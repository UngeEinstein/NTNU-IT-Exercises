import math

GRAVITY=9.81

def get_fall_time(distance):
    fall_time=math.sqrt((2*distance)/GRAVITY)
    return fall_time

distance=int(input("How many meters shall the object fall? "))
print("It will take {0} seconds for the object to fall {1} meter".format(get_fall_time(distance),distance))
