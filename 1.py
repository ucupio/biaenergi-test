def multiply(x, y):
    total = 0
    if x<0:
        while x < 0:
            total += y
        x += 1
    elif x>0:
        while x > 0:
            total += y
            x -= 1

    return total