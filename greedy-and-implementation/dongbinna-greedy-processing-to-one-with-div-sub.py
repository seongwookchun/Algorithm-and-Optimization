def solution(n, k):
    cnt = 0
    lcnt = 0
    while n > 1:
        q, mod = divmod(n, k)
        print(f'lcnt: {lcnt}', end=' ')
        if mod == 0:
            n = q
            cnt += 1
            print(f'div   / mod {mod} n/q {n}/{q} cnt: {cnt}')
        else:
            n -= 1
            cnt += 1
            print(f'minus / mod {mod} n/q {n}/{q} cnt: {cnt}')
        lcnt += 1
    print(cnt)



def teacherSolution(n, k):
    cnt = 0
    while True:
        q, mod = divmod(n, k)
        cnt += mod
        n -= mod # n = q * k  # max integer
        if n < k:
            break
        cnt += 1
        n = q
    cnt += (n - 1)
    print(cnt)
# print(solution(17,4))
if __name__ == '__main__':
    cases = [(25,3), (26,3), (27, 3)]
    for n, k in cases:
        print('='*50)
        print(solution(n,k))
        print(teacherSolution(n,k))
