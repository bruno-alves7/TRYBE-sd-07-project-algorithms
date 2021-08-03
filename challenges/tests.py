permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
target_time = 2
lista = []
count = 0

for element in permanence_period:
    if not isinstance(element[0], int) or not isinstance(element[1], int):
        print(None)
    for item in range(element[0], element[1] + 1):
        if item == target_time:
            count += 1

print(count)
