'''
Python Exercise 002

Write Python code to iterate through the first 10 numbers and, in each iteration,
print the sum of the current and previous number.

This will be done using a range() function and
a calculating a simple sum.
'''

# Generate a list of ten numbers.

previous = 0  # Initializes the var 'previous' = 0 to hold place values
print("Printing current and previous number sum up to 10th number:")

for i in range(10): # begin creating a series of 10 numbers
    current_sum = i + previous  # create current_sum
    print(f"Current Number {i}, Previous Number {previous}, Sum: {current_sum}")
    previous = i

