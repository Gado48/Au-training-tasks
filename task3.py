x = int(input("Enter the amount of money: "))

if x < 0:
    print("invalid: there is no chance I take money from you, I am here to serve sir")
    x = int(input("Enter the amount of money(postivie intiger): "))

i1 = 0
while x >= 200:
    x = x - 200
    i1 = i1 + 1

if i1 != 0:
    print(i1, end="")
    print("x 200 LE")

i2 = 0
while x >= 100:
    x = x - 100
    i2 = i2 + 1

if i2 != 0:
    print(i2, end="")
    print("x 100 LE")

i3 = 0
while x >= 50:
    x = x - 50
    i3 = i3 + 1

if i3 != 0:
    print(i3, end="")
    print("x 50 LE")

i4 = 0
while x >= 20:
    x = x - 20
    i4 = i4 + 1

if i4 != 0:
    print(i4, end="")
    print("x 20 LE")

i5 = 0
while x >= 10:
    x = x - 10
    i5 = i5 + 1

if i5 != 0:
    print(i5, end="")
    print("x 10 LE")

i6 = 0
while x >= 5:
    x = x - 5
    i6 = i6 + 1

if i6 != 0:
    print(i6, end="")
    print("x 5 LE")

i7 = 0
while x >= 1:
    x = x - 1
    i7 = i7 + 1

if i7 != 0:
    print(i7, end="")
    print("x 1 LE")
