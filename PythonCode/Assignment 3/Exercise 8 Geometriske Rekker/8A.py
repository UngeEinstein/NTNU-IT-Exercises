Sum=0
i=0
n=int(input("Skrivv inn antall ledd i rekken"))
r=int(input("Skriv inn et tall mellom -1,1"))
while(i<=n):
    Sum+=(r**i)
    i+=1
print(Sum)