# python program to print the initial of a name and with surname.
# title()  method used for, capatalize 1st char and small letter rest of other char in Word.
# upper()  method used for, capatalize word.

name = input("Enter any full name:-")

list = []
list = name.split()
Sort_name = ""
length = len(list)

for i in range(length-1):
    s = list[i]
    Sort_name = Sort_name + s[0].upper() + "."
    
Sort_name = Sort_name + list[length-1].title()

print(Sort_name)