from itertools import combinations as cb
from itertools import permutations as pm

def isPrime(x):
    if x <= 3: return x > 1
    if x % 2 == 0 or x % 3 == 0: return False
    dividor = 5
    root = int(x**0.5)
    while dividor <= root:
        if x % dividor == 0 or x % (dividor +2) == 0:
            return False
        dividor += 6
    return True
def mySolution(numbers):
    cnt = 0
    uniqueNumToCalc = list()
    for numOfDigits in range(1, len(numbers) +1):
        combs = set([str((''.join(item))) for item in list(cb([c for c in numbers], numOfDigits))])
#         print('='*50)
#         print('combs:')
#         print(combs)
        for c in combs:
#             perms = set([int(''.join(item)) for item in list(pm(c))])
            perms = set(list(pm(c)))
#             print('-'*25)
#             print('set perms')
#             print(perms)
            for perm in perms:
                x = int(''.join(perm))
                uniqueNumToCalc.append(x)
    uniqueNumToCalc = set(uniqueNumToCalc)
    for x in uniqueNumToCalc:
#         print('x:', x, end=' ')
        if isPrime(x):
            cnt += 1
#             print(f'>>> prime <<< cnt: {cnt}')
#         else:
#             print(f'...   no  ... cnt: {cnt}')
    print('*/\*'*25)
    print('cnt:', cnt)
    return cnt


def anothersSolution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, pm(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)


if __name__ == '__main__':
    mySolution('17')  # 3
    mySolution('011')  # 2
    mySolution('0123')  # 6?
# mySolution faster x10 ~ x600
# mySolution()
# 테스트 1 〉	통과 (0.10ms, 10.4MB)
# 테스트 2 〉	통과 (2.37ms, 10.5MB)
# 테스트 3 〉	통과 (0.04ms, 10.4MB)
# 테스트 4 〉	통과 (0.52ms, 10.4MB)
# 테스트 5 〉	통과 (1.95ms, 10.8MB)
# 테스트 6 〉	통과 (0.04ms, 10.4MB)
# 테스트 7 〉	통과 (0.10ms, 10.4MB)
# 테스트 8 〉	통과 (1.85ms, 10.7MB)
# 테스트 9 〉	통과 (0.08ms, 10.5MB)
# 테스트 10 〉	통과 (4.02ms, 10.5MB)
# 테스트 11 〉	통과 (0.66ms, 10.5MB)
# 테스트 12 〉	통과 (0.26ms, 10.5MB)

# anothersSolution()
# 테스트 1 〉	통과 (0.79ms, 10.5MB)
# 테스트 2 〉	통과 (75.87ms, 44.2MB)
# 테스트 3 〉	통과 (0.04ms, 10.3MB)
# 테스트 4 〉	통과 (53.11ms, 19.9MB)
# 테스트 5 〉	통과 (263.85ms, 145MB)
# 테스트 6 〉	통과 (1.51ms, 10.3MB)
# 테스트 7 〉	통과 (1.40ms, 10.3MB)
# 테스트 8 〉	통과 (674.01ms, 280MB)
# 테스트 9 〉	통과 (0.08ms, 10.4MB)
# 테스트 10 〉	통과 (326.28ms, 50.9MB)
# 테스트 11 〉	통과 (25.44ms, 13.8MB)
# 테스트 12 〉	통과 (6.00ms, 13.2MB)