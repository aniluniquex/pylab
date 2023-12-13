def cum_pro(lst):
    result = []
    cur = 1

    for n in lst:
        cur*=n
        result.append(cur)
    return result


lst = input("enter numbers with space").split(" ")
lst = [int(x) for x in lst]

print(f"The cummulative product of {lst} is {cum_pro(lst)}")