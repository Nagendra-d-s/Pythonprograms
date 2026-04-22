code=1234
count=3
while count>0:
    value=int(input("Enter the Code: "))
    if value==code:
        print("Access Granted")
        break
    else:
        count-=1
        if count==0:
            print("Account Locked")
            break
        else:
            print(f"INCORRECT,{count} attempts remaining")
