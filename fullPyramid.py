n = int(input("Enter the size of the pyramid: "))
for i in range(1, n + 1):
    print(' ' * (n - i), end='')
    print('* ' * i)
