numbers = input("Enter numbers separated by spaces: ")

# Split input and convert to integers
num_list = numbers.split()
num_list = [int(num) for num in num_list]

# Store in a set to remove duplicates
unique_numbers = set(num_list)

# Calculate statistics
count = len(unique_numbers)
total = sum(unique_numbers)
average = total / count
largest = max(unique_numbers)
smallest = min(unique_numbers)

# Print results
print("Unique numbers:", unique_numbers)
print("Count =", count)
print("Sum =", total)
print("Average =", average)
print("Max =", largest)
print("Min =",smallest)