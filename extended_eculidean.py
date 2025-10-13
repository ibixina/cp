def gcd(a, b , x, y):
    if (b == 0):
        x = 1
        y = 0
        return a



    x1 = y
    y1 = x % b
    d = gcd(b, a % b, x1, y1)
    x = y1
    y = x1 - y1 * int(a / b)
    return d


def gcd_iterative(a, b, x, y):
    x, y = 1, 0

    x1 = 0
    y1= 1
    a1 = a
    b1 = b

    while b1:
        q = a1 // b1


# gcd(a,b) = max{k > 0: (k|a) and (k|b)}``

def gcd_i(a, b):
    while b:
        a = a % b
        a, b = b, a
    return a


