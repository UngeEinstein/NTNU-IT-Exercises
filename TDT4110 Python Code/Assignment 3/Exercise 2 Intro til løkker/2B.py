def adjektivLøkker():
    i = 0
    print("Slå Enter uten å skrive noe når du vil avslutte.")
    while i < 1:
        adj = input("Beskriv deg selv med et adjektiv? ")   
        if adj!="":
            print("Hah, du {0}!? Jeg er mye {0}ere!".format(adj))
        else:
            i += 1  # øker med 1
    print("Takk for nå!")
adjektivLøkker()