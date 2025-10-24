total =0
print('=== Book Rental System ===')

while True: 
    a = input('Enter membership type(student, regular or premium): ')
    if a == "student":
        print("Price: $2.00")
        total+=2.00
        print(f"Current total: ${total}")
    elif a == "regular":
        print("Price: $4.00")
        total+=4.00
        print(f"Current total: ${total}")
    elif a == "premium":
        print("Price: $6.00")
        total+=6.00
        print(f"Current total: ${total}")
    elif a == "done":
        break
    else:
        print("Please enter the right rental service!")
print("=== Rental Summary ===")
print(f"Subtotal: ${total}")
if total >=15.00:
    print("Bulk rental discount: -$2.50")
    print("Final total: $",total-2.50)
else:
    print(f"Final total: ${total}")
print('Thank you for your rental!')