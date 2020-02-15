import sys
INF = 1000#sys.maxsize
# G = [[INF,  10,  15, INF, INF,     INF, INF, INF, INF, INF,     INF],
#      [INF, INF, INF,  20, INF,     INF, INF, INF, INF, INF,     INF],
#      [INF, INF, INF, INF,  15,     INF, INF, INF, INF, INF,     INF],
#      [INF, INF, INF, INF, INF,      20, INF, INF, INF, INF,     INF],
#      [INF, INF, INF, INF, INF,      15, INF, INF, INF, INF,     INF],
     
#      [INF, INF, INF, INF, INF,    INF,  20,   5, INF, INF,     INF],
#      [INF, INF, INF, INF, INF,    INF, INF, INF,  20, INF,     INF],
#      [INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF,     INF],
#      [INF, INF, INF, INF, INF,    INF, INF, INF, INF,   5,     20],
#      [INF, INF, INF, INF, INF,    INF, INF, INF, INF, INF,      5],
     
#      [INF, INF, INF, INF, INF,    INF, INF, INF, INF,  INF,     INF],]

G = [[INF,   5,   1, INF],
     [INF, INF,   5,   1],
     [INF, INF, INF,   5],
     [INF, INF, INF, INF]]
for i in range(len(G) -1):    # 양방향 연결을 위한 대각선 복사
    for j in range(i +1, len(G)):
        G[j][i] = G[i][j]
        
print('*'*100)

def isgroup(m, n):
    if l_gid[m] == l_gid[n]:
        return True
    return False

def kruskal(G):
    lis = list()
    for i in range(len(G) -1):
        for j in range(i +1, len(G)):
            lis.append([G[i][j], [i, j]])
    print('lis:', lis)
    lis = sorted(lis, key=lambda x: x[0])
    print('lis:', lis)
    newG = [[INF for _ in range(len(G))] for _ in range(len(G))]
    tot = 0
    for c, (m, n) in lis:
        if isgroup(m, n) == False:
            print('m:', m, 'n:', n)
            print(l_gid)
            print('tot:', tot)
            print('c:', c)
            tot += c
            print('tot:', tot)
            
            newG[m][n] = c
            newG[n][m] = c
            if l_gid[m] > l_gid[n]:
                l_gid[m] = l_gid[n]
            elif l_gid[m] < l_gid[n]:    # 효율을 위해서 == 인 경우를 배제함
                l_gid[n] = l_gid[m]
            
            print('connection:')
            print(l_gid)
            print('*'*100)
    
    print('*'* 100)
    print(newG)
    print(tot)
    return tot
    
kruskal(G)
