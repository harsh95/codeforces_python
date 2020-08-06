n = int(input())
people = input().split()
flag = 0
for i in people:
	if i == '1':
		flag = 1
if flag == 1:
	print("HARD")
else:
	print("EASY")
