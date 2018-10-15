while True:
    gender=input("What's yur gender? (f/m)").lower()
    age=int(input("What's your age?"))
    if age>=16 and age<=25:
        break
    else:
        print("Sorry your age is outside the targeted age group")
while True:
    fag=input("Tar du et eller flere fag? [ja/nei]: ")
    if fag.lower()=="ja" or fag.lower()=="nei":
        break
    else:
        print("Skriv inn et gyldig svar")
        



