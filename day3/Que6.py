
def add(n1,n2):
    return n1 + n2



def subtract(n1, n2):
    return n1 - n2



def multiply(n1, n2):
    return n1* n2



def divide(n1, n2):
    if n2 == 0:
        return "Division not possible"
    return n1 / n2


def calculate(n1, n2, operation):
    return operation(n1, n2)


n1=int(input("Enter a number 1:"))
n2=int(input("Enter a number 2:"))
print("Addition:", calculate(n1, n2, add))
print("Subtraction:", calculate(n1, n2, subtract))
print("Multiplication:", calculate(n1, n2, multiply))
print("Division:", calculate(n1, n2, divide))
print("Division by zero:", calculate(n1, 0, divide))
