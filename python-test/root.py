def root(head, headIndex):
    print(f'head: {head}')
    if head[headIndex] in [0, 1]:
        return head[headIndex]
    return root(head, head[headIndex])

if __name__ == '__main__':
    ans = root([0,1,0,2,3],-1)
    print(f'ans: {ans}')
