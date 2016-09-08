import math 

"""eu_ext			
	Euclid Extended Algorith
	@args b: Integer
		  n: Integer
	@return : gdc(b,n)
			  x and y integer	
			from bx + ny = gdf(b,n)
"""
def eu_ext(b, n):
	x0, x1, y0, y1 = 1, 0, 0, 1
	while n != 0:
		q, b, n = b // n, n, b % n
		x0, x1 = x1, x0 -q * x1
		y0, y1 = y1, y0 -q * y1
	return b, x0, y0


"""gdc
	Greatest Common Divisor
	@args: a,b Integer to evaluate
	@return gdc(a,b)
"""
def gdc(a, b):
	mini = min(a,b)
	gcd = 1 
	iter = range(mini +1)[1:]
	for i in iter:
		if (a % i == 0 and b % i ==0):
			gcd = i
	return gcd

"""Zinv
	Calculates the Zn* set
	@args: n Integer 
	@return l - list set	
"""		
def Zinv(n):
	l = []
	iter = range(36)[1:]
	for i in iter:
		if(gdc(i,n) == 1):
			l.append(i)
	return l

"""sqroot
	Calculate square root of n module m
	@args: n argument of the sqrt function
		   m Zm
	@return x integer 
"""
def sqroot(n,m):
	for i in range(1000):
		x = math.sqrt(m*i+n)
		if (math.floor(x) == x):	
			break
	return x

"""Dlog2table
	Discrete Logarith table from small Zn
	@args: base - base of the log
		   n - Zn
	@return: list - table
"""
def Dlog2table(base,n):
	iter = range(n)[1:]
	table = []
	for i in iter:
		for j in range(1000):
			if(i == math.pow(base,j) % n):
				table.append(j)
				break
	return table


"""order
	Calcules the order of a element in a cyclid group Zn
	@args: num - integer belonging to Zn
		   mod - Zn
	@return: o(num) in Zmod
"""
def order(num,mod):
	counter=1
	iter = range(mod+1)[1:]
	for i in iter:
		if (math.pow(num,i) % mod ==1):
			break
		else:
			counter = counter + 1
	return counter