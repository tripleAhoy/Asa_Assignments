#17

for i in range(1, 11):
    for star in range(i):
        print('*', end='')
    print()

print()

for i in range(10, 0, -1):
    for star in range(i):
        print('*', end='')
    print()

print()

for i in range(10, 0, -1):
    for space in range(10 - i):
        print(' ', end='')
    for star in range(i):
        print('*', end='')
    print()

print()

for i in range(1, 11):
    for space in range(10 - i):
        print(' ', end='')
    for star in range(i):
        print('*', end='')
    print()
