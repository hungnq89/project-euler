from math import sqrt
from math import ceil

n_count = 0
n = 1
divisor = 0
def generate_next_trianble(n):
  return int(n*(n+1)/2)


def get_factors_count(num):
  n_max = ceil(sqrt(num))
  n_factors = 0
  for n in range(1, int(n_max)):
    if num % n == 0:
      n_factors+=1
      if(n != (num // n)):
        n_factors+=1
  return n_factors

init = 1

while divisor <= 500:
  triangle = generate_next_trianble(init)
  divisor = get_factors_count(triangle)
  init+=1
  if(divisor>=500):
    print(triangle)
  
  