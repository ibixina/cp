r, c, n = map(int, input().split())

towers = []
for i in range(n):
    x, y = map(int, input().split())
    towers.append((x - 1, y - 1))

def manhattan(point, dest):
    a, b = point
    x, y = dest
    return abs(a - x) + abs(b - y)


def get_all_indexes(my_list, element):
    return [index for index, value in enumerate(my_list) if value == element]

second = []
for i in range(r):
    secon = []
    for j in range(c):
        distances = [manhattan(towers[k], (i, j)) for k in range(n)]
        sorted_distances = sorted(distances)
        min_distance = min(distances)
        index_of_min = distances.index(min_distance)
        indexes_of_second = get_all_indexes(distances, sorted_distances[1])
        indexe_of_second = indexes_of_second[0] if indexes_of_second[0] != index_of_min else indexes_of_second[1]
        print(index_of_min + 1, end=" ")
        secon.append(indexe_of_second + 1)

    second.append(secon)
    print()


for i in second:
    print(" ".join(map(str, i)))
