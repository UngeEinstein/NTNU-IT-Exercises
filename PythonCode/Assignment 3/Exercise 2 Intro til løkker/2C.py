def adjektivLøkker():
    i = 42
    while i>0:
        print("Du har {0} bokstaver til disposisjon".format(i))
        adj = input("Beskriv deg selv med et adjektiv? ")   
        print("Hah, du {0}!? Jeg er mye {0}ere!".format(adj))
        i-=len(adj)
    print("Takk for nå!")
adjektivLøkker()