#solution 1
raw_input = []
with open("problem008.in") as f:
    for line in f:
        raw_input.append(line)

input = map(int, "".join(raw_input).replace("\n",""))

product = []

for i in range(0, len(input)):
	if(i<=len(input)-5):
		product.append(input[i]*input[i+1]*input[i+2]*input[i+3]*input[i+4])

print max(product)
