a=[10,11,12,13]
b=[20,21,22,23,24]
c=[50,51,52,53]
for i in a:
    for j in b:
        if i!=j:
            x=j
            c.append(x)
            break;

    for k in c:
        if i not in c:
            c.append(i)
        else:
            break
print(c)
