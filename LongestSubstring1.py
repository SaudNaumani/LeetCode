def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force would be to check every different substring
        # can have two different loops and a helper function which checks if all the characters are unique
        start = end = maxInterval = 0
        hashset = set()
        size = len(s)

        while (start < size and end < size):
            if s[end] not in hashset:
                hashset.add(s[end])
                end+=1
                maxInterval = max(end-start, maxInterval)
            else:
                hashset.remove(s[start])
                start+=1
        return maxInterval
