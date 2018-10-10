# skriv funksjonen din her
def knop2km_t(knop):
    konversjon=knop*0.514444444*3.6
    return konversjon
# skript
knop = float(input("Oppgi fart i knop:"))
km_t = knop2km_t(knop)
print("Det blir", round(km_t,2), "km/t")