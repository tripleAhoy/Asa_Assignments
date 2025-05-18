#15

e_approx = 0
factorial = 1

for number in range(10):
	if number > 0:
		factorial *= number

	term = 1 / factorial
	e_approx += term

	print(f" {number + 1}\t { e_approx:.6f}")

print(f" Final approximation after 10 terms: {e_approx:.6f}")
