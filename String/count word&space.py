#  Python Program to Calculate the Number of Words and the Number of space Present in a String

n = input("Enter a string:- ")
space =0

for i in n:
    if(i==" "):
        space = space+1

print("total no. of space is:- ",space)
print("total no. of word is:- ", space+1)
    