INPUT = "day3.in"

with open(INPUT) as day3in:
	abc = 'abcdefghijklmnopqrstuvwxyz'
	p = {c:(i+1) for i,c in enumerate(abc)}
	p.update({c.upper():(i+27) for i,c in enumerate(abc)})
	# print(p)	

	total = 0
	lines = []
	threes_total = 0
	for r in day3in:
		lines.append(r.strip())
		u = set(r[:len(r) // 2]) & set(r[len(r) // 2:])	
		total += p[list(u)[0]]	
		if len(lines) == 3:
			u = set(lines[0]) & set(lines[1]) & set(lines[2])
			threes_total += p[list(u)[0]]
			lines = []
	print(total, threes_total)
