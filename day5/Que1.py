import math

#print(math.pi)
#print(math.e)

r=math.sqrt(625)
upper=math.ceil(1.45)
lower=math.floor(1.45)
sin=math.sin(math.pi/2)
cos=math.cos(0)
ln=math.log(10)
log10=math.log10(1000)

#print(r)
#print(upper)
#print(lower)
#print(sin)
#print(cos)
#print(ln)
#print(log10)

r = float(input("Enter radius: "))
circumference = 2 * math.pi * r
area = math.pi * (r ** 2)

print("Circumference:", circumference)
print("Area:", area)