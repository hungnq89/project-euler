for a in range(1, 500):
	for b in range(a,500):
		c = 1000 - (a + b)
		if a < b and b < c and (a*a)+(b*b)==(c*c):
			print a*b*c