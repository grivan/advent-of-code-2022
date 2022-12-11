INPUT = "day8.in"

def read_input(infile):
	m = []
	for line in infile:
		m.append([int(x) for x in list(line.strip())])
	return m

def visible(m):
	x, y = len(m[0]), len(m)
	visible = [[None for _ in range(x)] for __ in range(y)]
	score = [[None for _ in range(x)] for __ in range(y)]

	for i in range(y):
		for j in range(x):
			
			if i == 0 or i == (y-1) or j == 0 or j == (x-1):
				visible[i][j] = 1
				score[i][j] = 0
				continue

			up, down, left, right = 1, 1, 1, 1
			s_up, s_down, s_left, s_right = 0, 0, 0, 0
			
			# look up from tree
			for k in range(i-1, -1, -1):
				s_up += 1
				if m[k][j] >= m[i][j]:
					up = 0
					break
			
			# look down from tree
			for k in range(i+1, y):
				s_down += 1
				if m[k][j] >= m[i][j]:
					down = 0
					break
			
			# look right from tree
			for k in range(j+1, x):
				s_right += 1
				if m[i][k] >= m[i][j]:
					right = 0
					break
			
			# look left from tree
			for k in range(j-1, -1, -1):
				s_left += 1	
				if m[i][k] >= m[i][j]:
					left = 0
					break

			#print(i, j, m[i][j], up, down, left, right)	
			#print(i, j, m[i][j], s_up, s_down, s_left, s_right)	
			
			visible[i][j] = up or down or left or right
			score[i][j] = s_up * s_down * s_left * s_right
			

	return visible, score

def print_mat(mat):
	o = ""
	for l in mat:
		o += "\n" + "".join([str(i) for i in l])
	print(o)

m = read_input(open(INPUT))
#print_mat(m)
v,s = visible(m)
#print_mat(s)
print(sum([sum(l) for l in v]))
print(max([max(l) for l in s]))
