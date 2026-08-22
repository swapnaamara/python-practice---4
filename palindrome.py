n = int(input("Enter a number: ")) 
original = n
r = 0
while n > 0
    r = r*10 + n%10
    n = n//10

if original == r:
    print("Palindrome") 

else:
    print("Not Palindrome")
