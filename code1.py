import re
fname=("abcd.txt")
fo=open(fname)

fh=fo.read()
print(fh)
print(fh[2])
line=re.findall('[0-9]+',fh)
list=[int(i) for i in line]
sum=0
for j in list:
    sum=sum+j
print(sum)
