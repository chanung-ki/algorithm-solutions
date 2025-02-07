n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = 0

for i in range(n):
    min_num = min(a)
    max_num = max(b)
    
    a.remove(min_num)
    b.remove(max_num)
    
    result += min_num * max_num
    
print(result)