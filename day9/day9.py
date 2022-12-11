INPUT = "day9.in"

def read_moves(infile):
	moves = []
	for line in infile:
		line = line.strip()
		d,c = line.split(' ')
		moves.append((d,int(c)))
	return moves

def pair_move(H, T):
	
	Hx, Hy = H
	Tx, Ty = T
	Dx, Dy = (Hx - Tx), (Hy - Ty)
	if abs(Dx) > 1 or abs(Dy) > 1:
		if abs(Dy) == 2:
			Dy = int(Dy/2)
		if abs(Dx) == 2:
			Dx = int(Dx/2)
		Ty += Dy
		Tx += Dx
	return (Tx, Ty)
					

def perform_moves(moves):
	rope = [(0,0) for _ in range(10)]
	seen = set()
	seen.add(rope[-1])

	for move in moves:
		d = move[0]
		for _ in range(move[1]):
			# move the head
			Hx, Hy = rope[0]
			if d == 'R':
				Hx += 1
			if d == 'U':
				Hy += 1
			if d == 'D':
				Hy -= 1
			if d == 'L':
				Hx -= 1
			rope[0] = (Hx, Hy)
			
			# propogate to tail	
			for i, _ in enumerate(rope[1:]):
				P1, P2 = rope[i], rope[i+1]
				rope[i+1] = pair_move(P1, P2)
			
			seen.add(rope[-1])
	return len(seen)

moves = read_moves(open(INPUT))
print(perform_moves(moves))
