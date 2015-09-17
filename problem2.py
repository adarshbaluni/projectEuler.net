#find the problem at : https://projecteuler.net/problem=2
import sys


def findSumOfEvenValuedTerms(fibonacci):
	SumOfEvenValuedTerms = 2
	curIndex = 1

	while 1:
		nextValue = fibonacci[curIndex] + fibonacci[curIndex - 1]
		curIndex += 1

		if(nextValue > 4000000):
			return SumOfEvenValuedTerms
		else:
			fibonacci.append(nextValue)

		if(nextValue % 2 == 0):
			SumOfEvenValuedTerms += nextValue


if __name__ == "__main__":

	fibonacci = [1,2]
	result = findSumOfEvenValuedTerms(fibonacci)
	print "Sum of Even Valued Terms is %r" % result