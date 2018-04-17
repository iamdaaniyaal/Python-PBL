def characterCounts(s):
	counts={}

	for ch in s:
		if ch in counts:
			counts[ch] = counts[ch]+1
		else:
			counts[ch] = 1
	return counts

def main():
	s1 =input("enter 1st string")
	s2 =input("enter 2nd string")

	counts1 = characterCounts(s1)
	counts2 = characterCounts(s2)

	if counts1 == counts2:
		print("anagrams")

	else:
		print("not anagrams")

main()