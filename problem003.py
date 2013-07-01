import math
factors = []

def is_prime_number(num):
    for i in range(2, num - 1):
        if(num % i == 0):
            return False
    return True


x = 600851475143
for i in range(1, int(math.sqrt(x) + 1)):
    if(x % i == 0):
        if(is_prime_number(i)):
            factors.append(i)

print max(factors)

