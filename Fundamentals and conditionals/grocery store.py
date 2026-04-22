item=input("Enter the item name: ")
qty=int(input("Enter the quantity: "))
price=float(input("Enter the unit price: "))
is_member=int(input("Membership  status: "))

subtotal=qty*price
if is_member:
    disc=subtotal*0.1
    subtotal-=disc
gst=0
if subtotal>500:
    gst=0.05*subtotal
else:
    gst=0.12*subtotal
print("Total: ",(subtotal+gst))
