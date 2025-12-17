from geomery import area_circle as AC
from geomery import area_rectangle as AR

radius=int(input("enter radius:"))
length=int(input("enter length:"))
breadth=int(input("enter breadth:"))

area_circle=AC(radius)
print(f"area of circle: {area_circle}")

area_rectangle=AR(length,breadth)
print(f"area of rectangle:{area_rectangle}")