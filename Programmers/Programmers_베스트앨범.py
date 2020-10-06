def solution(genres,plays):
    
    answer = []
    genre_dict = {}
    play_dict = {}

    ###genres와 plays의 길이는 같음
    for i in range(len(genres)):
        
        ###value 추가
        if genres[i] in genre_dict:
            genre_dict[genres[i]] += plays[i]
            play_dict[genres[i]].append((plays[i],i))
            
        ###key, value저장
        else:
            genre_dict[genres[i]] = plays[i]
            play_dict[genres[i]] = [(plays[i],i)]

    #print("play_dict:",play_dict)
    #print("genre_dict:",genre_dict)

    ###재생횟수가 높은 장르 순으로 정렬, 조건1
    sorted_genre_dict = sorted(genre_dict.items(), key=lambda x:x[1], reverse=True)

    #print(sorted_genre_dict)
    
    for j in sorted_genre_dict:
        
        play_list = play_dict[j[0]]

        ###장르 안에서 재생횟수가 높은 순으로 정렬, 조건2
        sorted_play_list=sorted(play_list, key=lambda x:(x[0],x[1]), reverse=True)
        #print("play list:",sorted_play_list)

        for k in range(len(sorted_play_list)):
            ###두개씩만 저장 
            if k == 2:
                break

            ###재생횟수가 같을 경우 swap, 조건3
            if len(sorted_play_list)==2:
                if sorted_play_list[0][0]==sorted_play_list[1][0]:
                    sorted_play_list[0] = sorted_play_list[1]
                    sorted_play_list[1] = sorted_play_list[0]
                
            elif len(sorted_play_list)>2:
                if sorted_play_list[k][0]==sorted_play_list[k+1][0]:
                    sorted_play_list[k] = sorted_play_list[k+1]
                    sorted_play_list[k+1] = sorted_play_list[k]
                               
            answer.append(sorted_play_list[k][1])
            
    return answer
            
if __name__ == '__main__':
    #test case
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500,600,150,800,2500]
    print(solution(genres,plays))

###test case 2,15 실패, 왜?
