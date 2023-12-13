val1=input("Give an input : ")
val2=input("Give another input : ")
try:
    print("Result is : ",int(val1)+int(val2))
except ValueError as ve:
    print("Character conversion with int() is invalid!!")
