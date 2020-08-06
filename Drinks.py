n = int(input())
percent = input().split()
sum1 = 0
for i in percent:
	sum1 += int(i)
print(float(sum1/(n)))