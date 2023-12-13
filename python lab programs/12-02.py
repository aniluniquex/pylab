string=input("Enter list of values : ")
nlist=string.split(" ")
print("Enter the index to show the value : ")
ind=int(input())
try:
    print(nlist[ind] , " is the element at position",ind)
except IndexError:
    print("There is no element Index doesn't exists !..")
