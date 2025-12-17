import operations.arithmetic as Ar
import operations.string_ops as str

a=int(input("enter a number a:"))
b=int(input("enter a number b:"))


add=Ar.addition(a,b)
print(f"addition = {add}")

multiplication=Ar.mul(a,b)
print(f"multiplication = {multiplication}")

s=input("enter a string:")

rev=str.reverse_string(s)
vow=str.count_vowels(s)

print(f"Revrse string:{rev}")
print(f"vowel count:{vow}")
