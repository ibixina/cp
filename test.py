n, k = map(int, input().split())
diffs = set()
for i in range(n):
    i = input()
    diffs.add(i)

print(min(k, len(diffs)))
