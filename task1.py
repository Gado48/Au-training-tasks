x = int(input("Enter the height you desire (1 to 8): "))

while x < 1 or x > 8:
    print("invalid")
    x = int(input("please make sure you enter a positive integer between 1 to 8: "))

if x > 1 and x < 8:
    for i in range(1, x + 1):
        spaces = " " * (x - i)
        hashes = "#" * i
        print(spaces + hashes + " " + hashes)