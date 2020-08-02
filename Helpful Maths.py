s = input().split('+')
n = sorted(s)
string = ''
for i in range(len(n)):
	string += n[i]
	if i != len(n)-1:
		string += '+'
print(string)