def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b!=0:
        return a/b
    else:
        print("invalid operation!!")

a=int(input("Enter a number 1:"))
b=int(input("Enter a number 2:"))

print("1.Addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")

choice=int(input("Enter your choice:"))

if choice==1:
    print("addition:",add(a,b))
elif choice==2:
    print("sub:",sub(a,b))
elif choice==3:
    print("multiplication:",mul(a,b))
elif choice==4:
    print("division:",div(a,b))
else:
    print("Invalid choice:")

