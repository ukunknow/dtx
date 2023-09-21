import itertools

n, k = map(int, input().split())
elements = list(map(int, input().split()))

unique_combinations = set()

for r in range(1, n + 1):
    for combo in itertools.combinations(elements, r):
        if sum(combo) == k and len(combo) > 1:
            unique_combinations.add(tuple(sorted(combo)))  

for combo in unique_combinations:
    print(combo)

print(len(unique_combinations))
