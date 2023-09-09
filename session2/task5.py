def find_sum_pair(numbers, target):
    num_set = set()
    
    for i in numbers:
        comp = target - i
        if comp in num_set:
            return i, comp
        
        num_set.add(i)

    return None

numbers = input("Enter a list of numbers separated by spaces: ")
# numbers = [int(num) for num in input_numbers.split()]

target = int(input("Enter the target number: "))

result = find_sum_pair(numbers, target)

if result:
    print(f"Yes: {result[0]} + {result[1]} = {target}.")
else:
    print("No")