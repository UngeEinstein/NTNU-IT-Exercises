Pizza=750
Rabatt=0.2
Tips=0.08
Total=(Pizza*(1+Tips)*(1-Rabatt))
print("Total pris:",Total)
deltakkere=input("Hvor mange deltok på middagen?")
print("Ettersom dere var",deltakkere,"personer, så må hver person betale",Total/int(deltakkere))