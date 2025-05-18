#10

principal = 1000
rate = 7 / 100
nyears = 30

for nyears in range(1, nyears + 1):
	amount = principal * (1 + rate) ** nyears
	print(f"\n {nyears} \t{amount:,.2f}")
