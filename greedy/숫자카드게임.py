#문제해결 조건
#각 행마다 가장 작은 수를 찾을 뒤에 그 수들 중 가장 큰수를 고른다

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
min_arr = []

for i in range(N):
    min_arr.append(min(arr[i][:]))

print(max(min_arr))

# 개선된 버전
N, M = map(int, input().split())
result = 0

for i in range(N):
    arr = list(map(int, input().split()))
    min_val = min(arr)
    result = max(result, min_val)
print(result)

# 2중 for문 풀이
N, M = map(int, input().split())
result = 0

for i in range(N):
    min_val = 10000
    arr = list(map(int, input().split()))
    for j in range(M):
        min_val = min(min_val, arr[j])
    result = max(result, min_val)
print(result)

