navn=input("Skriv ditt navn: ")
alder=input("Hei, "+navn+", hvor gammel er du? ")
progalder=input("Hvor gammel var du da du begynte å programmere? ")
lengde_progalder=int(alder)-int(progalder)
print("Da har du programmert i ",lengde_progalder, " år." )
if lengde_progalder==1:
    input("Syns du det "+str(lengde_progalder)+" året har vært givende? ")
else:
    input("Syns du de "+str(lengde_progalder)+" årene har vært givende? ")
print("Takk for svar, ",navn+"!")