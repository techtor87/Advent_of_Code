import copy

data = []
with open("day_12_data.txt") as file:
    row = -1
    for line in file.readlines():
        line = line.strip()
        row += 1
        for col in range(len(line)):
            if line[col] == 'S':
                line = line.replace('S', 'a')
                end = (row, col)
            elif line[col] == 'E':
                line = line.replace('E', 'z')
                start = (row, col)
        data.append(line)

paths = [[start, set()]]


def isNotInClosedList(pos, allPaths):
    for path in allPaths:
        if pos in path[1] or pos == path[0]:
            return False
    return True


while True:
    path = paths[0]
    paths = paths[1:]

    if data[path[0][0]][path[0][1]] == 'a':
        print(f"Solution: {len(path[1])}")
        break

    current = path[0]
    closed = path[1]

    for move in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        moved = (current[0] + move[0], current[1] + move[1])
        if moved not in closed and \
            0 <= moved[0] < len(data) and \
            0 <= moved[1] < len(data[moved[0]]) and \
                isNotInClosedList(moved, paths):

            a = ord(data[moved[0]][moved[1]])
            b = ord(data[current[0]][current[1]])
            if b - a <= 1:
                newpath = copy.deepcopy(path)
                newpath[1].add(tuple(current))
                newpath[0] = moved
                paths.append(newpath)
