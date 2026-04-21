#BMI Calculator with Health Advisory
weight=int(input("Enter the Weight: "))
Height=float(input("ENter the height: "))
bmi=weight/Height**2
print("BMI: ",bmi)
if bmi<18.5:
    print("UnderWeight")
elif bmi>=18.5 and bmi<=24.9:
    print("Normal")
elif bmi>=25.0 and bmi<=29.9:
    print("OverWeight")
else:
    print("Obese")
