a = int(input("first number: ")) 
b = int(input("second number: ")) 

while b != 0:
    temp = b
    b = a % b
    a = temp

print(a) 
