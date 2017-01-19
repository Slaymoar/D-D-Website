
def rollDie(number):
	counts = [0] * 6
	for i in range(number):
    	roll = random.randint(1,6)
    	counts[roll - 1] += 1
	return counts


array = rollDie(6)
print array
