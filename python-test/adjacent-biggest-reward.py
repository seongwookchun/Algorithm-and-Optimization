def root(head, headIndex):
    if head[headIndex] in [0, 1]:
        return head[headIndex]
    return root(head, head[headIndex])
    
def solution(money):
    dp = list()
    dp.extend(money[:2])
    head = [0,1]#list()#[0]*len(money)#list()
    for i in range(2, len(money)):
        if dp[i-1] > dp[i-2] + money[i]:
            dp.append(dp[i-1])
            head.append(i-1)
        else:
            dp.append(dp[i-2] + money[i])
            head.append(i-2)
    # if dp[-1] != dp[-2]:
    #     rt = root(head, -1)
    #     if rt == 0: return dp[-2] 
    return dp[-1]
        # dp.append(max(dp[i-1], dp[i-2] + money[i]))
    ans = dp[-1]
    # print(f'root: {rt}')
    print(ans)
    print('money')
    print(money)
    print('dp')
    print(dp)
    print('head')
    print(list(range(len(head))))
    print(head)
    return ans
    
    
    
if __name__ == '__main__':
    money = [1,2,3,1,4,5,6]
    solution(money)
