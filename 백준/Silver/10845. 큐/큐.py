import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    command = sys.stdin.readline()
    
    match command.split():
        case ['push', value]:
            queue.append(int(value))
        case ['pop']:
            if queue:
                sys.stdout.write(str(queue.popleft()) + '\n')
            else:
                sys.stdout.write('-1' + '\n')
        case ['size']:
            sys.stdout.write(str(len(queue)) + '\n')
        case ['empty']:
            if queue:
                sys.stdout.write('0' + '\n')
            else:
                sys.stdout.write('1' + '\n')
        case ['front']:
            if queue:
                sys.stdout.write(str(queue[0]) + '\n')
            else:
                sys.stdout.write('-1' + '\n')
        case ['back']:
            if queue:
                sys.stdout.write(str(queue[-1]) + '\n')
            else:
                sys.stdout.write('-1' + '\n')