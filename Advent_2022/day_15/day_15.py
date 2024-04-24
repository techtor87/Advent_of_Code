import re

cave = []
x_min, y_min = 0, 0


def distance(p1, p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])


def build_scan(sensor, beacon):
    sensor_distance = distance(sensor, beacon)
    for y in range(len(cave)):
        for x in range(len(cave[y])):
            if distance((sensor[0]-x_min, sensor[1]-y_min), (x, y)) <= sensor_distance:
                cave[y][x] = '#'


def in_shape(cnt_set, sensor, row):
    if distance(sensor[0], (sensor[0][0], row)) < sensor[2]:
        in_shape = True
        dist = 0
        while in_shape:
            in_shape = False
            if distance(sensor[0], (sensor[0][0]+dist, row)) <= sensor[2]:
                cnt_set.add(sensor[0][0]+dist)
                in_shape = True

            if distance(sensor[0], (sensor[0][0]-dist, row)) <= sensor[2]:
                cnt_set.add(sensor[0][0]-dist)
                in_shape = True

            dist += 1
    return cnt_set


test_data = True
puzzle_input = open("day_15_test_data.txt").readlines() if test_data else open("day_15_data.txt").readlines()
x_list = []
y_list = []
sensor_list = []
for line in puzzle_input:
    results = re.search(r"Sensor at x=(-?\d*), y=(-?\d*): closest beacon is at x=(-?\d*), y=(-?\d*)", line)
    x1, y1, x2, y2 = map(int, results.groups())
    sensor_list.append(((x1, y1), (x2, y2), distance((x1, y1), (x2, y2))))
    x_list.extend([x1, x2])
    y_list.extend([y1, y2])


part_1 = True
if part_1:
    y = 10 if test_data else 2000000
    cnt_set = set()
    for sensor in sensor_list:
        cnt_set = in_shape(cnt_set, sensor, y)

    for sensor in sensor_list:
        if sensor[1][1] == y and sensor[1][0] in cnt_set:
            cnt_set.remove(sensor[1][0])

    print(f"Row {y} - {len(cnt_set)}")


# PART 2 - BRUTE FORCE - WORKS EVENTUALLY
min_coord = 0
max_coord = 21 if test_data else 4000001
x_mult = 4000000
instersect_set = set(range(min_coord, max_coord))
cnt_set = [set() for i in range(max_coord-min_coord)]

for y in range(min_coord, max_coord):
    for sensor in sensor_list:
        if distance(sensor[0], (sensor[0][0], y)) <= sensor[2]:
            cnt_set[y] = in_shape(cnt_set[y], sensor, y)

    cnt_set[y] = cnt_set[y].intersection(instersect_set)
    cnt_set[y] = instersect_set.difference(cnt_set[y])

    for i in cnt_set[y]:
        freq = y + i * x_mult
        print(i, y, freq)
        break
    else:
        print(y)
