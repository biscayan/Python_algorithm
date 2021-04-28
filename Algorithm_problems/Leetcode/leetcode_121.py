### solution1
### 시간초과
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] > prices[i]:
                    profit = prices[j] - prices[i]
                    answer = max(answer, profit)

        return answer


### solution2
### 1084 ms	25.2 MB
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        answer = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(price, min_price)
            answer = max(answer, price-min_price)

        return answer