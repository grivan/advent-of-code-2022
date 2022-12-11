INPUT = "day6.in"

def signal(infile, size):
	buffer = []
	for l in infile:
		for i,c in enumerate(l):
			buffer.append(c)
			if len(buffer) > size:
				buffer.pop(0)
			if len(set(buffer)) == size:
				return i+1
	return None

print(signal(open(INPUT), 4))
print(signal(open(INPUT), 14))
