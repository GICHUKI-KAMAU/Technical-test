def reverse_integer(n):
    sign = -1 if n < 0 else 1
    
    # Converting the number to a string, reversing the string
    reversed_str = str(abs(n))[::-1]
    
    # Convert the reversed string back to integer and reapply the sign
    reversed_int = int(reversed_str) * sign
    
    return reversed_int

# Testing the function with different integers
test_cases = [500, -56, -90, 91]

for num in test_cases:
    result = reverse_integer(num)
    print(f"Input: {num} -> Reversed: {result}")
