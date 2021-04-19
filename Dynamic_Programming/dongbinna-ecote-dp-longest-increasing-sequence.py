import logging
log = logging.Logger('my')
log.setLevel(logging.DEBUG)
print(logging.DEBUG)
def pt(x):
    for _ in x:
        print(_)
def solution(s):#gold2D):
    dp = [1]*len(s)
    for i in range(len(s)-2, -1, -1):
        log.debug(print('='*50))
        log.debug(print(f'i:{i}'))
        temp = 1
        # for j in range(i+1, len(s)):
        lcnt = i+1
        flag = False
        while(lcnt < len(s)):
            j = lcnt
            log.debug(print(f's[i]/s[j]: {s[i]}/{s[j]}'))
            log.debug(print(f'dp: {dp}'))
            log.debug(print(f'temp before: {temp}'))
            if s[i] >= s[j]:
                temp = max(temp, dp[j])
                flag = True
            log.debug(print(f'temp after : {temp}'))
            lcnt += 1
            
        if flag == True:
            dp[i] = temp + 1
        log.debug(print(f'-'*50))
        log.debug(print(f'dp: {dp}'))
    log.debug(print(f'='*50))
    log.debug(print(f'dp: {dp}'))
    ans = len(s) - max(dp)
            
    print(ans)
    return ans
# print(solution())

def teacherSolution1(s):
    dp = [1]*len(s)
    for i in range(len(s)-1, -1, -1):
        for j in range(i+1, len(s)):
            if s[i] >= s[j]:
                dp[i] = max(dp[i], dp[j]+1)
    print(dp)
    
def teacherSolution2_LIS(s):  # Longest Increasing Sequence
    dp = [1]*len(s)
    s = list(reversed(s))  # same as dp.reverse()
    print(s)
    
    for i in range(len(s)):
        for j in range(0, i):
            if s[j] <= s[i]:
                dp[i] = max(dp[i], dp[j]+1)
    print(dp)
if __name__ == '__main__':
    s = [15, 14, 4, 8, 5, 2, 4]  # => [15, 14, 8, 5, 4] / 2명 열외
    # solution(s)
    # teacherSolution1(s)
    teacherSolution2_LIS(s)
