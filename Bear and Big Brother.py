i, j = map(int,input().split())
count = 0
while(j >= i):
	i *= 3
	j *= 2
	count += 1

print(count)