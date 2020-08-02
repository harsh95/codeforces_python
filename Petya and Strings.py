string1 = []
string2 = []
string1 += str(input()).lower()
string2 += str(input()).lower()
length = len(string1)
#print(string1)
#print(string2)
count = 0
for i in range(length):
	if ord(string1[i]) != ord(string2[i]):
		if ord(string1[i]) > ord(string2[i]):
			count = 1
			break
		elif ord(string2[i]) > ord(string1[i]):
			count = -1
			break
	else:
		count = 0
		
print(count)
"""
if first > second:
	print("1")
elif second > first:
	print("-1")
else:
	print("0")

print(first, second)
"""