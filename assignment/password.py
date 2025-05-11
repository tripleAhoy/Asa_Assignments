password = input('Enter password: ')
input_length = len(password)

if input_length <= 7:
	print('very weak')
if input_length == 8:
	print('weak')
if input_length >= 9 and input_length <= 16:
	print('strong')
if input_length > 16:
	print('very strong')