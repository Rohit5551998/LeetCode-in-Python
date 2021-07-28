s = "abcabcbb"

def lengthOfLongestSubstring(s: str) -> int:
	longest = 0
	left = 0
	seen = {}

	for right in range(len(s)):

		el = s[right]
		if(el in seen):
			left = max(left, seen[el] + 1)

		seen[el] = right
		longest = max(longest, right-left+1) 

	return longest

print(f"The longest substring is: {lengthOfLongestSubstring(s)}")