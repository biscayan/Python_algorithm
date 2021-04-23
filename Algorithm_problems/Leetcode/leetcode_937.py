### 실무에서도 자주 쓰이는 매우 실용적인 문제
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        letters, digits = [], []

        for log in logs:
            if log.split()[1].isdigit() == True:
                digits.append(log)
            else:
                letters.append(log)

        letters = sorted(letters, key = lambda x: (x.split()[1:],x.split()[0]))

        answer = letters + digits

        return answer