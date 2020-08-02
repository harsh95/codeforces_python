word = str(input())
string = list(word)
upper, lower = 0, 0
for i in string:
	if i.islower():
		lower += 1
	else:
		upper += 1

if upper > lower:
	print(word.upper())
else:
	print(word.lower())