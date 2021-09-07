from typing import List

nums = [9,6,4,2,3,5,7,0,1]

def missingNumber(nums: List[int]) -> int:
	currentSum = sum(nums)
	n = len(nums)
	intendedSum = int(n*(n+1)/2)
	return intendedSum - currentSum

print(f"The missing number from the series is {missingNumber(nums)}")