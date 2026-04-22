N=int(input("Enter the  number of days: "))
d=[]
print("Enter the list element")
for i in range(N):
    val=int(input( ))
    d.append(val)
total=0
for i in d:
    total+=i
print("Total Stock: ",total)
print("Average Size: ",(total/N))
