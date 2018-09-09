avokado=6.022*(10)**(23)
stoff=input("Si et stoff du er i besittelse av: ")
molvekt=int(input("Hva er molvekt i gram for"+stoff+"? "))
vekt=int(input("Hvor mange gram"+stoff+"har du? "))
mol=vekt/molvekt
print(round(mol*avokado,1000))