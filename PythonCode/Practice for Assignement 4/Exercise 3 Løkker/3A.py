i=0
y=0
for x in range(0,103):
    if (x%3==0):
        i+=1
        y+=x
        if i>10 or y>120:
            break
        print(x)
        print(i)
        print(y)