#21

price = float(input("Enter the purchase price (<= 1.00): "))

if price > 1.00 or price <= 0:
    print("Invalid price. Must be between $0.00 and $1.00.")
else:
    change = round((1.00 - price) * 100)  

    quarters = change // 25
    change %= 25

    dimes = change // 10
    change %= 10

    nickels = change // 5
    change %= 5

    pennies = change

    print("Your change is:")
    if quarters: print(f"{quarters} quarters")
    if dimes: print(f"{dimes} dimes")
    if nickels: print(f"{nickels} nickels")
    if pennies: print(f"{pennies} pennies")
