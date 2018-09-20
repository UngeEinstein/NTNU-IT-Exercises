minipris=199
fullpris=440

while True:
    dager_til=input("Dager til du skal reise? ")
    if dager_til.isdigit():
        break
    print("Skriv inn et gyldig tall: ")    
if int(dager_til)>14:
    print("Minipris {0},- kan ikke refunderes/endres".format(minipris))
    while True:
        ønskes=input("Ønskes dette? (J/N): ").lower()
        if ønskes in ["j","n"]:
            break
        print("Skriv inn et gyldig svar")
    if ønskes=="j":
        print("Takk for pengene, god reise!") 
    elif ønskes=="n":
        print("Da tilbyr vi fullpris {0},-".format(fullpris))   
else:
    print("For sent for minipris; fullpris {0},-".format(fullpris))