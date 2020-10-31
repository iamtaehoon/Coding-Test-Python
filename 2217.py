n = int(input())
list_rope = []
max_weight = 0
for i in range(n):
    x = int(input())
    list_rope.append(x)

list_rope.sort(reverse=True)

for i in range(len(list_rope)):
    if max_weight < (list_rope[i] * (i + 1)):
        max_weight = list_rope[i] * (i + 1)

print(max_weight)