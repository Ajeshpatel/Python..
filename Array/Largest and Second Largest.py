"""
Largest and Second Largest

You are given an array A of N integers.
Find the maximum sum of two distinct integers in the array.

Note: It is guaranteed that there exist at least two distinct integers in the array.

Input Format:
    The first line of input will contain a single integer T, denoting the number of test cases.
    Each test case consists of multiple lines of input.
        The first line of each test case contains single integer N — the size of the array.
        The next line contains N space-separated integers, denoting the array A.

Output Format:
For each test case, output on a new line, the maximum sum of two distinct integers in the array.

Constraints:
    1≤T≤1000
    2≤N≤105
    1≤Ai​≤1000
    The sum of N over all test cases does not exceed 2⋅10**5.

Sample 1:
Input:
4
3
4 1 6
7
3 7 2 1 1 5 3
5
8 2 9 4 9
2
1 2

Output:
10
12
17
3

Explanation:

Test case 1: The maximum sum of two distinct elements is 4+6=10 .

Test case 2: The maximum sum of two distinct elements is 7+5=12.

Test case 3: The maximum sum of two distinct elements is 8+9=17.

Test case 4: The maximum sum of two distinct elements is 1+2=3.
"""
# -----------------------------------SOLUTION---------------------------------------
t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    t -= 1
    # Your code goes here
    s = sorted(a)
    length = len(a)
    
    ans = s[length-1]
    for i in range(length-2, -1, -1):
        if(s[i]==s[i+1]):
            ans = ans
        else:
            ans = ans + s[i]
            break
            
    print(ans)
        
        
        