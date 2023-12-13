str = input("enter a string:")
size = int(input("enter the size to check overlap:"))

newlist = []

if size>len(str):
    print("Invalid")
else:
    for i in range(len(str)-size+1):
        newlist.append(str[i:i+size])
    print(newlist)