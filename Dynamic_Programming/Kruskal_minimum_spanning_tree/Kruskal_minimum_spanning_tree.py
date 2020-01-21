class V():
    def __init__(self, id):
        self.id = id
        self.group_id = id

def connect(v0, v1):
    if v0.group_id > v1.group_id:
        v0.group_id = v1.group_id
    else:
        v1.group_id = v0.group_id

def isconnect(v0, v1):
    if v0.group_id == v1.group_id: return True
    else: return False
v0 = V(0)
v1 = V(1)
v2 = V(2)
v3 = V(3)
v4 = V(4)

connect(v0, v1)
connect(v1, v2)
connect(v3, v4)

print(v0.group_id)
print(v1.group_id)
print(v2.group_id)
print(v3.group_id)
print(v4.group_id)

print('is v0, v1?:', isconnect(v0, v1))
print('is v2, v3?:', isconnect(v2, v3))



## Kruskal minumum spanning tree
# with open("./union_find.txt") as f:
#     data = f.read()
if __name__ == "__main__":
	print('*'*100)
	mV, mE = map(int, input().split())
	print(mV, mE)
	K = map(int, input())
	print('K:', K)

	import sys
	INF = -1#sys.maxsize
	graph = [[INF]*mV for _ in range(mV)]
	for _ in range(mE):
	    u, v, w = map(int, input().split())
	    u, v = u-1, v-1
	    print(u,v,w)
	    graph[u][v] = w
	    graph[v][u] = w
	for item in graph:
	    print(item)
	print('*'*50)
