def is_prime(num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                return False
            return True
        else:
            return True
        
def next_prime(num):
    i = num+1
    while True:
        if is_prime(i):
            return i
        i = i+1

num = int(input("enter a number:"))
print(f"the next prime of {num} is {next_prime(num)}")