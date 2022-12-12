INPUT = "day10.in"

def read_input(infile):
	inst = []
	for line in infile:
		line = line.strip().split(' ')
		inst.append(line)
	return inst

def run_loop(capture, insts, cycles, crt):

	cycle = 1
	current = insts[0]
	rem = 0 if insts[0] == 'noop' else 1
	index = 1
	ans = 0
	x = 1

	while(cycle <= cycles):
		
		if cycle in capture:
			ans += x * cycle 

		if rem == 0:
			if current[0] == 'addx':
				x += int(current[1])	
			current = insts[index]
			index += 1
			if current[0] == 'noop':
				rem = 0
			else:
				rem = 1	
		else:
			rem -= 1
		
		if x-1 <= cycle % 40 <= x+1:
			crt[cycle] = 1

		cycle += 1
	
	return ans

def print_crt(crt):
	p = ""
	for i in range(6):
		for j in range(40):
			p += "#" if crt[j + 40*i] else "."
		p += '\n'

	print(p)

inst = read_input(open(INPUT))
capture = [20, 60, 100, 140, 180, 220]

crt = [0 for i in range(240)]

print(run_loop(capture, inst, 239, crt))

print_crt(crt)

