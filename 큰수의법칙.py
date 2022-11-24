# 전체 더하기 수행 수 M
# 하나의 글자를 반복하여 더할 수 있는 횟수 K
# 가장 큰 수가 되는 반복되는 수열의 경우는
# 가장 큰 수 a와 두 번째로 큰 수 b만 수열에 포함되는 경우이다
# 예를 들어 K가 3일 때  first+first+first+second 인 경우이다
# 하나의 조합은 K+1 개의 숫자를 묶은 것이며
# 전체 더하기 수행 수인 M을 (K+1)로 나누게 되면
# 몇 번의 수열이 반복되는 지 알수 있다
# M // (K+1)
# 하지만 더하기 수행 수(M)이 (K+1)의 배수가 아닐 수 있으니
# M % (K+1)로 몇 번의 a를 더 더할 수 있는지 찾아낸다

N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

arr.sort()
first = arr[len(arr) - 1]
second = arr[len(arr) - 2]

set_cnt = M // (K+1)

result = set_cnt * K * first
result += set_cnt * second

rest = M % (K+1)

result += rest * first

print(result)
