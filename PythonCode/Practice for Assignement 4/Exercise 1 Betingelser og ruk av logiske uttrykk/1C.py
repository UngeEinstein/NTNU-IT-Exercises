disposisjon=int(input("Hvor mye penger har Bjørn? "))
pris=int(input("Hvor mye penger koster genseren? "))
hoy_hals=False
if (disposisjon>=pris) and (hoy_hals==True):
    print("Bjørn kan kjøpe den")
elif (disposisjon>=pris) and (hoy_hals==False):
    print("Let videre")
else:
    print("Bjørn har ikke råd")

a = True
b = False
if not ((a and not b) or (a or b)):
    print ("Tomat")
else:
    print ("Potet")