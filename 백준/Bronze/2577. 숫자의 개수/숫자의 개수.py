a = int(input())
b = int(input())
c = int(input())

num_list = [
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
]

result = str(a * b * c)

for num in num_list:
    print(result.count(num))