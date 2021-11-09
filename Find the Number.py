n, x, k = map(int, "10 5 10".split(" "))
S = list("1234567891")

# n, x, k = map(int, "11 3 9".split(" "))
# S = list("13244467589")

blocks = [S[i:i+x] for i in range(0, n, x)]

digits = [sorted(set(i)) for i in blocks]

freq = [len(x) for x in digits]

for i in range(len(freq)-2, -1, -1):
	freq[i] = freq[i] * freq[i+1]

if k>freq[0]:
	print(-1)
freq.append(1)

ans = []
k = k-1

for i in range(1, len(freq)):
	div = k//freq[i]
	ans.append(digits[i-1][div])
	k = k % freq[i]

print(''.join(ans))


