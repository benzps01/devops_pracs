for i in range(1,21):
	output = ""
	if i % 3 == 0:
		output += "fizz"
	if i % 5 == 0:
		output += "buzz"
	if output == "":
		print(i)
	else:
		print(output)
	