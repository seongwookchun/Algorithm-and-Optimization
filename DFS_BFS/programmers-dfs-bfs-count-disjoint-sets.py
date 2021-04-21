def solution(n, computers):
    answer = 0
    root = [_ for _ in range(n)]
    
    ######################################
    # findRootMy에서 잘못된 부분은?!
    ######################################
    # def findRootMy(i):
    #     if root[i] == i: return root[i]
    #     else:
    #         root[i] = findRoot(root[i])
    def findRoot(i):
        if root[i] != i: 
            root[i] = findRoot(root[i])
        return root[i]
        
    def union(i, j):
        nonlocal root
        a = findRoot(i)
        b = findRoot(j)
        if a < b:
            root[b] = a#root[i]
        else:
            root[a] = b#root[j]
            
        
    for i in range(len(computers) -1):
        for j in range(i+1, len(computers)):
            if i == j: continue
            if computers[i][j] == 1:
                union(i, j)
    # update
    for i in range(len(root)):
        root[i] = findRoot(i)
        
    return len(set(root))


# js solution 출처
# https://velog.io/@munyohan/%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4
function solution(n, computers) {
  let p = new Array(n);

  // 컴퓨터 개수만큼 생성
  for (let i = 0; i < n; i++) {
    make(i);
  }

  for (let i = 0; i < computers.length; i++) {
    for (let j = 0; j < computers[i].length; j++) {
      if (i === j) continue; // 자기 자신은 제외

      // 네트워크로 연결되어 있으면 한 그룹으로 union
      if (computers[i][j] === 1) {
        union(i, j);
      }
    }
  }

  const tmp = []; // 집합의 개수를 세어주기 위해 임시로 만든 배열
  for (let i = 0; i < p.length; i++) {
    const t = find(p[i]); // 최상단의 부모로 업데이트
    // tmp에 포함이 안되어있으면 새로운 집합이므로 추가
    if (!tmp.includes(t)) {
      tmp.push(t);
    }
  }

  // 집합의 개수 출력
  return tmp.length;

  function make(x) {
    p[x] = x;
  }

  function union(x, y) {
    const px = find(x);
    const py = find(y);

    if (px !== py) {
      p[py] = px;
    }
  }

  function find(x) {
    if (p[x] === x) {
      return x;
    } else {
      p[x] = find(p[x]);
      return p[x];
    }
  }
}


if __name__ == '__main__':
    solution(3,	[[1, 0, 1], [0, 1, 1], [0, 0, 1]])  # 1


## conclusion
# 성능은 아래 두 방법이 비슷하다.

## union find
# 테스트 1 〉	통과 (0.02ms, 10.3MB)
# 테스트 2 〉	통과 (0.02ms, 10.3MB)
# 테스트 3 〉	통과 (0.07ms, 10.3MB)
# 테스트 4 〉	통과 (0.07ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.1MB)
# 테스트 6 〉	통과 (0.30ms, 10.2MB)
# 테스트 7 〉	통과 (0.03ms, 10.1MB)
# 테스트 8 〉	통과 (0.20ms, 10.2MB)
# 테스트 9 〉	통과 (0.12ms, 10.1MB)
# 테스트 10 〉	통과 (0.13ms, 10.2MB)
# 테스트 11 〉	통과 (0.91ms, 10.1MB)
# 테스트 12 〉	통과 (0.73ms, 10.3MB)
# 테스트 13 〉	통과 (0.35ms, 10.2MB)

## DFS
# 테스트 1 〉	통과 (0.01ms, 10.3MB)
# 테스트 2 〉	통과 (0.01ms, 10.1MB)
# 테스트 3 〉	통과 (0.07ms, 10.2MB)
# 테스트 4 〉	통과 (0.06ms, 10.2MB)
# 테스트 5 〉	통과 (0.01ms, 10.2MB)
# 테스트 6 〉	통과 (0.30ms, 10.1MB)
# 테스트 7 〉	통과 (0.03ms, 10.2MB)
# 테스트 8 〉	통과 (0.21ms, 10.3MB)
# 테스트 9 〉	통과 (0.13ms, 10.2MB)
# 테스트 10 〉	통과 (0.14ms, 10.3MB)
# 테스트 11 〉	통과 (0.96ms, 10.3MB)
# 테스트 12 〉	통과 (0.86ms, 10.3MB)
# 테스트 13 〉	통과 (0.42ms, 10.3MB)