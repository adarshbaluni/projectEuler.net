import sys

def problem3():
	number = 600851475143
	factor = 2
	largestPrimeFactor = number
	
	while factor * factor <= number:
		if number % factor == 0:
			number = number / factor
			largestPrimeFactor = factor 			
		else:
			factor += 1 
		
	if number > largestPrimeFactor:
		largestPrimeFactor = number

	print "The largest prime factor is : ", largestPrimeFactor

if __name__ == '__main__':
	problem3()
