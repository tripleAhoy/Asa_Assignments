purchase = int(input('Enter purchase amount: '))

discount = 0
discount_remove = 0
discount_price = 0

if purchase < 1000:
	print('invalid amount')
else:
	if purchase >= 1000 and purchase <= 10000:
		discount = 5 // 100
		discount_remove = purchase * 5 // 100
		discount_price = purchase - discount_remove
		formatted_price = f"{discount_price:,.2f}"
		print(formatted_price)

	if purchase > 10000 and purchase <= 50000:
		discount = 10 // 100
		discount_remove = purchase * 10 // 100
		discount_price = purchase - discount_remove
		formatted_price = f"{discount_price:,.2f}"
		print(formatted_price)

	if purchase > 50000:
		discount = 20 // 100
		discount_remove = purchase * 20 // 100
		discount_price = purchase - discount_remove
		formatted_price = f"{discount_price:,.2f}"
		print(formatted_price)
