from typing import List

nums = [5,7,8,8,8,8,10]
target = 8

def leftSearch(nums: List[int], target:int) -> int:
	left, right = 0, len(nums) - 1

	while(left <= right):
		mid = (left + right)//2
		if(nums[mid] == target):
			#Leftmost Occurence
			if(mid == 0 or (mid-1 > 0 and nums[mid-1] != target)):
				return mid
			#Not the Leftmost Occurence
			else:
				right = mid - 1

		elif(nums[mid] > target):
			right = mid - 1

		elif(nums[mid] < target):
			left = mid + 1
			
	return -1

def rightSearch(nums: List[int], target:int) -> int:
	left, right = 0, len(nums) - 1

	while(left <= right):
		mid = (left + right)//2
		if(nums[mid] == target):
			#Rightmost Occurence
			if(mid == len(nums)-1 or (mid+1 < len(nums) and nums[mid+1] != target)):
				return mid
			#Not the Rightmost Occurence
			else:
				left = mid + 1

		elif(nums[mid] > target):
			right = mid - 1

		elif(nums[mid] < target):
			left = mid + 1
		
	return -1

def searchRange(nums: List[int], target:int) -> List[int]:
	left = leftSearch(nums, target)
	right = rightSearch(nums, target)

	return [left, right]

print(f"The first and last position of {target} is {searchRange(nums, target)}")