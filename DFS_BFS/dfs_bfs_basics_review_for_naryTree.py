class Node():
    def __init__(self, idx):
        self.idx = idx
        self.children = list()
    def connect(self, node):
        self.children.append(node)
    
root = Node(0)
c1 = Node(1)
c2 = Node(2)
c3 = Node(3)
c4 = Node(4)
c5 = Node(5)
c6 = Node(6)

root.connect(c1)
root.connect(c2)

c1.connect(c3)
c1.connect(c4)

c4.connect(c5)
c4.connect(c6)

print(root.children[0].children[1].children[0])
print(root.children[0].children[1].children[0].idx)


def DFS(root):
    stack = [root]
    visted = list()
    while stack:
        mem = stack.pop()
        for child in mem.children:
            stack.append(child)
        visted.append(mem.idx)
    return visted
    
def BFS(root):
    queue = [root]
    visted = list()
    while queue:
        mem = queue.pop(0)
        for child in mem.children:
            queue.append(child)
        visted.append(mem.idx)
    return visted
    
print(DFS(root))
