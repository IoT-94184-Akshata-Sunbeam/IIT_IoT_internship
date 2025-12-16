W=float(input("Enetr the weight in tons:"))


conversions=[
    lambda w:w*1000,
    lambda w:w*1000,
    lambda w:w*1000,
    lambda w:w*0.00000220462 
]
kilograms=conversions[0](W)
grams=conversions[1](kilograms)
miligram=conversions[2](grams)
pounds=conversions[3](miligram)

print(f"kilograms:{kilograms}","kg")
print(f"grams:{grams}","grams")
print(f"miligrams:{miligram}","miligrams")
print(f"pounds:{pounds}","pounds")
