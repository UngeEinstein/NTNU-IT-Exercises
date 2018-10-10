def komparativ(adj):
    # GROVT FORENKLET FOR Å KUNNE FOKUSERE PÅ HOVEDPOENGET
    if len(adj) >= 8: # unøyaktig
        svar = "mer " + adj
    else:
        svar = adj + "ere"
    return svar
  
### TILLEGG 1, ny funksjon, kommer her:
def superlativ(adj):
    if len(adj)>=8:
        svar="mest {0}".format(adj)
    else:
        svar="{0}est".format(adj)
    return svar

def gradBøying(adj,bøyingsform,bøying):
    svar = input("Hva er {0} for {1}?".format(bøyingsform,adj)).lower()
    fasit = bøying(adj).lower()
    if svar== fasit:
        print("Korrekt!")
    else:
        print("Feil det var {0}".format(fasit))
   
#DEL AV KODEN HVOR SYSTEMET DISSER BRUKEREN
def main():
    adj = input("Beskriv deg selv med et adjektiv: ")
    print("Hah! Jeg er mye", komparativ(adj), "!")
    ### TILLEGG 2 kommer her ...
    print("Jeg er faktisk {0} i hele verden".format(superlativ(adj))) 
    # DEL AV KODEN HVOR BRUKEREN TRENER PÅ Å GRADBØYE
    adj = input("Skriv inn et adjektiv: ")
    ### TILLEGG 3 kommer her...
    gradBøying(adj,"komparativ",komparativ)  
    gradBøying(adj,"superlativ",superlativ)
main()



