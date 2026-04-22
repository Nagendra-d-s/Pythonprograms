amount = int(input("Enter the amount: "))
is_member = int(input("Enter 1 for Member otherwise Enter 0: "))

# Slab discount
if amount <= 500:
    discount = 0
elif amount <= 1000:
    discount = 0.10
elif amount <= 2000:
    discount = 0.15
else:
    discount = 0.20

# Extra member discount
if is_member == 1:
    discount += 0.05

# Calculate total
total = amount - (amount * discount)

print("Final Amount:", total)