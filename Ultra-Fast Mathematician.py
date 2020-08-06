first = list(str(input()))
second = list(str(input()))
#print(first, second)
output = ""
for i in range(len(first)):
	if first[i] == second[i]:
		output += '0'
	else:
		output += '1'
print(output)
