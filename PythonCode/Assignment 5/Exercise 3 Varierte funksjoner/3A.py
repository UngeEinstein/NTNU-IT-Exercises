# Skriv funksjonen din her
def absol(tall):
    if tall<0:
        tall*=(-1)
    return tall
# skript for å teste funksjonen:
print("Absoluttverdien til 5 er", absol(5))
print("Absoluttverdien til -3 er", absol(-3))
print("Absoluttverdien til 0 er", absol(0))