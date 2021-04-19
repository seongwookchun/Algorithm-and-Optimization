import time

def testModifying(arrSize):
    timeInit = time.time()
    arr = [0]*arrSize
    for i in range(len(arr)):
        arr[i] = 1
    return time.time() - timeInit
def testAppending(arrSize):
    timeInit = time.time()
    arr = []
    for i in range(len(arr)):
        arr.append(1)
    return time.time() - timeInit
def main(testIterationNum, arrSize):
    mem = [0, 0]
    for tsNum in range(testIterationNum):
        mem[0] += testModifying(arrSize)
        mem[1] += testAppending(arrSize)
    print(f'testIterationNum: {testIterationNum}')
    print(f'arrSize: {arrSize}')
    print(f'total testModifying: {mem[0]}')
    print(f'total testAppending: {mem[1]}')
    print(f'avg testModifying: {mem[0]/arrSize}')
    print(f'avg testAppending: {mem[1]/arrSize}')
    whichFaster = "modyfing" if mem[0] < mem[1] else "appending"
    print(f'which faster: {whichFaster}')
    
    
    
if __name__ == '__main__':
    n = 100#sys.argv[1]
    arrSize = int(1e+6)#sys.argv[2]
    main(n, arrSize)
