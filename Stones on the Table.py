n = int(input())
string = str(input())
word = []
for i in range(len(string)):
	word.append(string[i:i+1])
count = 0
for i in range(1,n):
	if word[i-1] == word[i]:
		count += 1
print(count)