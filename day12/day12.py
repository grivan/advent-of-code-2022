INPUT = "day12.in"

def read_input(infile):
	m = []
	s = None
	e = None
	for i, line in enumerate(infile):
		line = list(line.strip())
		m.append(line)
		if 'S' in line:
			s = i, line.index('S')
		if 'E' in line:
			e = i, line.index('E')
	m[s[0]][s[1]] = 'a'
	m[e[0]][e[1]] = 'z'
	return m, s, e

def diff(a, b):
	abc = 'abcdefghijklmnopqrstuvwxyz'
	abc = {v:k for k,v in enumerate(abc)}
	return abc[b] - abc[a]

visited = set()
min_count = 999999

def traverse_dfs(grid, c, e, count):

	# this code has too long of a runtime
	
	global min_count
	h = len(grid)
	w = len(grid[0])
	
	visited.add(c)

	if e in visited:
		if count < min_count:
			min_count = count

	moves = [(0, -1), (0, 1), (1, 0), (-1, 0)]
	valid_moves = []
	for m in moves:
		x = c[0] + m[0]
		y = c[1] + m[1]
		if x > -1 and x < h and y > -1 and y < w:
			d = diff(grid[x][y], grid[c[0]][c[1]])
			if (x, y) not in visited and d >= -1:
				valid_moves.append((x,y))
		
	for move in valid_moves:
		traverse_dfs(grid, move, e, count+1)
	
	visited.remove(c)
	
def traverse_bfs(grid, c, e):

	queue = list()
	queue.append(c)
	visited = set()
	visited.add(c)
	h = len(grid)
	w = len(grid[0])
	previous = [[None for i in range(w)] for j in range(h)]
	
	n = 0
	while(len(queue) > 0):

		n += 1
		c = queue.pop(0)
		if c == e:
			# exit condition, now find the path traced so far
			path_len = 0
			x = e
			while(x):
				path_len += 1
				x = previous[x[0]][x[1]]
			return path_len - 1

		moves = [(0, -1), (0, 1), (1, 0), (-1, 0)]
		valid_moves = []
		for m in moves:
			x = c[0] + m[0]
			y = c[1] + m[1]
			if x > -1 and x < h and y > -1 and y < w:
				d = diff(grid[x][y], grid[c[0]][c[1]])
				if (x, y) not in visited and d >= -1:
					previous[x][y] = c[0], c[1]
					visited.add((x, y))
					queue.append((x, y))

	# print("no path found...")
	return -1
					
m, s, e = read_input(open(INPUT))
# print(m)
# print(s, e)
# DFS is too slow here, so implemented BFS
# traverse_dfs(m, s, e, 0)
print(traverse_bfs(m, s, e))
min_path = 9999999
for x in range(len(m)):
	for y in range(len(m[0])):
		if m[x][y] == 'a':
			path = traverse_bfs(m, (x,y), e)
			if path != -1 and path < min_path:
				min_path = path

print(min_path)
