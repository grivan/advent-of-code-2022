INPUT = 'day1.in'

def find_max_calories():
	calories = []
	with open(INPUT) as day1in:
		elf_cal = []
		for cal in day1in:
			if cal == '\n':
				calories.append(elf_cal)
				elf_cal = []
			else:
				elf_cal.append(int(cal))
	
	sums = [sum(cal) for cal in calories]

	return max(sums), sum(sorted(sums)[-3:])

print(find_max_calories())
