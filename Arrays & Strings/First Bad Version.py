n = 5

def isBadVersion(n: int) -> bool:
	#Provided in Question
	pass

def firstBadVersion(n: int) -> int:
	left, right = 1, n
	while (left < right):
		mid = (left + right) // 2

		if(not isBadVersion(mid)):
			left = mid + 1

		else:
			right = mid #Since loop will stop at left == right

	return left


print(f"The First Bad Version is at {firstBadVersion(n)}")