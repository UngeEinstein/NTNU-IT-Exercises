alder=int(input("Din alder: "))
if alder<3:
    print("Biletten er gratis")
elif alder<12:
    print("Bilettpris:30kr")
elif alder<26:
    print("Bilettpris:50kr")
elif alder<67:
    print("Bilettpris:80kr")
else:
    print("Bilettpris:40kr")

    