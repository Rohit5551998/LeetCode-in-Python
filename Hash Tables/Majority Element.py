from typing import List

nums = [1, 2, 5, 2, 4, 5, 5, 5, 5]

def majorityElement(nums: List[int]) -> int:
	map = {}

	for num in nums:
		map[num] = map.get(num, 0) + 1

	for num in nums:
		if (map[num] > len(nums)//2):
			return num

print(f"The majority element in the list {nums} is {majorityElement(nums)}")

print("The majority element in the list "+ str(nums) +" is "+ str(majorityElement(nums))