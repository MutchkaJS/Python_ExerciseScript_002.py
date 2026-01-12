# Exercise 1: Calculate the multiplication and sum of two numbers.
# This project comes from https://pynative.com/python-basic-exercise-for-beginners/

def product_or_sum(a, b):
    """
    Return the product of a and b if it is
    less than or equal to 1000; otherwise return their sum.
    """
    product = a * b
    if product <= 1000:
        return product
    else:
        return a + b

# Example usage
num1 = 20
num2 = 30

result = product_or_sum(num1, num2)
print("Number a:" ,num1)
print("Number b: ",num2)
print("Result:", result)

# Test Cases
print("Test Case 1:", product_or_sum(30, 20))
print("Test Case 2:", product_or_sum(12, 17))