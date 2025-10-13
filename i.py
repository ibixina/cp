n = int(input())
additional = list(map(int, input().split()))

sols = list(map(int, input().split()))

su = 0

best = 0

for i in range(n):
    su += sols[i]
    total_su = su + additional[i]
    avg = total_su / n
    best = max(best, avg)
    
print(best)
