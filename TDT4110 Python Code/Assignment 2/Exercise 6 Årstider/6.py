måned=str.lower(input("Måned: "))
dag=int(input("Dag: "))
if (måned=="mars" and dag>=20) or måned=="april" or måned=="mai" or (måned=="juni" and dag<=20):
    print("Vår")
elif (måned=="juni" and dag>=21) or måned=="juli" or måned=="august" or (måned=="september" and dag<=22):
    print("Sommer")
elif (måned=="september" and dag>=22) or måned=="oktober" or måned=="november" or (måned=="desember" and dag<=21):
    print("Høst")
else:
    print("Vinter")