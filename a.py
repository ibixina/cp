r, g, b = map(int, input().split())
ar, ag, ab = map(int, input().split())
x, y = map(int, input().split())

needed_r, needed_g, needed_b = r - ar, g - ag, b - ab

s = 0
if needed_r > 0:
    x = x - needed_r
    s += needed_r
if needed_b > 0:
    y = y - needed_b
    s += needed_b

if x < 0  or y < 0:
    print(-1)
    exit()

if needed_g > 0:
    if x + y < needed_g:
        print(-1)
        exit()
    s += needed_g

print(s)
