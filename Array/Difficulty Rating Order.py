"""
Difficulty Rating Order

Our Chef has some students in his coding class who are practicing problems. Given the difficulty of the problems
that the students have solved in order, help the Chef identify if they are solving them in non-decreasing order 
of difficulty. Non-decreasing means that the values in an array is either increasing or remaining the same,
but not decreasing. That is, the students should not solve a problem with difficulty d1​, and then later a 
problem with difficulty d2​, where d1​>d2​.

Output “Yes” if the problems are attempted in non-decreasing order of difficulty rating and “No” if not.

Input Format:
    The first line of input will contain a single integer T, denoting the number of test cases. 
    The description of the test cases follows.
    Each test case consists of 2 lines of input.
        The first line contains a single integer N, the number of problems solved by the students
        The second line contains N space-separate integers, the difficulty ratings of the problems attempted
        by the students in order.

Output Format:
    For each test case, output in a new line “Yes” if the problems are attempted in non-decreasing order of
    difficulty rating and “No” if not. The output should be printed without the quotes.

Each letter of the output may be printed in either lowercase or uppercase. 
For example, the strings yes, YeS, and YES will all be treated as equivalent.

Constraints:
    1≤T≤100
    2≤N≤100
    1≤ difficulty of each problem ≤5000

Sample 1:
Input:
4
3
1 2 3
3
1 1 2
5
100 200 300 400 350
5
1000 2000 5000 3000 1000

Output:
Yes
Yes
No
No

Explanation:

Test case 1: 1≤2≤3. The students have solved problems in increasing order, and so the answer is "Yes".

Test case 2: 1≤1≤2. The students have solved problems in non-decreasing order, and so the answer is "Yes".

Test case 3: 400>350, but the students have solved a 400-difficulty level problem before solving a 
350-difficulty problem. The students have not solved problems in non-decreasing order, and so the answer is "No".

Test case 4: 5000>3000, but the students have solved a 5000-difficulty level problem before solving a 
3000-difficulty problem. The students have not solved problems in non-decreasing order, and so the answer is "No".
"""
# ----------------------------------------SOLUTION-------------------------------------------
t = int(input())

while t > 0:
    n = int(input())
    d = list(map(int, input().split()))
    # Your code goes here
    s = sorted(d)
    
    if(d==s):
        print("YES")
    else:
        print("NO")
        
    t -= 1
    