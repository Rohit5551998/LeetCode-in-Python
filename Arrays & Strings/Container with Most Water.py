from typing import List

heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]

def maxArea(heights: List[int]) -> int:
	maxWater = 0
	p1 = 0
	p2 = len(heights) - 1

	while(p1 < p2):
		height = min(heights[p1], heights[p2])
		width = p2 - p1
		currWater = height * width
		maxWater = max(maxWater, currWater)

		if (heights[p1] <= heights[p2]):
			p1 += 1
		else:
			p2 -= 1 

	return maxWater

print(f"Maximum water that can be held is {maxArea(heights)}")