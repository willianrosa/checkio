#coding: utf-8
def checkio(opacity):	
	#fibonacci method
	def fib():
	    x = 0
	    y = 1
	    while 1:
	        x, y = y, x + y
	        yield x
	g = fib()
	f = [g.next() for i in range(19)]

	#calc opacity x years
	def calc(t,f):
		for i in range(0,t):			
			t=t-i if (i in f) else t+1
			yield t

	#call generators
	num = calc(9999,f)
	s=[(x, num.next()) for x in range(0,5000)]
	
	return [item[0] for item in s if item[1] == opacity][0]
	
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"