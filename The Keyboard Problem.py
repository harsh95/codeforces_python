string = str(input())
word = list(string)
count = 0
for i in range(len(word)):
	if i == 0:
		count += ord(word[i])-64
	else:
		count += abs(ord(word[i-1]) - ord(word[i]))

print(count)