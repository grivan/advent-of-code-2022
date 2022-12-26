INPUT = "day18.in"

def read_input(infile):
	cubes = []
	for line in infile:
		cube = line.strip().split(',')
		cube = [int(x) for x in cube]
		cube = (cube[0], cube[1], cube[2])
		cubes.append(cube)
	return cubes

def find_int(cubes):
	n = len(cubes)
	inter = 0
	for i in range(n):
		for j in range(i+1, n):
			c1 = cubes[i]
			c2 = cubes[j]

			x = abs(c1[0] - c2[0])
			y = abs(c1[1] - c2[1])
			z = abs(c1[2] - c2[2])

			if x == 0 and y == 0 and z == 1:
				inter += 1
			if x == 0 and y == 1 and z == 0:
				inter += 1
			if x == 1 and y == 0 and z == 0:
				inter += 1

	return inter * 2

def inbounds(check, minc, maxc):
	x,y,z = check
	return minc < x < maxc and minc < y < maxc and minc < z < maxc

def traverse(start, cubes, minc, maxc):
	visible = 0
	n = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
	visited = set()
	queue = [start]
	while queue:
		x,y,z = queue.pop(0)
		visited.add((x,y,z))
		for nx, ny, nz in n:
			check = (x+nx, y+ny, z+nz)
			if inbounds(check, minc, maxc) and check not in visited and check not in queue:
				if check in cubes:
					visible += 1
				else:
					queue.append(check)
	return visible
	

cubes = read_input(open(INPUT))
print(len(cubes) * 6 - find_int(cubes))
print(traverse((0,0,0), cubes, -5, 24))
