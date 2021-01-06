def fib(n):
	pre1 = 1;
	pre2 = 1;
	print(1)
	for i in range (n):
		print(pre2)
		tmp = pre1
		pre1 = pre2
		pre2 = tmp + pre2

if __name__ =="__main__":
	n = int(input('输入：'))
	fib(n)

