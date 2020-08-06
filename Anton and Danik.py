n = int(input())
string = list(str(input()))
countA = 0
for i in string:
	if i == 'A':
		countA += 1
if countA > (len(string)/2):
	print("Anton")
elif countA == (len(string)/2):
	print("Friendship")
else:
	print("Danik")
