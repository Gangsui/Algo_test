from multiprocessing.sharedctypes import Value
from re import A


def solution(N, stages):
    answer = [] 
    N_dic={}
    a=len(stages)
    to_answer=[]
    for nn in range(N+1):
        N_dic[nn+1]=0
    
    for stage in stages:       
        N_dic[stage]=N_dic[stage]+1

    for aa in range(1,N+1):
        b=float(N_dic[aa])/a
        a-=N_dic[aa]
        N_dic[aa]=b

        answer.append(b)
    answer.sort()
    answer.reverse()
    K_V=[]
    
    

    for ss in range(N):
        key,value=N_dic.items()
        K_V.append([key,value])
    print(K_V)
    for aa in answer:
        for K in K_V:
            if aa==K[1]:
                to_answer.append(K[0])
                K[1]=-1
    
   
        
    

    
    
    
    
        print(to_answer)
    return answer




solution(4, [4, 4, 4, 4, 4])