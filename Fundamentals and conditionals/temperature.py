celsius=int(input("Enter the temperature (in degree Celsius): "))
f=celsius*(9/5)+32
k=celsius+273.15
print("F=",f)
print("K=",k)
if celsius<0:
    print("Freezing")
elif celsius>=0 and celsius<=15:
    print("Cold")
elif celsius>15 and celsius<=30:
    print("Pleasant")
else:
    print("Hot")
