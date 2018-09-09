des_tall=float(input("Gi inn et desimaltall: "))
des_plass=int(input("Antall desimaler i avrunding: "))
print(des_tall)
print(round(des_tall,des_plass))
rounded=round(des_tall,des_plass)
print(round(des_tall,des_plass)<des_tall)
if rounded<des_tall:
    print("Avrundet til",des_plass,"desimaler:",round(des_tall+10**(-(des_plass+1)),des_plass))
else:
    print("Avrundet til",des_plass,"desimaler:",round(des_tall,des_plass)) 
