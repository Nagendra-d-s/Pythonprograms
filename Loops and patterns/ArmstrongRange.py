n1=int(input("Enter the first number : "))
n2=int(input("Enter the second number: "))
if n2<n1:
    n2,n1=n1,n2
for i in range(n1,n2):
    order=len(str(i))
    temp=i
    total=0
    while temp>0:
        digit=temp%10
        total+=digit**order
        temp//=10
    if total==i:
        print(i,end=" ")