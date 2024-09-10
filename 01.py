t = int(input())

count_even = 0
count_odd = 0
for i in range(1, t+1):
    if(i%2 == 0):
        count_even += 1
    else:
        count_odd += 1
        
print("total even no. is:-", count_even)
print("total odd no. is:-", count_odd)