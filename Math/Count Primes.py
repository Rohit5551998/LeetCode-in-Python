import math

def countPrimes(n: int) -> int:

	if (n<2):
		return 0

	isPrime = [True] * n
	isPrime[0] = isPrime[1] = False
	for i in range(2, math.ceil(math.sqrt(n+1))):
		if isPrime[i] == True:
			for multiples_of_i  in range(i*i, n, i):
				isPrime[multiples_of_i] = False

	return isPrime.count(True)

print(f"The number of Prime numbers is {countPrimes(100)}")