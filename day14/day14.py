INPUT = "day14.in"

def read_input(infile):
	paths = []
	maxx = -1
	maxy = -1
	for line in infile:
		x = [l.strip().split(',') for l in line.split('->')]
		x = [(int(l[0]), int(l[1])) for l in x]
		maxx = max(maxx, max([e[0] for e in x]))
		maxy = max(maxy, max([e[1] for e in x]))
		paths.append(x)

	return paths, maxx, maxy

def process_paths(paths, maxx, maxy):
	m = [['.' for _ in range(maxx+1)] for _ in range (maxy+1)]
	
	# print(maxx, maxy, len(m[0]), len(m))

	for p in paths:
		s = p[0]
		for i in range(1, len(p)):
			e = p[i]
			if s[0] == e[0]:
				x = s[0]
				ys, ye = min(s[1], e[1]), max(s[1], e[1])
				for y in range(ys, ye+1):
					m[y][x] = '#'
			else:
				y = s[1]
				xs, xe = min(s[0], e[0]), max(s[0], e[0])
				for x in range(xs, xe+1):
					m[y][x] = '#'
			s = e
	return m

def print_map(m):
	ms = ''
	for r in m:
		ms += '\n' + ''.join(r)
	print(ms)	

def drop_sand(m, s):
	x, y = s[0], s[1]
	did_exit = False
	while(True):
		if x >= maxx or y >= maxy:
			did_exit = True
			break
		elif m[y+1][x] == '.':
			x, y = x, y+1
		elif m[y+1][x-1] == '.':
			x, y = x-1, y+1
		elif m[y+1][x+1] == '.':
			x, y = x+1, y+1
		else:
			break
	m[y][x] = 'o'
	return did_exit

def drop_sand_2(m, s):
	x, y = s[0], s[1]
	
	if m[y][x] == 'o':
		return True

	while(True):
		if y == len(m) - 1:
			break
		elif m[y+1][x] == '.':
			x, y = x, y+1
		elif m[y+1][x-1] == '.':
			x, y = x-1, y+1
		elif m[y+1][x+1] == '.':
			x, y = x+1, y+1
		else:
			break

	m[y][x] = 'o'

	return False

paths, maxx, maxy = read_input(open(INPUT))
m = process_paths(paths, maxx, maxy)

# soln1
total = 0
while(True):
	did_exit = drop_sand(m, (500, 0))
	if not did_exit:
		total += 1
	else:
		break
print(total)

# soln2
m = process_paths(paths, maxx + 500, maxy + 1)
total = 0
while(True):
	filled = drop_sand_2(m, (500, 0))
	if not filled:
		total += 1
	else:
		break
# print_map(m)
print(total)
