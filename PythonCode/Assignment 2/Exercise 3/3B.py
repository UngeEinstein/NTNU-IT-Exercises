
navn_1=input("Førstenavn: ")
navn_2=input("Andre navn: ")
navn_1_l=str.lower(navn_1)
navn_2_l=str.lower(navn_2)
print("Under følger navnene i alfabetisk rekkefølge:")

#Tar ikke hensyn til æøå
if navn_1_l<navn_2_l:
    print(navn_1,
    "\n"+navn_2)
else:print(navn_2,
    "\n"+navn_1)

#Tar hensyn til ÆØÅ

if "å" in navn_1_l[0]:
    print(navn_2,
    "\n"+navn_1)
 
elif "å" in navn_2_l[0]:
    print(navn_1,
    "\n"+navn_2)