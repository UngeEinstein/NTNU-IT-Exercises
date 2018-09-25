while True:
    repitisjoner=input("Hvor mange adjektiv vil du gi meg?")
    if repitisjoner.isdigit():
        repitisjoner=int(repitisjoner)
        break

for i in range(repitisjoner):
    adj = input("Beskriv deg selv med et adjektiv? ")
    print("Hah, du", adj + "!? Jeg er mye", adj + "ere!")
print("Takk for nå!")
