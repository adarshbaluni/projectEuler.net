#https://projecteuler.net/problem=1
import sys


def findSumOfMultiples():
	sumOfMultiples = 0

	for value in range(1,1000):
		if( value % 3 == 0 or value % 5 == 0):
			sumOfMultiples += value			
			
	return sumOfMultiples



if __name__ == "__main__":

	result = findSumOfMultiples()
	print "Sum of multiples of 3 or 5 below 1000 is %r" % result