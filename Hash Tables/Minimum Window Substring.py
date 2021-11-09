def minWindow(self, s: str, t: str) -> str:    
		len1 = len(s)
		len2 = len(t)

		if (len1 < len2):
				return ""

		hashPat, hashStr = {}, {}

		for i in t:
				if i not in hashPat:
						hashPat[i] = 0
				hashPat[i] += 1

		count = 0
		left = 0
		minLen = float("inf")
		startIndex = -1

		for right in range(0, len1):

				if s[right] not in hashStr:
						hashStr[s[right]] = 0
				hashStr[s[right]] += 1

				if hashPat.get(s[right]) is None:
						hashPat[s[right]] = 0

				if (hashStr.get(s[right]) <= hashPat.get(s[right]) and hashPat.get(s[right]) != 0):
						count += 1

				if (count == len2):
						
						if(hashStr.get(s[left]) is None):
								hashStr[s[right]] = 0
						if(hashPat.get(s[left]) is None):
								hashPat[s[right]] = 0
						
						while(hashStr.get(s[left]) > hashPat.get(s[left]) or hashPat.get(s[left]) == 0):

								if (hashStr.get(s[left]) > hashPat.get(s[left])):
										hashStr[s[left]] -= 1
								left += 1  # incrementing the left pointer

						windowLen = right - left + 1  # calculating the windows length
						if (minLen > windowLen):
								minLen = windowLen
								startIndex = left

		if (startIndex == -1):
				return ""

		return s[startIndex:startIndex+minLen]

