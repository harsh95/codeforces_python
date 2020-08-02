n = int(input())
code = []
for i in range(n):
	s = input()
	code.append(s)
count = 0
for i in code:
	if i[0] == '+':
		count += 1
	elif i[0] == '-':
		count -= 1
	elif i[0] == 'X':
		if i[1] == '+':
			count += 1
		elif i[1] == '-':
			count -= 1

print(count)