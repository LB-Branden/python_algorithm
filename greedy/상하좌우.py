N = int(input())
# cmd = list(map(str, input().split()))
cmd = input().split()  # 이 방식을 사용하자 위와 같다
x = 1
y = 1

for c in cmd:
    if c == 'U' and x != 1:
        x -= 1
        continue
    if c == 'D' and x != N:
        x += 1
        continue
    if c == 'L' and y != 1:
        y -= 1
        continue
    if c == 'R' and y != N:
        y += 1
        continue
print('now', x, y)

# 다른 풀이 방식
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']
nx = 0
ny = 0

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or nx > n:
        continue
    x, y = nx, ny
print(x, y)
