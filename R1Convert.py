
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f: # -sig can delete the memory note in the beginning of text
		for line in f:
			lines.append(line.strip())
	return lines
# a=[]
# b=[1,2,3,4]
# a = a.append(b)

def convert(lines): # because of the following convert(lines)
	new = []
	person = None
	for line in lines:
		if line == 'Allen': # line has been given value, and Allen is a string
			person = 'Allen' # person = string
			continue # save Allen, then jump to next line, and print out Allen's texts
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:
			new.append(person + ': ' + line)
	return new 

def write_file(filename, lines):
	with open (filename, 'w', encoding = 'utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

main()