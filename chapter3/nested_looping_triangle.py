#18

rows = 10

for i in range(1, rows + 1):
    for j in range(i):
        print('*', end='')
    print(' ' * (rows - i), end='   ')

    for j in range(rows - i + 1):
        print('*', end='')
    print(' ' * (i - 1), end='   ')

    for space in range(i - 1):
        print(' ', end='')
    for star in range(rows - i + 1):
        print('*', end='')
    print('   ', end=' ')

    for space in range(rows - i):
        print(' ', end='')
    for star in range(i):
        print('*', end=' ')

    print()
