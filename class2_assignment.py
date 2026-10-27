c_name = input("Enter your name: ")
item_count = int(input("Enter the number of items: "))
unit_price = float(input("Enter the unit price: "))
toal_cost = item_count * unit_price
# Bonus add 13% vat with round(total*1.12,2)
 

print(f"Total cost for {c_name} including tax is: {round(toal_cost * 1.13, 2)}")

