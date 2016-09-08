import math 

def eu_ext(b, n):
	x0, x1, y0, y1 = 1, 0, 0, 1
	while n != 0:
		q, b, n = b // n, n, b % n
		x0, x1 = x1, x0 -q * x1
		y0, y1 = y1, y0 -q * y1
	return b, x0, y0

def gdc(a, b):
	mini = min(a,b)
	gcd = 1 
	iter = range(mini +1)[1:]
	for i in iter:
		if (a % i == 0 and b % i ==0):
			gcd = i
	return gcd

def Zinv(n):
	l = []
	iter = range(36)[1:]
	for i in iter:
		if(gdc(i,n) == 1):
			l.append(i)
	return l

def sqroot(n,r,m):
	for i in range(1000):
		x = math.sqrt(m*i+n)
		if (math.floor(x) == x):	
			break
	return x

def Dlog2table(base,n):
	iter = range(n)[1:]
	table = []
	for i in iter:
		for j in range(1000):
			if(i == math.pow(base,j) % n):
				table.append(j)
				break
	return table

def order(num,mod):
	counter=1
	iter = range(mod+1)[1:]
	for i in iter:
		if (math.pow(num,i) % mod ==1):
			break
		else:
			counter = counter + 1
	return counter