import sys
m = int(sys.stdin.readline())
datas = set()
for _ in range(m):
    command_line = sys.stdin.readline().strip().split()
    command = command_line[0]
    try:
        x = int(command_line[1])
    except:
        pass
    
    match command:
        case 'add':
            datas.add((x))
        case 'remove':
            if x in datas:
                datas.remove(x)
        case 'check':
            if x in datas:
                sys.stdout.write('1'+'\n')
            else:
                sys.stdout.write('0'+'\n')
        case 'toggle':
            if x in datas:
                datas.remove(x)
            else:
                datas.add(x)
        case 'all':
            datas = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
        case 'empty':
            datas = set()