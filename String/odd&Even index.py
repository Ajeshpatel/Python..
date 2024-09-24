"""
Odd and Even Index.
Python program to remove the characters which have odd index and Even index values of a given string
"""

# Method:1
# string = input("Enter a string:-")
# even = ""
# odd = ""

# for i in range(0, len(string)):
#     if(i%2 == 0):
#         even = even + string[i]
#     else:  # (i%2 != 0)
#         odd = odd + string[i]
        
# print("Even Index charecter of given String:-",even)
# print("Even Index charecter of given String:-",odd)


# Method:2
string = input("Enter a string:-")
even = ""
odd = ""

for i in range(0, len(string), 2):
    even = even + string[i]
        
for j in range(1, len(string), 2):
    odd = odd + string[j]

print("Even Index charecter of given String:-",even)
print("Even Index charecter of given String:-",odd)