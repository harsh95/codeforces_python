num = []
for i in range(5):
	s = input().split()
	num.append(s)
r, c = 0, 0
for i in range(5):
	for j in range(5):
		if num[i][j] == '1':
			r = abs(2-i)
			c = abs(2-j)
			break

print(r+c)