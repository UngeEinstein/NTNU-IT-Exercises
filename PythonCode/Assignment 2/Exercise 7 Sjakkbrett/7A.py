def sjakk():
    pos=input("Skriv inn posisjon: ")
    #Hvis lengden på inputet ikke er 2 så får man en error
    if len(str(pos))!=2:                                        
        exit("Feil input.\nDu må skrive akkurat to tegn")
    tall=int(pos[1])
    bokstav= (pos[0])
    bokstav_svart_1={"a","c","e","g"}
    tall_svart_1={1,3,5,7}

    #Denne if statementen er for alle de svarte rutene i sjakkbrettet. Den skiller mellom bokstaver med svart og hvitt i første kolonne
    if (bokstav in(bokstav_svart_1) and tall in(tall_svart_1)) or (bokstav not in bokstav_svart_1 and tall not in tall_svart_1):
        print("Svart")
    #Denne elif statementen sier at hvis bokstaven ikke er i listen av tillate bokstaver, så vil man få error
    elif (bokstav not in{"a","b","c","d","e","f","g","h"}):
        exit("Feil input.\nFørste tegn må være en bokstav A-H eller a-h")
    #Denne elif statementen sier at hvis bokstaven ikke er i listen av tillate tall så vil man få error 
    elif (tall not in{1,2,3,4,5,6,7,8}):
        exit("Feil input.\nAndre tegn må være et tall 1-8")
    #Hvis posisjonen har ungåt alle errorene, har riktig input og er ikke svart. Så vil det si at posisjonen står på en hvit rute
    else:
        print("Hvit")
sjakk()
