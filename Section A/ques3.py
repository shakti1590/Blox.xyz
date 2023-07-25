import math
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
def find_unit_distance_pairs(point_set):
    n = len(point_set)
    unit_distance_pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            distance = euclidean_distance(point_set[i], point_set[j])
            if distance == 1:
                unit_distance_pairs.append((point_set[i], point_set[j]))
    return unit_distance_pairs
half_convex_point_set = [(1, 2), (2, 2), (3, 3), (4, 3),(4, 4), (3, 5), (2, 5), (1, 4)]
result = find_unit_distance_pairs(half_convex_point_set)
print(result)
