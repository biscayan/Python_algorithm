class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l_idx, r_idx = 0, len(nums)-1
    
        while l_idx <= r_idx:

            m_idx = (l_idx + r_idx) // 2
            
            ### m_idx를 찾는 엄격한 방법
            ### overflow를 일으키지 않는 계산법
            m_idx = l_idx + (r_idx-l_idx) // 2

            if nums[m_idx] == target:
                return m_idx

            elif nums[m_idx] > target:
                r_idx = m_idx -1

            elif nums[m_idx] < target:
                l_idx = m_idx + 1
                
        return -1