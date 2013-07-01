max = 2000000
prime = [True] * max;
prime[0] = False
prime[1] = False

for n in range(2, max):
	if(prime[n]):
		for i in range(n*n, max, n):
			prime[i] = False

print sum(key for key, value in enumerate(prime) if value == True)