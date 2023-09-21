N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

min_F = float('inf')

for i in range(N - M + 1):
    min_F = min(min_F, A[i + M - 1] - A[i])

print(min_F)
