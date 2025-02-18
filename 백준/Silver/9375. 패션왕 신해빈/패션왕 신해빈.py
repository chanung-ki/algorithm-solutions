import sys

input = sys.stdin.readline
t = int(input().rstrip())

for _ in range(t):
    n = int(input().rstrip())
    costumes_count = {}
    
    for _ in range(n):
        _, category = input().rstrip().split()
        
        if category in costumes_count.keys():
            costumes_count[category] += 1
        else:
            costumes_count[category] = 1
    
    count = 1
    
    for key in costumes_count.keys():
        count *= costumes_count[key] + 1
        
    print(count-1)