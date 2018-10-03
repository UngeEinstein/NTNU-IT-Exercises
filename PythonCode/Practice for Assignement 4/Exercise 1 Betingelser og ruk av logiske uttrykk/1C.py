disposisjon=int(input("Hvor mye penger har Bjørn? "))
pris=int(input("Hvor mye penger koster genseren? "))
hoy_hals=False
if (disposisjon>=pris) and (hoy_hals==True):
    print("Bjørn kan kjøpe den")
elif (disposisjon>=pris) and (hoy_hals==False):
    print("Let videre")
else:
    print("Bjørn har ikke råd")