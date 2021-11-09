from typing import List

nums1 = [1, 2]
nums2 = [-2, -1]
nums3 = [-1, 2]
nums4 = [0, 2]

def fourSumCount(nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
	map = {}
	ans = 0

	for i in nums1:
		for j in nums2:
			sum = i+j

			if sum not in map:
				map[sum] = 0

			map[sum] += 1

	for i in nums3:
		for j in nums4:
			target = -(i+j)

			ans += map[target]

	return ans

print(f"The Four Sum Count is {fourSumCount(nums1, nums2, nums3, nums4)}")