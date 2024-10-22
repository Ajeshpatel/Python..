"""
Chef and Happy String

Chef has a string SS with him. Chef is happy if the string contains a contiguous substring of length 
strictly greater than 2 in which all its characters are vowels.

Determine whether Chef is happy or not.

Note that, in english alphabet, vowels are a, e, i, o, and u.

Input Format:
    First line will contain T, number of test cases. Then the test cases follow.
    Each test case contains of a single line of input, a string SS.

Output Format:
For each test case, if Chef is happy, print HAPPY else print SAD.

You may print each character of the string in uppercase or lowercase 
(for example, the strings hAppY, Happy, haPpY, and HAPPY will all be treated as identical).

Constraints:
    1≤T≤10001≤T≤1000
    3≤∣S∣≤1000, where ∣S∣ is the length of S.
    S will only contain lowercase English letters.

Sample 1:
Input:
4
aeiou
abxy
aebcdefghij
abcdeeafg

Output:
Happy
Sad
Sad
Happy

Explanation:

Test case 1: Since the string aeiou is a contiguous substring and consists of all vowels and has a length > 2,
Chef is happy.

Test case 2: Since none of the contiguous substrings of the string consist of all vowels and have a length > 2,
Chef is sad.

Test case 3: Since none of the contiguous substrings of the string consist of all vowels and have a length > 2,
Chef is sad.

Test case 4: Since the string eea is a contiguous substring and consists of all vowels and has a length > 2,
Chef is happy.
"""
# ------------------------------------------------SOLUTION-----------------------------------------------
t = int(input())

while t > 0:
    s = input()
    # Your code goes here
    
    count = 0
    ans = 0
    for i in s:
        if i in "aeiou":
            count += 1
            if(count > 2):
                ans = 1
        else:
            count = 0
            
    if(ans > 0):
        print("Happy")
    else:
        print("Sad")
    
    t -= 1