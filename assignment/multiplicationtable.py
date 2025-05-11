length = 9
print('      ', end='\t')
for i in range(1, length + 1):
	print( i, end='\t')
print('\n' + '-' * 75)

for i in range(1, length + 1):
	print(i, "|", end='\t') 
	for j in range(1, length + 1):
		print(i * j, end='\t')
	print()