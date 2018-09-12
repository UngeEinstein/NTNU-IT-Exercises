
#Kodesnutt 1:
if 'k' < 'b':
    print('k er mindre enn b')
else:
    print('k er større enn b')
#I Kodesnutt 1 så printes k er større enn b fordi k har større verdi enn b, altså at k<b er ikke sant.
  
#Kodesnutt 2:
ny = "New York"
la = "Los Angeles"
  
if ny < la:
    print(ny)
    print(la)
else:
    print(la)
    print(ny)
#I kodesnutt 2 så vil la printes først fordi L kommer før N i alfabetet, som også betyr at n har større verdi enn l og derfor er ny<la False.
  
#Kodesnutt 3:
d1 = "DRuEr"
d2 = "drUer"
if d1.lower() < d2.lower():
    print(d1)
    print(d2)
else:
    print(d2.lower())

#Kodesnutt 3 skriver druer fordi at d1 er ikke større en d2, der er nemlig like, aka d2 druer printes 