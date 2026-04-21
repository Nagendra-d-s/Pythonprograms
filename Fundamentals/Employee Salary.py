basic=int(input("Enter the salary: "))
hr=0.2*basic
da=0.5*basic
pf=0.12*basic
gross=basic+hr+da
tax=0.1*gross
print("Gross Salary:",gross)
print("Total Deduction:",(pf+tax))
print("Net Salary: ",(gross-(pf+tax)))