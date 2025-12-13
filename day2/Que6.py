n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 1: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter  choice: "))

if choice == 1:
    print(f"{n1} + {n2} = {n1 + n2}")
elif choice == 2:
    print(f"{n1} - {n2} = {n1 - n2}")
elif choice == 3:
    print(f"{n1} * {n2} = {n1 * n2}")
elif choice == 4:
    print(f"{n1} / {n2} = {n1 / n2}")
else:
    print("Invalid choice!")