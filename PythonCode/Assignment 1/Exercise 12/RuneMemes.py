
ᚢ=500/48
ᚲ=400/48
ᚠ=int(input("How many cookies do you want to make? "))
ᚦ=int(input("and how many cookies do you want ot make tomorow? "))
ᚨ=int(input("and how many cookies do you want to make in a week? "))
print("Antall cookies:","sugar(g)".rjust(13),"chocolate(g)".rjust(22),
"\n"+str(ᚠ),str(round(ᚠ*ᚲ,1)).rjust(23)+"\t","\t"+str(round(ᚠ*ᚢ,1)),
"\n"+str(ᚦ),str(round(ᚦ*ᚲ,1)).rjust(23)+"\t","\t"+str(round(ᚦ*ᚢ,1)),
"\n"+str(ᚨ),str(round(ᚨ*ᚲ,1)).rjust(23)+"\t","\t"+str(round(ᚨ*ᚢ,1)),
)
