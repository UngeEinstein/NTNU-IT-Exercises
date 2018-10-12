Sum=0
tol=0.001
n=0
r=0.5
while (2-Sum)>tol:
    Sum=(1-r**(n+1))/(1-r)
    n+=1
print(Sum)
print("For å være innenfor toleransegrensen: {0} , kjørte løkken {1} ganger.".format(tol,n))
print("Diferansen mellom grenseverdien og faktisk verdi: ", 2-Sum)