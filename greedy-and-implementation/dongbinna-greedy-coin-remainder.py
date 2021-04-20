def remainder(money):
    units = [10, 50, 100, 500]
    units.sort(reverse=True)
    lcnt = 0
    coins = list()
    for unit in units:
        print('-'*50)
        print(unit)
        while True:
            print('while')
            print(money, end='/')
            money -= unit
            if money < 0:
                print()
                print('break')
                money += unit
                break
            print(money)
            lcnt += 1
            coins.append(unit)
    print(lcnt)
    print(coins)

def teacherRemainder(money):
    units = [500, 100, 50, 10]
    cnt = 0
    for unit in units:
        cnt += money // unit
        money %= unit
        
    return cnt

def teacherRemainder2(money):
    units = [500, 100, 50, 10]
    cnt = 0
    for unit in units:
        mod, money = divmod(money, unit)
        cnt += mod
    return cnt

if __name__ == '__main__':
    remainder(3690)
    print(teacherRemainder(3690))
    print(teacherRemainder2(3690))
