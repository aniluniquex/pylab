class Person():
    def __init__(self,name):
        self.name=name
    def nameLength(self):
        print("Length of the name:%d characters"%(len(self.name)))

p1=Person(input("Enter a string : "))
p1.nameLength()
