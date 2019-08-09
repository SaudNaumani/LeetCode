class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        start = 0
        end = len(s) - 1

        while (start < end):
            if not s[start].isalnum():
                start += 1
            elif not s[end].isalnum():
                end -= 1
            elif s[start].lower() != s[end].lower():
                return False
            else:
                start += 1
                end -= 1
        return True


        '''
        The optimal solution would be to a implement an in place two pointer solution.
        We have a left and right pointer and we iterate from opposite ends of the string
        If they are not alphanumeric we move one, else we see if they are the same
        If they are not we return false

        '''
