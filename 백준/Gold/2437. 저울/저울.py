n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

result = 1

for num in numbers:
    
    if result < num :
        break
    
    result += num
    
print(result)