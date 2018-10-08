hemmelig_ord=input("Skriv inn det hemmelige ordet: ")
antall_liv=int(input("Skriv inn antall liv du vil gi brukeren: "))
bokstav=""
while True:
    if antall_liv!=0:
        bokstav=input("Gjett på en bokstav: ")
    if bokstav not in hemmelig_ord:
        antall_liv-=1
        if antall_liv==0:
            print("Du har brukt opp alle livene dine")
            break
        else:
            print("Bokstaven {0} er ikke i ordet \nDu har {1} liv igjen, prøv på nytt".format(bokstav,antall_liv))
    else:
        print("Stemmer, bokstaven er i ordet")
