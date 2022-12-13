from functools import cmp_to_key

INPUT = "day13.in"

def read_input(infile):
	pairs = []
	pair = []
	for line in infile:
		line = line.strip()
		if line == '':
			pairs.append(pair)
			pair = []
			continue
		pair.append(eval(line))
	pairs.append(pair)
	return pairs

def compare(p1, p2):
	p1t = type(p1)
	p2t = type(p2)
	cmp = None
	if p1t == int and p2t == int:
		if p1 < p2:
			cmp = 1
		elif p1 > p2:
			cmp = -1
		else:
			cmp = 0
	elif p1t == list and p2t == list:
		cmp = 0
		for i in range(len(p1)):
			if i >= len(p2):
				cmp = -1
				break
			else:
				cmp = compare(p1[i], p2[i])
				if cmp != 0:
					break
		if cmp == 0:
			if len(p1) < len(p2):
				cmp = 1
	elif p1t == list and p2t == int:
		cmp = compare(p1, [p2])
	elif p1t == int and p2t == list:
		cmp = compare([p1], p2)
	
	return cmp

pairs = read_input(open(INPUT))
# print(pairs)
total = 0
for i, pair in enumerate(pairs):
	cmp = compare(pair[0], pair[1])
	# print(cmp)
	if cmp == 1:
		# print(i)
		total+= (i+1)
print(total)

allitems = []
for pair in pairs:
	allitems.append(pair[0])
	allitems.append(pair[1])

allitems.append([[2]])
allitems.append([[6]])
# print(allitems)
allitems = sorted(allitems, key=cmp_to_key(compare), reverse=True)
print((allitems.index([[2]])+1) * (1+allitems.index([[6]])))
