
lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(' ')
	time = s[0][:5]#用第幾個字來切割字串0~4
	name = s[0][5:]#0到５之後
	print(name)

