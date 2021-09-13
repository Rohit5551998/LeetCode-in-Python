from typing import List

nums =  [1, 2, 3, 4, 1, 2, 3, 4, 5]

def singleNumber(nums: List[int]) -> int:
	unqNumsSum = sum(set(nums))
	numSum = sum(nums)

	return 2*unqNumsSum - numSum

print(f"The number that appers only once is {singleNumber{nums}}")