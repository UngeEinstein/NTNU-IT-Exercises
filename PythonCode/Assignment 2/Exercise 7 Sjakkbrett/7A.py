pos=input("Skriv inn posisjon: ")
#Hvis lengden på inputet ikke er 2 så får man en error
if len(str(pos))!=2:                                        
   exit("Feil input.\nDu må skrive akkurat to tegn")
tall=int(pos[1])
bokstav=str.lower(pos[0])
#Denne if statementen er for alle de svarte rutene i sjakkbrettet. Den skiller mellom bokstaver med svart og hvitt i første kolonne
if (bokstav in{"a","c","e","g"} and tall in {1,3,5,7}) or (bokstav in{"b","d","f","h"} and tall in {2,4,6,8}):
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
