def is_palimdrome(s):
    return s=="".join(reversed(s))
string=input("enter a string ")
if is_palimdrome(string):
    print("your string is a palindrome")

else: print("your string is not a palindrome")