n, h = map(int,input().split())
num = input().split()
height = 0
for i in num:
	if int(i) > h:
		height += 2
	else:
		height += 1
print(height)