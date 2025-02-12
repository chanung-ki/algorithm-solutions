import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
pokemons = {}
for i in range(n):
    name = input().strip()
    number = str(i + 1)
    pokemons[name] = number
    pokemons[number] = name

for _ in range(m):
    input_name = input().strip()
    sys.stdout.write(pokemons[input_name] + '\n')