import re

### solution1
### 44ms, 15.7mb
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        s = re.sub('[^a-z0-9]','',s)
        
        for i in range(len(s)//2):
            if s[i] != s[len(s)-i-1]:
                return False
                
        return True

### solution2
### 32ms, 15.6mb
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        s = re.sub('[^a-z0-9]','',s)
        
        ### s[::-1] -> s를 뒤집음
        if s != s[::-1]:
            return False
        else:
            return True