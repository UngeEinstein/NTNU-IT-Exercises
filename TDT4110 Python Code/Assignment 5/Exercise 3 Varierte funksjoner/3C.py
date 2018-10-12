def imp2cm(fot,tommer):
    tommer_til_cm=tommer*2.54
    fot_til_cm=fot*12*2.54
    sum=tommer_til_cm+fot_til_cm
    return sum

fot = int(input("Oppgi antall fot: "))
tommer = int(input("Oppgi antall tommer: "))
cm = imp2cm(fot, tommer)
print("Det blir", cm, "cm")    