def sum_of_digits(number):
    digit_sum = 0
    while number > 0:
        digit = number % 10
        digit_sum += digit
        number //= 10
    return digit_sum

# List of numbers
numbers = [56, 57, 42, 36, 98, 13]

# Iterate through the list and call the 'sum_of_digits' function
for num in numbers:
    result = sum_of_digits(num)
    print(f"The sum of the digits of {num} is {result}.")
