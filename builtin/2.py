def count(s):
    upper_count=0
    lower_case_count=0

    for c in s:
        if c.isupper():
            upper_count+=1
        elif c.islower():
            lower_case_count+=1

    return upper_count, lower_case_count
    
string=input("enetr a string ")
upper, lower= count(string)

print("upper_count is ",  upper)
print("lower_count is ", lower)


        