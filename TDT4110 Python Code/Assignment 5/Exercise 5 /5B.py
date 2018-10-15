import math

def set_gravity(gravity):
  global GRAVITY
  GRAVITY = gravity
 
 
print(get_fall_time(20))

def get_fall_time(distance,gravity=None):
    if gravity is None:
        set_gravity(GRAVITY)
    fall_time=math.sqrt((2*distance)/GRAVITY)
    return fall_time

print(get_fall_time(20))
print(get_fall_time(20,1.62))