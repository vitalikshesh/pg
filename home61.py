import math

def plo(a, b, c):
	import math
	p = a + b + c
	o = p * (p - a) * (p - b) * (p - c)
	s = math.sqrt(o)
	return s

aa = int(input('1 storona = '))
bb = int(input('2 = '))
cc = int(input('3 = '))


res = plo(aa, bb, cc)
print (res)

