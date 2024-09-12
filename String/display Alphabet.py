# Python Program to display all alphabets from A to Z.

def char():
    for i in range(65, 91): # 65 == A, 90 == Z.
        print(chr(i), end=" ")
    
    print(" ")

    for i in range(97, 123):   # 97 == a, 122 == z.
        print(chr(i), end=" ")
        
char()