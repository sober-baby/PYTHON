class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        valid = False 
        for i in range (len(s)):
            if s[i] in '([{':
                    print(s[i])
                    if s[i + 1] == s[i]:
                        valid = True
        return valid 
    

if __name__ == '__main__':
    s = Solution()
    print(s.isValid('()'))