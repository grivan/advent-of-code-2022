INPUT = "day7.in"

class Node():
	def __init__(self, parent, is_file, size, name):
		self.is_file = is_file
		self.parent = parent
		self.size = size
		self.name = name
		self.child = {}
	
	def add_child(self, name, child):
		self.child[name] = child

def make_tree(infile):

	# read the first line since it should be always root
	infile.readline()
	root = Node(None, False, None, '/')

	current = root
	for line in infile: 
		line = line.strip()
		#print(line)
		if line[0] == '$':
			cmd = line[2:4]
			if cmd == 'ls':
				continue
			else:
				cd_dir = line[5:]
				if cd_dir == '..':
					current = current.parent
				elif cd_dir == '/':
					current = root
				else:
					current = current.child[cd_dir]
				continue
		
		p1, p2 = line.split(' ')
		if p1 == 'dir':
			current.add_child(p2, Node(current, False, None, p2))
		else:
			current.add_child(p2, Node(current, True, int(p1), p2))
	
	return root

def print_tree(root, indent=0):
	l1 = ' ' * indent + '- ' + root.name 
	l2 = ' (dir, size=%s)' % root.size if not root.is_file else ' (file, size=%s)' % root.size
	print(l1 + l2)
	for child in root.child.values():
		print_tree(child, indent+1)
	
def compute_size(root):
	total_s = 0
	for child in root.child.values():
		if child.is_file:
			total_s += child.size
		else:
			total_s += compute_size(child)
	root.size = total_s
	return total_s

def soln1(root):
	total = 0
	if root.size <= 100000:
		total += root.size
	for child in root.child.values():
		if not child.is_file:
			total += soln1(child)
	return total

def soln2(root, sp_req, sp_free, min_d):
	
	for child in root.child.values():
		if not child.is_file:
			d = sp_free + child.size
			if d > sp_req:
				child_size = min(child.size, soln2(child, sp_req, sp_free, min_d))
				if child_size < min_d:
					min_d = child_size
	return min_d

tree = make_tree(open(INPUT))
compute_size(tree)
# print_tree(tree)
print(soln1(tree))
print(soln2(tree, 30000000, 70000000 - tree.size, tree.size))
