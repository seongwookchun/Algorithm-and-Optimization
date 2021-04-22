# https://programmers.co.kr/learn/courses/30/lessons/42840
# 완전탐색 - 모의고사 - lv1.
def solution(answers):
    cnt = [[i + 1, 0] for i in range(3)]
    pat2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pat3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i, ans in enumerate(answers):
        # 1, 2, 3, 4, 5, 1, 2, 3, ...
        if ans == (i % 5 + 1):
            cnt[0][1] += 1
        if ans == pat2[i % 8]:
            cnt[1][1] += 1
        if ans == pat3[i % 10]:
            cnt[2][1] += 1

    maxCnt = max([e[1] for e in cnt])
    return sorted([item[0] for item 
                            in sorted([item for item 
                                            in cnt if item[1] == maxCnt], 
                                                      key=lambda x: x[1])])



if __name__ == '__main__':
    solution([1,2,3,4,5])  # [1]
    solution([1,3,2,4,2])  # [1,2,3!]
    solution([2, 1, 1, 1, 2])  # [2, 3]