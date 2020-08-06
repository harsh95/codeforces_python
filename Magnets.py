n = int(input())
mag = []
for i in range(n):
	mag.append(str(input()))
flag = mag[0]
count, x = [1], 0
for i in range(1, n):
	if mag[i] == flag:
		count[x] += 1
		#print(flag)
	else:
		count.append(0)
		flag = mag[i]
		x += 1
		count[x] += 1
		#print(flag)
print(len(count)) 