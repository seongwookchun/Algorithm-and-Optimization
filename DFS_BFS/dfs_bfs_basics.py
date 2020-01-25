# DFS
n = 7
st = [0]    # 시작노드 0으로 설정.
visited = list()
G = [[0, 1, 1, 0, 0, 0, 0],
     [1, 0, 0, 1, 1, 0, 0],
     [1, 0, 0, 0, 0, 1, 1],
     [0, 1, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0]]

while st:
    cur_node = st.pop()
    for idx in range(n):
        if G[cur_node][idx] == 1 and idx not in visited:
            st.append(idx)
    visited.append(cur_node)

print([x for x in map(lambda x: x+1, visited)])

# BFS
n = 7
q = [0]    # 시작노드 0으로 설정
visited = list()
while q:
    cur_node = q.pop(0)
    for idx in range(n):
        if G[cur_node][idx] == 1 and idx not in visited:
            q.append(idx)
    visited.append(cur_node)

print([x for x in map(lambda x: x+1, visited)])

# [1, 3, 7, 6, 2, 5, 4]
# [1, 2, 3, 4, 5, 6, 7]
