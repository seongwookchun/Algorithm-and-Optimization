def isPrimeMy(x):
    if x == 1: return False,
    if x == 2: return True,
    if x % 2 == 0: return False,
    root = sqrt(x)
    dividor = 3
    while dividor < root:
        if x % dividor == 0:
            return False, f'dividor: {dividor}'
        dividor += 2
    return True,

def isPrime(x):
    if x <= 3: return x > 1,  # L2 + L3  # how about zero as input?
    if x % 2 == 0 or x % 3 == 0: return False,  # improved L3
    root = int(x**0.5)                         # improved L5
    dividor = 5                                # improved L6   / 6n +- 1 form
    while dividor <= root:                     # corrected L7 
                                               # equality should be needed.
                                               # (2n+1)**2 forms
                                               # ex) 9 -> 3 * 3
                                               # ex) 25 -> 5 * 5
        if x % dividor == 0:
            return False, f'dividor: {dividor}'
        if x % (dividor +2) == 0:
            return False, f'dividor: {dividor +2}'
        dividor += 6
    return True,

cases = list(range(1, 51 +1, 2)) + [100]
for x in cases:
    print(f'x:{x} same? {isPrimeMy(x)[0] == isPrime(x)[0]} isPrimeMy/isPrime: {isPrimeMy(x)}/{isPrime(x)} ')