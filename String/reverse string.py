# write a program to reverse String in python

# string  = input("enter a string:-")
# length_str = len(string)
# result = ""

# for i in range(1, length_str+1):
#     result = result + string[length_str - i]
# print(result)


# method:2
string  = input("enter a string:-")
result = ""

for i in string:
    result = i + result
print(result)

