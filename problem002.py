memo = [1, 2]
a, b = 1, 2
f = 0
while (f < 4000000):
	a, b = b, b + a
	memo.append(f)
	f = a + b

even_fib = [x for x in memo if x % 2 == 0]

print "Even fibonaci %s" % sum(even_fib)
