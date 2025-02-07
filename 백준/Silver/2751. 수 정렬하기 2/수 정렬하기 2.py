import sys

n = int(input())  # 입력 받기
nums = [int(sys.stdin.readline()) for _ in range(n)] 

nums.sort()

print('\n'.join(map(str, nums)))