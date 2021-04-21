def solution(numbers, target):
    cnt = 0
    def dfs(num, summed, target):
        num = [e for e in num]  # 복사하는 과정이 있기 때문에 느리다.
#         print(num)
        if len(num) == 0 and summed == target:
            nonlocal cnt
            cnt += 1
            return
        if len(num) > 0:
            value = num.pop(0)
        else:
            return
        dfs(num, summed + value, target)
        dfs(num, summed - value, target)
    dfs(numbers, 0, target)
    return cnt


def anotherSolution(numbers, target):
     cnt = 0

     def operator(numbers, target, idx=0):
         if idx < len(numbers):
             numbers[idx] *= 1
             operator(numbers, target, idx+1)

             numbers[idx] *= -1
             operator(numbers, target, idx+1)

         elif sum(numbers) == target:
             nonlocal cnt
             cnt += 1

     operator(numbers, target)

     return cnt

    
def improvedSolution(numbers, target):
    cnt = 0
    def dfs(i, summed, target):
        nonlocal cnt
        # operator precedence
        # https://www.programiz.com/python-programming/precedence-associativity
        if i == len(numbers) and summed == target:  # == 비교 연산자 < +, - 덧셈 뺄셈 연산자
            cnt += 1
        print(i, summed, target, cnt)
        if i < len(numbers):
            dfs(i+1, summed + numbers[i], target)  # another's solution 보다 빠른 이유는?
            dfs(i+1, summed - numbers[i], target)  # 노드마다 sum을 개별적으로 계산하지 않고
                                                   # 부모노드에서 계산한 것을 전달 해주기 때문이다.
    
    dfs(0, 0, target)
    return cnt


if __name__ == '__main__':
    # solution([1, 1, 1, 1, 1]	, 3)
    n = 5
    solution([1 for _ in range(n+2)], n)
    otherSolution([1 for _ in range(n+2)], n)

    print(f'i, summed, target, cnt')
    improvedSolution([1, 1, 1]	, 1)
    
    
    
    
# my solution
# 테스트 1 〉	통과 (787.12ms, 10.1MB)
# 테스트 2 〉	통과 (749.66ms, 10.2MB)
# 테스트 3 〉	통과 (1.26ms, 10.3MB)
# 테스트 4 〉	통과 (3.83ms, 10.2MB)
# 테스트 5 〉	통과 (25.54ms, 10.1MB)
# 테스트 6 〉	통과 (2.17ms, 10.2MB)
# 테스트 7 〉	통과 (1.28ms, 10.3MB)
# 테스트 8 〉	통과 (6.36ms, 10.2MB)

# another's solution
# 테스트 1 〉	통과 (615.29ms, 9.98MB)
# 테스트 2 〉	통과 (613.97ms, 10.1MB)
# 테스트 3 〉	통과 (0.94ms, 10.2MB)
# 테스트 4 〉	통과 (2.62ms, 10.1MB)
# 테스트 5 〉	통과 (18.25ms, 10.2MB)
# 테스트 6 〉	통과 (1.52ms, 10.2MB)
# 테스트 7 〉	통과 (0.99ms, 10.2MB)
# 테스트 8 〉	통과 (5.08ms, 10.1MB)

# improved solution
# 테스트 1 〉	통과 (419.01ms, 10.2MB)
# 테스트 2 〉	통과 (414.14ms, 10.3MB)
# 테스트 3 〉	통과 (0.73ms, 10.1MB)
# 테스트 4 〉	통과 (2.09ms, 10.3MB)
# 테스트 5 〉	통과 (13.17ms, 10.2MB)
# 테스트 6 〉	통과 (1.38ms, 10.2MB)
# 테스트 7 〉	통과 (0.73ms, 10.3MB)
# 테스트 8 〉	통과 (4.14ms, 10.2MB)