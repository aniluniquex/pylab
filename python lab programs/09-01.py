def first_diff(string1,string2):
    x=string1.split()
    y=string2.split()
    if(len(x) < len(y)):
        length=len(x)
    else:
        length=len(y)
    for i in range(length):
        if x[int(i)] == y[int(i)]:
            print("The location of string same")
        else:
            b=x[i]
            print("The location of string different at : ",int(i),"-->",b)
 
string1="hello you are learning python now"
string2="hello you are good at learning"
first_diff(string1, string2)