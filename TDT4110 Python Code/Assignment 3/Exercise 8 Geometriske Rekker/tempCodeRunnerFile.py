n = 0
tol = 0.001
r = 0.5
summen = 0

while (2 - summen) > tol:
    summen = (1-r**(n+1))/(1-r)
    n += 1
print(summen)
print("Antall iterasjoner: ", n)
print("Differansen mellom grenseverdien og faktisk verdi: ", 2 - summen)