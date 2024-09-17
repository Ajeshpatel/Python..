# Python program to print "Sum of Largest contiguous subarray"

def solution(N, arr):
    
    max_so_far = arr[0]
    curr_max = arr[0]
    
    for i in range(1, N):
        curr_max = max(arr[i], curr_max + arr[i])
        max_so_far = max(max_so_far, curr_max)
        
    print(max_so_far)
    
N = int(input())
arr = list(map(int, input().split()))
solution(N, arr)