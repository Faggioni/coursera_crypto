
"""
	7a + 23b = 1
"""
def test():
	for i in range(20):
		for j in range(20):
			if (7*i + 23*j == 1):
				a = i
				b = j
				break

	print a,b

def xgcd(a,b):
	prevx, x = 1, 0; prevy, y = 0, 1
	while b:
	q = a/b
	x, prevx = prevx - q*x, x
	y, prevy = prevy - q*y, y
	a, b = b, a % b
	return a, prevx, prevy



