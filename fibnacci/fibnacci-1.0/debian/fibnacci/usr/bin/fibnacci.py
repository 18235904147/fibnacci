#!/usr/bin/python3
def fib(n):
	pre1 = 1;
	pre2 = 1;
	print(1)
	for i in range (n):
		print(pre2)
		tmp = pre1
		pre1 = pre2
		pre2 = tmp + pre2

def check_n(n):
	if n.isdigit():
		if isinstance(int(n),int) and int(n) > 0:
			return int(n)
		else:
			return False
	else:
		return False

if __name__ =="__main__":
	n = input('输入：')
	result = check_n(n)
	if result is False:
		print("错误！")
	else:
		fib(result)

