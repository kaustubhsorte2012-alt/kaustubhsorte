# Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

#original list
original_list = list(range(1, 11))

# Extract the first 5 elements
first_five = numbers[:5]

# Reverse the extracted elements
reversed_list = first_five[::-1]

# Print both lists
print("original list:", original_list)
print("Extracted list:", first_five)
print("Reversed list:", reversed_list)