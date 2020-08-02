n, x = map(int,input().split())
s = str(input())
word = list(s)

for j in range(x):
	i = 1
	while(n > i):
		if word[i-1] == 'B' and word[i] == 'G':
			word[i-1], word[i] = word[i], word[i-1]
			i += 2
		else:
			i += 1
string = ''.join(word)
print(string)