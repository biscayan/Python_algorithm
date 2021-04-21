class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        answer = ''

        if len(s)<2 or s == s[::-1]:
            answer = s
            return answer

        ### two-pointer algorithm
        else:
            for i in range(len(s)):

                ### s의 길이가 홀수일 때
                left, right = i, i

                while (left >= 0 and right < len(s)) and s[left] == s[right]:
                    left -= 1
                    right += 1

                if len(s[left+1:right]) > len(answer):
                    answer = s[left+1:right]

                ### s의 길이가 짝수일 때
                left, right = i, i+1
                
                while (left >= 0 and right < len(s)) and s[left] == s[right]:
                    left -= 1
                    right += 1

                if len(s[left+1:right]) > len(answer):
                    answer = s[left+1:right]

        return answer