def factorial(n):
	if n <= 1:
		return 1
	return n * factorial(n - 1)

def derangement(n):
	if n == 0:
		return 1
	if n == 1:
		return 0
	return (n-1) * (derangement(n - 1) + derangement(n - 2))

print(derangement(4))

print(factorial(4))