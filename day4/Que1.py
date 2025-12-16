n=int(input("Enter distance :"))
def kiloTomet():
    return n*1000


def metToCenti():
    return n*100


def CentiToMili():
    return n*10



def FeetToInch():
    return n*12


def InchToCenti():
    return n*2.54




def Distance_convertor(n, operation):
    return operation(n)

print("distance in kilometer to meter :",kiloTomet(),"meters")
print("distance in meter to centimeter :",metToCenti(),"centimeters")
print("distance in centimeter to milimeter :",CentiToMili(),"milimeters")
print("distance in feet to inch:",FeetToInch(),"inch")
print("distance in inch to centimeter :",InchToCenti(),"centimeters")
