# Chapter 5. 리스트, 딕셔너리

## 리스트
- 각 언어별 동적 배열 구현
    |언어|동적 배열|
    |:---:|:---:|
    |파이썬|list()|
    |c++|std::vector|
    |자바|ArrayList|
- 파이썬 리스트는 정수1, 문자 '안녕', 불리언 True 등 모두 제각각인 자료형을 한 단일 리스트에 모두 통합해서 저장할 수 있다. 

## 딕셔너리
- 각 언어별 해시 테이블 구현
    |언어|해시 테이블|
    |:---:|:---:|
    |파이썬|dict()|
    |c++|std::unordered_map|
    |자바|HashMap|
- 해시 테이블은 다양한 타입을 키로 지원하면서도 입력과 조회 모두 O(1)에 가능하다.
- 파이썬 3.7+ : 딕셔너리 입력 순서 유지
- 파이썬 3.6+ : 딕셔너리 메모리 사용량 20% 감소

### defaultdict 객체
- defaultdict 객체는 존재하지 않는 키를 조회할 경우, 에러 메시지를 출력하는 대신 디폴트 값을 기준으로 해당 키에 대한 딕셔너리 아이템을 생성해준다. 
```python
import collections

a = collections.defaultdict(int)
a['A'] = 5
a['B'] = 4
a['C'] += 1
a

defaultdict(<class 'int'>, {'A': 5, 'B': 4, 'C': 1})
```
### Counter 객체
- Counter 객체는 아이템에 대한 개수를 계산해 딕셔너리로 리턴한다.
    ```python
    import collections

    a = [1,2,3,4,5,5,5,6,6]
    b = collections.Counter(a)
    b

    Counter({5: 3, 6: 2, 1: 1, 2: 1, 3: 1, 4: 1})
    ```
- most_common()은 Counter 객체에서 가장 빈도 수가 높은 요소를 추출한다. 
    ```python
    b.most_common(2)

    [(5,3), (6,2)]
    ```