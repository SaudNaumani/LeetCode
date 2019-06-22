def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force would be to check every different substring
        # can have two different loops and a helper function which checks if all the characters are unique

        dict = {}
        start = maxInterval = 0
        for i,character in enumerate(s):
            #we start at the starting
            #we increase i each time and see if there is a duplicate in interval [start,i]
            if character in dict:
                duplicateIndex = dict[character] + 1
                if (start < duplicateIndex):
                    start = duplicateIndex

            dict[character] = i
            answer = i+1 - start
            if answer > maxInterval:
                maxInterval = answer

        return maxInterval
