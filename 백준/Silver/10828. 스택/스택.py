import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    command = sys.stdin.readline()
    
    match command.split():
        case ['push', value]:
            stack.append(int(value))
        case ['pop']:
            if stack:
                sys.stdout.write(str(stack.pop()) + '\n')
            else:
                sys.stdout.write('-1' + '\n')
        case ['size']:
            sys.stdout.write(str(len(stack)) + '\n')
        case ['empty']:
            if stack:
                sys.stdout.write('0' + '\n')
            else:
                sys.stdout.write('1' + '\n')
        case ['top']:
            
            if stack:
                sys.stdout.write(str(stack[-1]) + '\n')
            else:
                sys.stdout.write('-1' + '\n')