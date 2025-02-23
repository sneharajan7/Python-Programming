def print_pyramid(size):
    for row in range(0, size):
        for col in range(0, row+1):
            print("*", end=" ")
        print("")


size = int(input("Enter the size of the Pyramid : "))
print_pyramid(size)