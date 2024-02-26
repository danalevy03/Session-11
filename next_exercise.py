#write a function that takes an integer as parameter
# and returns a list of all the divisors of that number:

def divisors(n):
    divisor = []
    for i in range(1, n+1):
        if n % i == 0:
            divisor.append(i)
    return divisor

print(divisors(100))
