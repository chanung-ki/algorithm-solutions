import sys
n = int(sys.stdin.readline())
coordinates = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

coordinates.sort(key=lambda x: (x[1], x[0]))

for coordinate in coordinates:
    sys.stdout.write(f'{coordinate[0]} {coordinate[1]}' + '\n')