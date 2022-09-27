# 실패율문제 시간 초과
def solution(N, stages):
    N_dic={}
    a=len(stages)
    
    for nn in range(1,N+1):
        if a !=0:
            Coun_stag=stages.count(nn)
            N_dic[nn]=Coun_stag/a
            a-=Coun_stag
        else:
            N_dic[nn]=0
    
    
    return sorted(N_dic,key=lambda x:N_dic[x],reverse=True)

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]	))
