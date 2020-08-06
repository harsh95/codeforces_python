n = int(input())
string = "I hate "
flag = "hate "
for i in range(n-1):
	string += "that "
	if flag == "hate ":
		flag = "love "
		string += "I "
		string += flag
	else:
		flag = "hate "
		string += "I "
		string += flag
string += "it"
print(string)
