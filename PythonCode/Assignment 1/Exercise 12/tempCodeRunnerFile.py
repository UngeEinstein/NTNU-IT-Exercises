skjokolade=500/48
sukker=400/48
cookies_1=int(input("Hvor mange cookies vil du lage? "))
cookies_2=int(input("og hvor mange cookies vil du lage nå? "))
cookies_3=int(input("og hvor mange cookies vil du lage til slutt? "))
print("Antall cookies:","sukker(g)".rjust(14),"skjokolade(g)".rjust(19),
"\n"+str(cookies_1),str(round(cookies_1*sukker,1)).rjust(23)+"\t",str(round(cookies_1*skjokolade,1)).rjust(15),
"\n"+str(cookies_2),str(round(cookies_2*sukker,1)).rjust(23),str(round(cookies_2*skjokolade,1)).rjust(15),
"\n"+str(cookies_3),str(round(cookies_3*sukker,1)).rjust(23),str(round(cookies_3*skjokolade,1)).rjust(15),
)