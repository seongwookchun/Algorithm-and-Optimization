import sys
INF = 1000#sys.maxsize
G = [[INF,  10,  15, INF, INF,     INF, INF, INF, INF, INF,     INF],
     [INF, INF, INF,  20, INF,     INF, INF, INF, INF, INF,     INF],
     [INF, INF, INF, INF,  15,     INF, INF, INF, INF, INF,     INF],
     [INF, INF, INF, INF, INF,      20, INF, INF, INF, INF,     INF],
     [INF, INF, INF, INF, INF,      15, INF, INF, INF, INF,     INF],
     
     [INF, INF, INF, INF, INF,    INF,  20,   5, INF, INF,     INF],
     [INF, INF, INF, INF, INF,    INF, INF, INF,  20, INF,     INF],
     [INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF,     INF],
     [INF, INF, INF, INF, INF,    INF, INF, INF, INF,   5,     20],
     [INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF,      5],
     
     [INF, INF, INF, INF, INF,    INF, INF, INF, INF,  INF,     INF],]
# G=[[1, 2, 3],[-1, -1, 4], [-1, -1, -1]]
for i in range(len(G) -1):    # 양방향 연결을 위한 대각선 복사
    for j in range(i +1, len(G)):
        G[j][i] = G[i][j]
        
print('*'*100)
# print('G')
# print(len(G))
# print(len(G[0]))

def dijstra(node_s, G):
    q = list(range(len(G)))
    D = [INF for _ in range(len(G))]
    
    D[node_s] = 0
    
    while q:
        q = sorted(q, key=lambda x: D[x])    # sorted, key arg의 사용법을 익혀두자.
        print(q)
        print(D)
        node_cur = q.pop(0)
        l_connected = list()    # 현재 커서 노드에 연결되어 있는 노드들을 담는 리스트
        # for idx in range(node_cur +1, len(G)):
        for idx in range(len(G)):
            cost = G[node_cur][idx]
            if cost != INF:
                l_connected.append(idx)
        for node in l_connected:
            via = D[node_cur] + G[node_cur][node]
            if via < D[node]:
                D[node] = via
    
    
    return D
    
dijstra(5, G)
