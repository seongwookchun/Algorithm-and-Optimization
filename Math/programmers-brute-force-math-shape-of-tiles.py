def solution(cb, cy):
    # x + y = (cb + 4) / 2
    # total num of tiles: x * y = cb + cy
    
    # ax^2 + bx + c = 0
    a = 1
    b = -int((cb + 4) / 2)
    c = cb + cy
    
    x = (-b + int((b**2) - 4 * a * c) ** 0.5) / (2 * a)
    y = -b - x
    return [x, y]