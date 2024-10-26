# check number is prime or not

num1 = int(input("Enter a number:"))
count = 0

if(num1>1):
    for i in range(1,num1+1):
        if(num1%i == 0):
            count = count+1
    
    if(count == 2):
        print("number is prime number")
    else:
        print("number is not prime number")
