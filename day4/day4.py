INPUT = "day4.in"

def overlap(p1, p2, total=True):
	if p1[0] > p2[0]:
		p1, p2 = p2, p1
	if total:
		if p2[0] >= p1[0] and p2[1] <= p1[1]:
			return True
		if p2[0] == p1[0]:
			return True
	else:
		if p1[0] <= p2[1] and p2[0] <= p1[1]:
			return True
	return False
	
with open(INPUT) as day4in:
	count1 = 0
	count2 = 0
	for line in day4in:
		p1, p2 = line.strip().split(',')
		p1, p2 = p1.split('-'), p2.split('-')
		p1, p2 = [int(p1[0]), int(p1[1])], [int(p2[0]), int(p2[1])]
		if overlap(p1, p2):
			count1 += 1
		if overlap(p1, p2, total=False):
			count2 += 1
	print(count1, count2)
