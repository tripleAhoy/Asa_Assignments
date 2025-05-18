#1
passes = 0
failures = 0
counter = 0

while counter <= 9:
	result = int(input('Enter result (1 = pass, 2 = fail): '))
	if result <= 0 or result > 2:
		print('Invalid')

	else:
		if result == 1:
			passes += 1

		counter += 1
	failures = counter - passes

print('Passed:', passes)
print('Failed:', failures)
