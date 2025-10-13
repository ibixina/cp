MOD = 998244353 #prime mod

def solve(n,k):
    #compute n * (2k)^(2k)
    numerator = (n % MOD) * pow(2*k, 2*k, MOD) % MOD
    #compute (2k + 1)^(2k)
    denominator = pow((2*k + 1) , 2*k, MOD)
    #compute modular inverse of denominator using Fermat's Little Theorem
    inverse = pow(denominator, MOD - 2, MOD)
    answer = numerator * inverse % MOD
    return answer

n, k = map(int, input().split())
answer = solve(n,k)
print(answer)
