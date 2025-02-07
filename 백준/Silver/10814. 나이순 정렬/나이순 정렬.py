n = int(input())
members = []
for _ in range(n):
    member_info = input().split()
    members.append({'age': int(member_info[0]),'name': member_info[1]})
    
members.sort(key=lambda x: x['age'])

for member in members:
    print(member['age'], member['name'])