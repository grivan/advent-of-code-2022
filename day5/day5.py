INPUT = "day5.in"

def read_input_stacks(infile):
	lines = []
	for line in infile:
		if line.strip() == '':
			break
		lines.append(line)

	s_str = [s for s in lines[-1].strip().split(' ') if s.strip() != '']
	s_dict = {x:list() for x in range(len(s_str))}
	
	for line in lines[:-1]:
		for i, s in enumerate(s_dict):
			letter = line[4*i+1:4*i+2]
			if letter.strip() == '':
				continue
			s_dict[i].insert(0, line[4*i+1:4*i+2])
	
	return s_dict

def read_moves(infile):
	moves = []
	for line in infile:
		ls = line.split(' ')
		move = [int(ls[1]), int(ls[3])-1, int(ls[5].strip())-1]
		moves.append(move)
	return moves

def perform_moves_2(stacks, moves):
	for move in moves:
		from_ = move[1]
		to_ = move[2]
		qty = move[0]
		stacks[from_], cargo = stacks[from_][:-qty], stacks[from_][-qty:]
		stacks[to_].extend(cargo)

def perform_moves(stacks, moves):
	for move in moves:
		from_ = move[1]
		to_ = move[2]
		qty = move[0]
		for i in range(qty):
			cargo = stacks[from_].pop()
			stacks[to_].append(cargo)

def solve():
	infile = open(INPUT)
	stacks = read_input_stacks(infile)
	moves = read_moves(infile)
	#print(stacks)
	#print(moves)
	perform_moves_2(stacks, moves)
	print("".join([s[-1] for s in stacks.values()]))

solve()
