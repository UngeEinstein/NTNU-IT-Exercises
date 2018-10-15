def heltallsdivisjon(x,y):
    num=x//y
    return (num,x,y)

def kvadratett(x):
    num=x**2
    return (num,x)
num,x,y=heltallsdivisjon(23,4)
print("Helltallsdivisjon av {0} over {1} gir {2}".format(x,y,num))

num,x=kvadratett(3)
print("Kvadratet av {0} er {1}".format(x,num))