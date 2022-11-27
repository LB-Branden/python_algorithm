# 기본적 풀이 방법
N, K = map(int, input().split())
ans = 0

while True:
    if N == 1:
        break
    if N % K == 0:
        N = N / K
    else:
        N = N - 1
    ans += 1

print(ans)

# 효율성을 높인 풀이 방법1
N, K = map(int, input().split())
ans = 0
while True:
    print('N', N)
    if N >= K:
        left = N

        N = N // K
        left -= N * K
        ans += 1
        ans += left
    else:
        if N == 1:
            break
        N -= 1
print(ans)

# 효율성을 높인 풀이 방법2
N, K = map(int, input().split())
ans = 0
while True:
    if N >= K:
        target = (N // K) * K
        ans += (N - target)
        ans += 1
        N = N // K
    else:
        if N == 1:
            break
        N -= 1
