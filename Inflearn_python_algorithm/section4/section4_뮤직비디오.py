import sys

sys.stdin = open('input.txt','r')

def divide_video(mid,videos):
    
    cnt = 0
    dvd_num = 1
    
    for video in videos:
        cnt += video
        if cnt > mid:
            dvd_num +=1
            cnt = video
    return dvd_num

if __name__=='__main__':
    
    N, M = map(int,input().split())
    video_list = list(map(int,input().split()))

    capacity = 0

    l_idx = 1
    r_idx = sum(video_list)

    while l_idx <= r_idx:
        
        m_idx = (l_idx + r_idx)//2

        if divide_video(m_idx,video_list) <= M:
            capacity = m_idx
            r_idx = m_idx-1
        else:
            l_idx = m_idx+1
            
    print(capacity)
            
