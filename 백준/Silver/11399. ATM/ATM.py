n = int(input())
p = list(map(int, input().split()))
p.sort()

result = 0
accumulated_time = 0

for time in p:
    accumulated_time += time
    result += accumulated_time

print(result)