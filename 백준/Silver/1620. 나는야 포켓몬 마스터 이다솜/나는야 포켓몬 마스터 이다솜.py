import sys
n, m = map(int, sys.stdin.readline().strip().split())
pokemons = {}
for i in range(n):
    name = sys.stdin.readline().strip()
    number = str(i + 1)
    pokemons[name] = number
    pokemons[number] = name

for _ in range(m):
    input_name = sys.stdin.readline().strip()
    sys.stdout.write(pokemons[input_name] + '\n')