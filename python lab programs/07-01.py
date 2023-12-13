str=input("Enter a string to count characters :")
str=sorted(str)
d={}

for x in str:
    d[x]=str.count(x)
for u,v in d.items():
 print(u,':',v)


