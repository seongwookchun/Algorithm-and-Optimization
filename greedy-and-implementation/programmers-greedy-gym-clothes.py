def solution(n, lost, reserve):
    arr = [0] + [1] * (n)
    for i in lost:
        arr[i] = 0
    for i in reserve:
        arr[i] += 1
    cnt = 0
    print(arr)
    print('='*50)
    for i in range(1, n):
        if arr[i] > 0:
            cnt += 1
        if arr[i] == 0:
            if arr[i - 1] == 2:
                arr[i - 1] = 1
                cnt += 1
            elif arr[i + 1] == 2:
                arr[i + 1] = 1
                cnt += 1
        print('-'*50)
        print(arr)
                
        print(f'i:{i} cnt:{cnt} arr[i-1]:{arr[i-1]} arr[i]:{arr[i]}')
                
    if arr[n] == 0 and arr[n - 1] == 2 or arr[n] > 0:
        cnt += 1
            
                    
    return cnt

if __name__ == '__main__':
    solution(5,	[2, 4],	[1, 3, 5]) # 5