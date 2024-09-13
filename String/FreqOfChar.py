# 7: write a program to find the frequency of character in a string

n = input("Enter any string:-")
search = input("Enter search character:-")
count = 0
for i in n:
    if(i==search):
        count += 1

print("number of time found:- ",count)