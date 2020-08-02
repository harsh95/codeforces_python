n = int(input())
count = 0
capacity = []
for x in range(n):
	o, i = map(int,input().split())
	count -= o
	count += i
	capacity.append(count)
print(max(capacity))