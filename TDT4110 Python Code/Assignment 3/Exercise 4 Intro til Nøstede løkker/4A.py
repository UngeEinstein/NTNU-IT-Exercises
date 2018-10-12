studass=int(input("Hvor mange studenter? "))
emner=int(input("Hvor mange emner? "))
for x in range(1,studass+1):
    for y in range(1,emner+1):
        print("Stud {0} elsker Emne {1}".format(x,y),end=" ; ")
    print()