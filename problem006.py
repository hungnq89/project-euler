# solution 1
sum_of_squares = 0
for x in range(1, 101):
    sum_of_squares += x*x

total = 0
for x in range(1,101):
    total +=x

square_of_sum = total**2

print square_of_sum - sum_of_squares

#solution 2

sum_of_squares = sum([i*i for i in range(1,101)])

square_of_sum = pow(sum(range(1,101)),2)

print square_of_sum - sum_of_squares

#solution 3: one line

print pow(sum(range(1,101)),2) - sum([i*i for i in range(1,101)])