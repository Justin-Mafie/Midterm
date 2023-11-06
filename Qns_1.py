# Define a function to calculate T(n) based on the provided recursive formula
def calculate_T(n):
    # Base case: When n is 1, T(n) is 1
    if n == 1:
        return 1
    # Recursive case: For n > 1, T(n) = T(n-1) + 2n
    else:
        # Calculate T(n-1) recursively and add 2n
        return calculate_T(n - 1) + 2 * n

# Define the value of n for which you want to calculate T(n)
n = 200

# Call the function to calculate T(n)
result = calculate_T(n)

# Print the result
print(f'T({n}) = {result}')

