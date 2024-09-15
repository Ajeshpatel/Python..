# Python program to check if two strings are anagram or not.

# Listen         EILNST          Silent :Listen and Silent are anagram because after sorted both are same.
# Traingle         AEGILNRT          Integral :Traingle and Integral are anagram because after sorted both are same.

A = input("Enter First string:- ")
B = input("Enter second string:- ")

A_result = sorted(A)
B_result = sorted(B)

if(A_result == B_result):
    print("String are Anagram")
else:
    print("String are not Anagram")
    
