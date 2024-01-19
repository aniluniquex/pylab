class Robot:
    pop = 0

    def __init__(self, name):
        self.name = name
        print(f"Initializing {self.name}")
        Robot.pop += 1

    def __del__(self):
        print(f"{self.name} is being destroyed")
        Robot.pop -= 1
        if Robot.pop == 0:
            print(f"{self.name} was the last one")
        else:
            print(f"There are still {Robot.pop} working")

    def hi(self):
        print(f"Greetings! My masters call me {self.name}")

    def howmany(self):
        print(f"There are {Robot.pop} robots")


x = Robot("r1-d1")
x.hi()
x.howmany()
y = Robot("r2-d2")
y.hi()
y.howmany()

print("Robots work")
print("Robots die")

del x
del y
# robot.howmany()  # Commented this line as it's not a valid usage

# Access the class variable directly to get the total count
print("Total robots remaining:", Robot.pop)

