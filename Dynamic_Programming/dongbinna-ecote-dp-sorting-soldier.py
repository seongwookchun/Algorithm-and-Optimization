def pt(x):
    for _ in x:
        print(_)
def solution():#gold2D):
    m, n = 4, 3
    gold2D = '1 3 3 2 2 1 4 1 0 6 4 7'.split()
    gold2D = [list(map(int, gold2D[i*m:(i+1)*m])) for i in range(n)]
    
    pt(gold2D)
    
    for i in range(m-2, -1, -1):#len(gold2D[0])):
        for j in range(n):
            if j == 0:
                gold2D[j][i] += max(gold2D[j][i+1], gold2D[j+1][i+1])
            elif j == n-1:
                gold2D[j][i] += max(gold2D[j][i+1], gold2D[j-1][i+1])
            else:
                gold2D[j][i] += max(gold2D[j][i+1], gold2D[j-1][i+1], gold2D[j+1][i+1])
    
    pt(gold2D)
    ans = max([gold2D[_][0] for _ in range(n)])
    print(ans)
    return ans
print(solution())
