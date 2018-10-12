minipris=199
fullpris=440


def dager(minipris,fullpris):
    dager_til=int(input("Dager til du skal reise? "))
    if dager_til>14:
        print("Du kan få minipris: ",minipris,",-")
    else:
        print("For sent for minipris; fullpris",str(fullpris)+",-")
    return
    
dager(minipris,fullpris)