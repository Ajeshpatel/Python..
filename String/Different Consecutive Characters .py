"""
Different Consecutive Characters

Chef has a binary string S of length NN. Chef can perform the following operation on S:

    Insert any character (0 or 1) at any position in S.

Find the minimum number of operations Chef needs to perform so that no two consecutive characters are same in S.

Input Format:
    The first line contains a single integer T — the number of test cases. Then the test cases follow.
    The first line of each test case contains an integer N — the length of the binary string SS.
    The second line of each test case contains a binary string S of length N containing 00s and 11s only.

Output Format:
For each test case, output on a new line the minimum number of operations Chef needs to perform so that 
no two consecutive characters are same in S.

Constraints:
    1≤T≤100
    1≤N≤1000

Sample 1:
Input:
3
2
11
4
0101
5
00100

Output:
1
0
2

Explanation:

Test case 1: We can perform the following operations: 11→10​1.

Test case 2: We do not need to perform any operations.

Test case 3: We can perform the following operations: 00100→01​0100→010101​0.
"""

# -------------------------------------------SOLUTION---------------------------------------------
# cook your dish here
t = int(input())
for _ in range(t):
    N = int(input())
    S = input()
    
    c = 0
    for i in range(0, N-1):
        if(S[i]==S[i+1]):
            c+=1
    print(c)