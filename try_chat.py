def get_divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

# Example usage with a number that has divisors
num = 100
result = get_divisors(num)
print(f"The divisors of {num} are: {result}")

# Example usage with a number that has no divisors
num = 13
result = get_divisors(num)
print(f"The divisors of {num} are: {result}")
# Example usage with a number that has divisors
num = 100
result = get_divisors(num)
print(f"The divisors of {num} are: {result}")
