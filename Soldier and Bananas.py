k,n,w = map(int,input().split())
count = 0
for i in range(w):
	count += (i+1)*k

if count > n:
	print(abs(n-count))
else:
	print("0")