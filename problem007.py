import math
import time

def is_prime(num):
    if(num == 2): return True
    if(num % 2 == 0): return False
    if(num < 9): return True
    if(num % 3 == 0): return False
    x = int(math.sqrt(num)) + 1
    for i in range(5,x):
        if(n%i==0):
            return False
    return True

count = 0
n = 2
while(count < 10001):
    if(is_prime(n)):
        count = count + 1
    if(count==10001):
        break;
    n = n + 1
  
print n
