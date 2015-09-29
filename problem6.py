import sys

def function():
	sumOfSq = 0;
	for number in range(1,101):
		sumOfSq += number**2

	sqofSum = ((100 * (101)) / 2)**2

	print sqofSum - sumOfSq


if __name__ == "__main__":
	function()
