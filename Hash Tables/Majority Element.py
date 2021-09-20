from typing import List

def majorityElement(nums: List[int]) -> int:
	map = {}

	for num in nums:
		map[num] = map.get(num, 0) + 1

	for num in nums:
		if (map[num] > len(nums)//2):
			return num