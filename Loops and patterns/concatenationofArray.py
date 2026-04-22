li=list(map(int,input("Enter the list: ").split()))
ans=[0]*(2*len(li))
for i in range(len(li)):
    ans[i]=li[i]
    ans[len(li)+i]=li[i]
print(ans)