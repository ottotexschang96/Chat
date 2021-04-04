
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f: 
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines): 
	person = None
	allen_word_counting = 0
	allen_sticker_counting = 0
	allen_image_counting = 0
	viki_word_counting = 0
	viki_sticker_counting = 0
	viki_image_counting = 0

	for line in lines:
		s = line.split(' ') # cut off space, and make the elements into a list
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_counting += 1
			elif s[2] == '圖片':
				allen_image_counting += 1
			else:
				for m in s[2:]:
					allen_word_counting += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_counting += 1
			elif s[2] == '圖片':
				viki_image_counting += 1
			else:
				for m in s[2:]:
					viki_word_counting += len(m)
	print('Allen says', allen_word_counting, 'words and sends', allen_sticker_counting, 'sticker(s) and', allen_image_counting, 'image(s)')
	print('Viki says', viki_word_counting, 'words and sends', viki_sticker_counting, 'sticker(s) and', viki_image_counting, 'image(s)')


def write_file(filename, lines):
	with open (filename, 'w', encoding = 'utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)

	# write_file('output.txt', lines)


main()
