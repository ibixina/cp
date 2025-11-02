import sys

X = int(input())

if X == 1:
    print("0 0")
    sys.exit(0)

def cmp_binom(n: int, k: int, X: int) -> int:
    res = 1
    for i in range(1, k + 1):
        res = res * (n - k + i) // i
        if res > X:
            return 1
    if res == X:
        return 0
    return -1

best_n, best_k = X, 1

MAX_K = 500

for k in range(2, MAX_K + 1):
    if k >= best_n:
        break

    low, high = k, best_n - 1
    found = False
    while low <= high:
        mid = (low + high) // 2
        c = cmp_binom(mid, k, X)
        if c == 0:
            if mid < best_n or (mid == best_n and k < best_k):
                best_n, best_k = mid, k
            found = True
            high = mid - 1  
        elif c < 0:
            low = mid + 1
        else:
            high = mid - 1


print(best_n, best_k)

