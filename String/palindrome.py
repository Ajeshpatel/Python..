# write a program to check given string is palindrome or not in python.

# method:1
# string  = input("enter a string:-")
# length_str = len(string)
# result = ""

# for i in range(1, length_str+1):
#     result = result + string[length_str - i]

# if(string == result):
#     print(string, ", will be a palindrome")


method:2
string  = input("enter a string:-")
result = ""

for i in string:
    result = i + result

if(string == result):
    print(string, ", will be a palindrome")

