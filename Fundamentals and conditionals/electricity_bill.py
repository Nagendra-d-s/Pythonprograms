n=int(input("Enter thee number of units Consumed: "))
bill_amt=0
if n<=100:
    bill_amt=n*1.50
elif n>100 and n<=200:
    t=n%100
    bill_amt=100*1.50+t*2.50
else:
    t=n%200
    bill_amt=150+250+t*4.00
print(bill_amt)
