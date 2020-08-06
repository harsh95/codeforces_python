n = int(input())
p1 = set(input().split())
p2 = set(input().split())
print(p1, p2)
count = 0
for i in range(1, n+1):
	if str(i) in p1 or str(i) in p2:
		#print(i)
		count += 1
#print(count)
if count == n:
	print("I become the guy.")
else:
	print("Oh, my keyboard!")