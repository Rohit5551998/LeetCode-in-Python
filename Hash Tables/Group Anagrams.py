from typing import List

strs = ["eat","tea","tan","ate","nat","bat"]

def findHash(string: str) -> str:
	return "".join(sorted(string))

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
	answers = []
	map = {}

	for string in strs:
		hashed = findHash(string)
		
		if hashed not in map:
			map[hashed] = []

		map[hashed].append(string)

	for val in map.values():
		answers.append(val)

	return answers

print(f"The anagrams are as follows: {groupAnagrams(strs)}")