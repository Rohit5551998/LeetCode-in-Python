from typing import List

nums = [2, 7, 11, 15]
target = 17

def twoSum(nums: List[int], target:int) -> List[int]:
	seen = {}
	for i in range(len(nums)):
		if nums[i] in seen:
			return [seen[nums[i]], i]

		seen[target-nums[i]] = i

print(f"The indices that reach {target} from the given array are {twoSum(nums, target)}")