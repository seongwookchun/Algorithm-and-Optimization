def solution(citations):
    h = len(citations)
    while h > 0:
        filtered = list(filter(
            lambda x: x >= h, citations))
        print('-'*25)
        print(f'h: {h}')
        print(filtered)
        if len(filtered) == h:
            return h
        h -= 1
    return 0

def solutionCnt(citations):
    n = len(citations)
    for h in range(n,-1,-1):
        cnt = 0
        for citation in citations:
            if citation >= h:
                cnt = cnt + 1
        if cnt >= h:
            answer = h
            return answer

def teacherSolution(citations):
    citations.sort()
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            # 논문이 인용된 횟수(h번 이상) >= 인용된 논문의 개수(h개 == h번)
            return l-i
    return 0
if __name__ == '__main__':
    case = [3, 0, 6, 1, 5]
    # print(solution(case))
    # print(solution([0,0]))
    # print(solution([5,5,5,5,5]))
    # print(solution([0]))
    # print(solution([1]))
    # print(solution([2]))
    # print(solution([6,5,4,1,0]))  # 3
    print(solution([0,0,0]))        # 0
    # 정확성 테스트 1~16 중에서
    # 테스트 16 〉	실패
    # print(teacherSolution(case))




# O(N*N) my solution - using filter funtion
# 테스트 1 〉	통과 (1.62ms, 10.2MB)
# 테스트 2 〉	통과 (3.74ms, 10.2MB)
# 테스트 3 〉	통과 (2.46ms, 10.2MB)
# 테스트 4 〉	통과 (2.36ms, 10.2MB)
# 테스트 5 〉	통과 (3.64ms, 10.2MB)
# 테스트 6 〉	통과 (5.30ms, 10.2MB)
# 테스트 7 〉	통과 (0.51ms, 10.2MB)
# 테스트 8 〉	통과 (0.03ms, 10.1MB)
# 테스트 9 〉	통과 (0.02ms, 10.1MB)
# 테스트 10 〉	통과 (0.89ms, 10.2MB)
# 테스트 11 〉	통과 (6.67ms, 10.2MB)
# 테스트 12 〉	통과 (0.04ms, 10.2MB)
# 테스트 13 〉	통과 (3.98ms, 10.2MB)
# 테스트 14 〉	통과 (2.70ms, 10.2MB)
# 테스트 15 〉	통과 (4.77ms, 10.1MB)
# 테스트 16 〉	통과 (0.03ms, 10.1MB)


# O(N*N) using cnt variable
# 테스트 1 〉	통과 (1.02ms, 10.3MB)
# 테스트 2 〉	통과 (2.57ms, 10.2MB)
# 테스트 3 〉	통과 (1.56ms, 10.2MB)
# 테스트 4 〉	통과 (1.51ms, 10.1MB)
# 테스트 5 〉	통과 (2.45ms, 10.1MB)
# 테스트 6 〉	통과 (3.20ms, 10.3MB)
# 테스트 7 〉	통과 (0.25ms, 10MB)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)
# 테스트 9 〉	통과 (0.01ms, 10.2MB)
# 테스트 10 〉	통과 (0.48ms, 10.1MB)
# 테스트 11 〉	통과 (4.26ms, 10.3MB)
# 테스트 12 〉	통과 (0.02ms, 10.3MB)
# 테스트 13 〉	통과 (2.22ms, 10.1MB)
# 테스트 14 〉	통과 (2.17ms, 10.2MB)
# 테스트 15 〉	통과 (2.86ms, 10.2MB)
# 테스트 16 〉	통과 (0.01ms, 10.2MB)

# O(N logN)  using sort
# 테스트 1 〉	통과 (0.06ms, 10.2MB)
# 테스트 2 〉	통과 (0.10ms, 10.1MB)
# 테스트 3 〉	통과 (0.08ms, 10.2MB)
# 테스트 4 〉	통과 (0.07ms, 10.2MB)
# 테스트 5 〉	통과 (0.09ms, 10.2MB)
# 테스트 6 〉	통과 (0.11ms, 10.2MB)
# 테스트 7 〉	통과 (0.04ms, 10.2MB)
# 테스트 8 〉	통과 (0.01ms, 10.2MB)
# 테스트 9 〉	통과 (0.01ms, 10.2MB)
# 테스트 10 〉	통과 (0.04ms, 10.2MB)
# 테스트 11 〉	통과 (0.75ms, 10.2MB)
# 테스트 12 〉	통과 (0.02ms, 10.1MB)
# 테스트 13 〉	통과 (0.10ms, 10.2MB)
# 테스트 14 〉	통과 (0.10ms, 10.1MB)
# 테스트 15 〉	통과 (0.11ms, 10.2MB)
# 테스트 16 〉	통과 (0.01ms, 10.2MB)
