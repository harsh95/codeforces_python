n, max = map(int,input().split())
score = input().split()
count = 0
for i in score:
	if int(i) >= int(score[int(max)-1]) and int(i) > 0:
		count += 1
	else:
		break
print(count)