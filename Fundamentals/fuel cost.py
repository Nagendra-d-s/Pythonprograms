import math
distance=int(input("Enter the distance in KM: "))
mileage=int(input("Enter the Truck mileage(km per litre): "))
price=int(input("Enter the unit fuel price: "))
toll=int(input("Enter the toll price: "))
wage=int(input("Enter the daily wage: "))
Budget=int(input("Enter the Budget for the trip "))
fuel_cost=(distance/mileage)*price
days=math.ceil(distance/500)
driverCost=wage*days
tripCost=fuel_cost+toll+driverCost
remain=abs(tripCost-Budget)
print("Total cost=",tripCost)
if tripCost>Budget:
    print("Over Budget by ",remain)
else:
    print("Within Budget,savings=",remain)