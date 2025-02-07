import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque([i for i in range(1, n+1)]) 

while True:
    if len(queue) == 1:
        print(queue[0])
        break
    
    # 첫번째 카드를 버림
    queue.popleft()
    # 두번째 카드를 마지막으로
    queue.append(queue.popleft())