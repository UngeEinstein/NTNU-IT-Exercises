print("Hei! Jeg har 10 pannekaker jeg ønsker å dele med deg ^u^")
p = int(input("Hvor mange pannekaker ønsker du? "))
s = input("Er du glad i pannekaker? (J/N) ")
 
if s == 'J':
    elsker_pannekaker = True
else:
    elsker_pannekaker = False
if not(elsker_pannekaker) or p>10 or p<0:            #Kode mangler her
    print("Beklager, men det er nok ikke mulig")
else:
    r = 10-p
    print("Da blir det",p,"på deg og",r,"på meg :D")