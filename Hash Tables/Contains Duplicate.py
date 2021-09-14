from typing import List

nums = [1, 2, 3, 1]

def containsDuplicate(nums: List[int]) -> int:
	seen = set()
	for i in range(len(nums)):
		if nums[i] in seen:
			return True
		
		seen.add(nums[i])

	return False

print(f"The given array {'' if containsDuplicate(nums) else 'does not '}contains duplicate values.")