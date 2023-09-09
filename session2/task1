def binarySearch(arr, start, end, x):
    if end >= start:
        mid = (end + start) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, start, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, end, x)

    else:
        return -1


arr = [2, 5, 7, 9, 15, 27, 34, 49, 40, 48, 52, 55]
x = int(input("Enter the element you want to test its existance: "))

result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Elemnt Found")
else:
    print("Element not Found")
