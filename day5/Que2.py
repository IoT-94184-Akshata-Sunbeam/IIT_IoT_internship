import calulator

a=int(input("enter a number a:"))
b=int(input("enter a number b:"))

add = calulator.add(a,b)
print(f"addition = {add}")

sub = calulator.subtract(a,b)
print(f"substraction = {sub}")

multiplication=calulator.multiply(a,b)
print(f"multiplication = {multiplication}")

division = calulator.divide(a,b)
print(f"division = {division}")


