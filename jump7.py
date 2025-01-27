a = 0
while a < 100:
	a += 1
	b = a % 10
	c = a // 10
	if b == 7 or c == 7 or a % 7 == 0:
		continue
	print(a)