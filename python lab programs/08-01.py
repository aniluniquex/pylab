def rev(str_lst):
    rev_words = [word[::-1]for word in str_lst]
    return rev_words

str_lst = ["hello","bye"]
reverse = rev(str_lst)
print(reverse)