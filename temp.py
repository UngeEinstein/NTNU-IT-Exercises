des_tall=float(input("Gi inn et desimaltall: "))
des_plass=int(input("Antall desimaler i avrunding: "))
avrunde=round(des_tall+10**(-(des_plass+1)),des_plass)
print(format(des_tall,"."+str(des_plass)+"f"))
if format(des_tall,"."+str(des_tall)+"f")<des_tall:
    print("Avrundet til",des_plass,"desimaler:",avrunde)
else:
    print("Avrundet til",des_plass,"desimaler:",round(des_tall,des_plass)) 


#Finn ut en IF statement som funker
#
