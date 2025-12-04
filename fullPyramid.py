# Input
N = int(input("Enter the size of the pyramid: "))

# Loop through each level of the pyramid
for i in range(1, N + 1):
    # Print spaces to center the stars
    print(' ' * (N - i), end='')
    
    # Print the stars with a space between them
    print('* ' * i)
