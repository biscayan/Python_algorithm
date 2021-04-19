import re
import collections

### solution1
### 36ms, 14.3MB
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        word_list = []

        paragraph = paragraph.lower()
        paragraph = re.sub('[^a-z]',' ',paragraph)

        for word in paragraph.split():
            if word not in banned:
                word_list.append(word)

        count_list = collections.Counter(word_list).most_common()

        answer = count_list[0][0]

        return answer


### solution2
### 36ms, 14.2MB
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        word_list = []

        paragraph = paragraph.lower()
        paragraph = re.sub('[^a-z]',' ',paragraph)

        for word in paragraph.split():
            if word not in banned:
                word_list.append(word)

        count_dict = collections.defaultdict(int)
        
        for word in word_list:
            count_dict[word] += 1
            
        answer = max(count_dict, key=count_dict.get)
        
        return answer