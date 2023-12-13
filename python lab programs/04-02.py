alpha = input("enter a letter:")

if alpha>='A' or alpha<='Z'and alpha>='a' and alpha<='z':
    if alpha=='a'or alpha=='A' or alpha=='e' or alpha=='E'or alpha=='i' or alpha=='I' or alpha=='O' or alpha=='o' or alpha=='u' or alpha=='U':
        print("It is vowel")
    else:
        print("not vowel")
else:
    print("not alphabet")