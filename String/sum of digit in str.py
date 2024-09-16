# Write A Python Program To Compute Sum Of Digits Of A Given String.

s = input("Enter a string:-")

all_digit = ""
sum_of_digit = 0

for i in range(0, len(s)):
    if(s[i].isdigit()):
        all_digit += s[i] + ","
        sum_of_digit += int(s[i])
        
print("Original string:- ", s)
print("All_digit:- ",all_digit)
print("Sum of digits:- ",sum_of_digit)