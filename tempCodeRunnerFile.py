des_tall=float(input("Gi inn et desimaltall: "))
des_plass=int(input("Antall desimaler i avrunding: "))
avrunde=round(des_tall+10**(-(des_plass+1)),des_plass)
print(format(des_tall,"."+str(des_plass)+"f"))