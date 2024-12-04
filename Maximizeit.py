from itertools import product


k, m = map(int, input().split())
lists = []

for _ in range(k):
    _, *elements = map(int, input().split())
    lists.append(elements)


combinations = product(*lists)


max_value = 0
for combination in combinations:
    value = sum(x**2 for x in combination) % m
    max_value = max(max_value, value)


print(max_value)
