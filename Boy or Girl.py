string = str(input())
word = []

for i in range(len(string)):
	if string[i:i+1] not in word:
		word.append(string[i:i+1])
if len(word)%2 == 0:
	print("CHAT WITH HER!")
else: 
	print("IGNORE HIM!")
