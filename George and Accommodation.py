n = int(input())
s, r, count = 0, 0, 0
for i in range(n):
	s, r = map(int,input().split())
	if (r - s) > 1:
		count += 1
print(count)