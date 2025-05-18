#6

prompt2 = ' '
prompt1 = input('What is your problem? ')
if prompt1 == ' ' or prompt1 == '':
	print('invalid input')
else:
	while prompt2 != 'yes' and prompt2 != 'no': 
		prompt2 = input("Have you had this problem before ('yes' or 'no')? ")

		if prompt2 != 'yes' and prompt2 != 'no':
			print('invalid input.')
	

		else:
			if prompt2 == 'yes':
				print('Well, you have it again.')

			else:
				print('Well, you have it now.')
