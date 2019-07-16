'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Hello World")
def describe(lis):
    print("********************")
    l_temp = [item for item in lis]    # python just connects origin list object to new object
                                       # if you want to copy an list object without connection
                                       # using for loop
    # for i in range(len(lis)):
    #     l_temp.append(lis[i])
    l0 = []
    l1 = []
    l2 = []
    for i in range(len(lis)):
        temp = l_temp.index(lis[i])
        # print("lis.index(lis[", i, "])", temp)
        
        if(lis[i] == 0):
            l0.append(temp)
        elif(lis[i] == 1):
            l1.append(temp)
        elif(lis[i] == 2):
            l2.append(temp)
        l_temp[temp] = -1    # to avoid bad print
    print("l_top[] :", l_top)
    print(l0[::-1])
    print(l1[::-1])
    print(l2[::-1])
    print("********************")

num = int(input("how many blocks"))
ini = int(input("initial position of the top?"))
l_top = [ini for _ in range(num)]
des = int(input("where to move the top?")    )

def han(lv, x):
    print("han(", lv, ",", x, ") has been called")
    # if(lv == 0):
    #     l_top[lv] = x
    #     describe(l_top)
    # elif(l_top[lv-1] == l_top[lv]):     # should be modified because it is not enough condition
                                        # what if : move lv 3 to pos l2
                                        # [0] 3 0
                                        # [1] 1
                                        # [2]
    # else:
    if(l_top.index(l_top[lv]) != lv): # however this condition is not the solution for the error.
        pos = 3-(x+l_top[lv])    # 3 - (destination + current position) -> position with extra space
        han(lv-1, pos)
    
    # if(l_top.index(l_top[lv]) == lv):
    # else:
    print("lv:", lv, " move to x:", x)
    l_top[lv] = x    # to move lv th block to destination
    describe(l_top)
    # print("l_top[] in han :", l_top)
    # for i in range(lv-1,-1,-1):
    if(lv!=0):
        print("let's burn", end=" ")
        han(lv-1, x)

# print("l_top[] in han :", l_top)
describe(l_top)
han(num-1, des)
# for i in range(10-1,-1,-1):
#     print(i)
# for i in range(-1, -1, -1):
#     print("hi")
