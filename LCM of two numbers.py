a = int(input("first number: ")) 
b = int(input("second number: ")) 

x = a
y = b

while y!= 0:
    temp = y
    y = x % y
    x = temp

gcd = x
lcm = (a * b) // gcd

print(lcm) 
