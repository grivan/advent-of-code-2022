INPUT = 'day2.in'

def score1():
	score = 0
	with open(INPUT) as day2in:
		s = {'X':1, 'Y':2, 'Z':3}
		w = {'A':'Z', 'B':'X', 'C':'Y'}
		eq = {'A':'X', 'B':'Y', 'C':'Z'}
		for play in day2in:
			x,y = play.strip().split(' ')
			score += s[y]
			if eq[x] == y:
				score += 3
			elif w[x] != y:
				score += 6
	return score

def score2():
	score = 0
	with open(INPUT) as day2in:
		s = {'A':1, 'B':2, 'C':3}
		w = {'A':'C', 'B':'A', 'C':'B'}
		l = {'C':'A', 'A':'B', 'B':'C'}
		for play in day2in:
			x,y = play.strip().split(' ')
			if y == 'X':
				score += s[w[x]]
			elif y == 'Y':
				score += s[x] + 3
			else:
				score += s[l[x]] + 6
	return score


print(score1(), score2())
