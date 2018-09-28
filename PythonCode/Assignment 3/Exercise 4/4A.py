studass=int(input("Hvor mange studenter? "))+1
emner=int(input("Hvor mange emner? "))+1
for x in range(1,studass):
    for y in range(1,emner):
        print("Stud {0} elsker Emne {1}".format(x,y),end=" ; ")
    print()