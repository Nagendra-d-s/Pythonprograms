stock=[7,1,5,3,6,4]
mini=stock[0]
profit=0
for i in stock:
    if i<mini:
        mini=i
    profit=max(profit,i-mini)
print("Profit: ",profit)