from typing import List

people = [3, 2, 2, 1] 
limit = 3

def numRescueBoats(people: List[int], limit: int) -> int:
	people.sort()
	left = 0
	right = len(people) - 1
	boats = 0
	while(left <= right):
		
		if (left == right):
			boats += 1
			break
		
		elif (people[left] + people[right] <= limit):
			boats += 1
			left += 1
			right -= 1
		
		elif (people[left] + people[right] > limit):
			boats += 1
			right -= 1

	return boats

print(f"Minimum no of boats required is {numRescueBoats(people, limit)}")