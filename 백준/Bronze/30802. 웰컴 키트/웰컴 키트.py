n = int(input())
sizes = list(map(int, input().split()))
t, p = map(int, input().split())

t_shirt_count = 0

for size in sizes:
    if size % t == 0:
        t_shirt_count += size // t
    else:
        t_shirt_count += size // t + 1
        
print(t_shirt_count)
print(n//p, n%p)