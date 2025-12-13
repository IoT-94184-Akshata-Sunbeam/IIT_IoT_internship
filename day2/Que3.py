n=int(input("Enter a number:"))

a=0
b=1

if n>0:
    for i in range(n):
        print(a)
        c=a+b
        a=b
        b=c
else:
    print("Enter a possitive integer!!")