length = float(input("enter length in feet: "))

print("---------conversions-----")
print("1. To Inches")
print("2. To Yards")
print("3. To miles")
print("4. To Millimeters")
print("5. To Centimeters")
print("6. To Meters")
print("7. To Kilometers")

option = int(input("enter the option:"))

if option==1:
    inches = length*12
    print("The length in inches is",inches)
elif option==2:
    yards = length/3
    print("The length in yards is",yards)
elif option==3:
    miles = length/5280
    print("The length in miles is",miles)
elif option==4:
    Millimeters = length*305
    print("The length in millimeters is",Millimeters)
elif option==5:
    cm = length*30.48
    print("The length in cm is",cm)
elif option==6:
    m = length/3.281
    print("The length in m is",m)
elif option==7:
    km = length/3281
    print("The length in km is ",km)

