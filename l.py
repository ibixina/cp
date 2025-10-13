input()
dists = list(map(int, input().split()))


a = dists[0] / 3
b = dists[-1] / 3

c = dists[-2] - 2 * b

sol = sorted([int(a), int(b), int(c)])
print(f"{sol[0]} {sol[1]} {sol[2]}")
