def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
def power(base,exp):
    if exp==0:
     return 1
    else:
       return base * power(base,exp-1)
    
num=int(input("Enter a number:"))
base=int(input("Enter a base:"))
exponent=int(input("Enter a exponent:"))
print("Factorial :", factorial(num))
print(base, "raised to the power", exponent, "is:", power(base, exponent))