forsøk=0
hovedstad=False
while hovedstad!="alofi":
    hovedstad=input("Hva heter hovedstaden til Niue?  ").lower()
    forsøk+=1
    if hovedstad!="alofi":
        print("Det var feil, prøv igjen")
print("Korrekt!! Du brukte {0} forsøk".format(forsøk))
