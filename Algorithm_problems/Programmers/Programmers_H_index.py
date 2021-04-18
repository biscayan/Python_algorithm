def solution(citations):
    citation_dict={}
    citations=sorted(citations,reverse=True)
    
    for i in range(len(citations)):
        citation_dict[citations[i]]=i
    
    print(citation_dict)

    for citation in citations:
        if citation_dict[citation]>=citation:
            return citation_dict[citation]

if __name__=='__main__':
    citations=[3,0,6,1,5]
    print(solution(citations))

###test case 9,16 실패