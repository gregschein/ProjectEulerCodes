def factorial(factorialRoot):
		if factorialRoot==0:
			return 1
		return factorialRoot * factorial(factorialRoot-1)
print factorial(4)