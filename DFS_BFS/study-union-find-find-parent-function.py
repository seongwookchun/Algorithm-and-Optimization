# findRootMy 가 틀린 이유는?!

def findRootMy(i):
    if root[i] == i: return root[i]
    root[i] = findRootMy(root[i])
def findRootTeacher(i):
    if root[i] != i: 
        root[i] = findRootTeacher(root[i])
    return root[i]
def union(i, j, findRoot):
#     nonlocal root
    a = findRoot(i)
    b = findRoot(j)
    if a < b:
        root[b] = a#root[i]
    else:
        root[a] = b#root[j]


net = [
    [1,1,0,1,0,0],
    [1,1,1,0,0,0],
    [0,1,1,0,0,0],
    [1,0,0,1,0,0],
    [0,0,0,0,1,1],
    [0,0,0,0,1,1],
]
n = 6
root = [_ for _ in range(n)]


print('='*50)
print(root)
print('-'*50)
for i in range(1, n-1):
    for j in range(i+1, n):
# for i in range(n):
#     for j in range(n):
        if i == j: continue
        if net[i][j] == 1:
            union(i, j, findRootRootMy)
        print(root)
        

print('='*50)
print(root)
print('-'*50)
for i in range(1, n-1):
    for j in range(i+1, n):
# for i in range(n):
#     for j in range(n):
        if i == j: continue
        if net[i][j] == 1:
            union(i, j, findRootTeacher)
        print(root)