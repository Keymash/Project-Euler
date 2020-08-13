# find the sum of all multiples of 3 and 5 up to 1000

#Expected Answer: 233168
y = 0
for x in range(0,1000):
	if  x%3==0:
		y+=x 
	elif x%5==0:
		y+=x

print(y)
