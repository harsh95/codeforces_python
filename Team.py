n = int(input())
code = []
for i in range(n):
	s = input().split()
	code.append(s)

count = 0

for i in code:
	c = 0
	for j in range(3):
		if i[j] == '1':
			c += 1
	if c > 1:
		count += 1

print(count)