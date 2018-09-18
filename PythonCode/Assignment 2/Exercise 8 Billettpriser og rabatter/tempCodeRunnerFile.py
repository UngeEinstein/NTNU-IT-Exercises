fullpris=440
minipris=199

while True:
    dager_til=input("Dager til du skal reise? ")
    if dager_til.isdigit():
        break
    print("Skriv inn et gyldig tall: ")    
if int(dager_til)>14:
    print("Minipris,",str(minipris)+",- kan ikke refunderes/endres")
    while True:
        ønskes=str.lower(input("Ønskes dette? (J/N): "))
        if ønskes in ["j","n"]:
            break
        print("Skriv inn et gyldig svar")
    if ønskes=="j":
        print("Takk for pengene, god reise!") 
    elif ønskes=="n":
        print("Da tilbyr vi fullpris",str(fullpris)+",-")   
else:
    print("For sent for minipris; fullpris",str(fullpris)+",-")