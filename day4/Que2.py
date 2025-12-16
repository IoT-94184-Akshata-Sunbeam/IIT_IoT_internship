
n=int(input("Enter distance:"))
KiloToMeter=lambda n:n*1000
MeterToCentiMeter=lambda n:n*100
CentiTomiliMeter=lambda n:n*10
feetToinches=lambda n:n*12
inchToCentiMeter=lambda n:n*2.54

print(f"kilometer to meter={KiloToMeter(n)}")
print(f"Meter To CentiMeter={MeterToCentiMeter(n)}")
print(f"Centi To miliMeter={CentiTomiliMeter(n)}")
print(f"feet To inches={feetToinches(n)}")
print(f"inches to centimeter ={inchToCentiMeter(n)}")