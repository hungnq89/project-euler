#solution 1
total = 0
for i in range(1,1000):
	if i%3==0 or i%5==0:
		total+=i
print total

#solution 2
print sum(set(range(0,1000,3))|set(range(0,1000,5)))