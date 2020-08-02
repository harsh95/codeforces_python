n = int(input())
word = []

for i in range(n):
	s = str(input())
	word.append(s)


for i in word:
	if len(i) > 10:
		print(i[0] + str(len(i)-2) + i[len(i)-1])
	else:
		print(i)