#14

pi_approx = 0.0
denominator = 1
sign = 1
term_count = 0
	
target1 = 3.14
target2 = 3.141
target3 = 3.1415
target4 = 3.14159

achieved1 = False
achieved2 = False
achieved3 = False
achieved4 = False
	
while not (achieved1 and achieved2 and achieved3 and achieved4):
	term = sign * 4 / denominator
	pi_approx += term
	term_count += 1
	print(f"{term_count}\t {pi_approx:.10f}")
	
	if not achieved1 and abs(pi_approx - target1) < 0.000005:
		achieved1 = True
		print(f"\nAchieved' {target1} after {term_count} terms")

	if not achieved2 and abs(pi_approx - target2) < 0.000005:
		achieved2 = True
		print(f"\nAchieved {target2} after {term_count} terms")

	if not achieved3 and abs(pi_approx - target3) < 0.000005:
		achieved3 = True
		print(f"\nAchieved {target3} after {term_count} terms")

	if not achieved4 and abs(pi_approx - target4) < 0.000005:
		achieved4 = True
		print(f"\nAchieved {target4} after {term_count} terms")

	denominator += 2
	sign *= -1

print("Final approximation:", pi_approx)
