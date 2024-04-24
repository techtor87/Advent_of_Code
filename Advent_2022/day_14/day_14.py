
def build_cave(line):
    points = line.split(' -> ')
    for i in range(len(points) - 1):
        build_line(points[i], points[i + 1])


def build_line(p1, p2):
    step = 1
    x1, y1 = map(int, p1.split(','))
    x2, y2 = map(int, p2.split(','))
    if x1 == x2:
        if y1 > y2:
            step = -1
        for i in range(y1, y2, step):
            cave[i][x1-x_min] = '#'
    if y1 == y2:
        if x1 > x2:
            step = -1
        for i in range(x1, x2, step):
            cave[y1][i-x_min] = '#'

    cave[y1][x1-x_min] = '#'
    cave[y2][x2-x_min] = '#'


def sand_drop(starting_pos):
    sand_pos = starting_pos
    try:
        while sand_pos is not None:
            sand_pos, final_pos = sand_tick(sand_pos)
            if final_pos == starting_pos:
                return False

    except IndexError:
        # fell out of sandbox
        return False
    return True


def sand_tick(cur_pos):
    try:
        if cur_pos[0] >= len(cave[0]):
            for i in range(x_min, x_min+len(cave[0])+2):
                cave[i].append('')

        if cave[cur_pos[1]+1][cur_pos[0]] != '#' and cave[cur_pos[1]+1][cur_pos[0]] != 'o':
            return (cur_pos[0], cur_pos[1]+1), (cur_pos[0], cur_pos[1]+1)
        elif cave[cur_pos[1]+1][cur_pos[0]-1] != '#' and cave[cur_pos[1]+1][cur_pos[0]-1] != 'o':
            return (cur_pos[0]-1, cur_pos[1]+1), (cur_pos[0]-1, cur_pos[1]+1)
        elif cave[cur_pos[1]+1][cur_pos[0]+1] != '#' and cave[cur_pos[1]+1][cur_pos[0]+1] != 'o':
            return (cur_pos[0]+1, cur_pos[1]+1), (cur_pos[0]+1, cur_pos[1]+1)
        else:
            cave[cur_pos[1]][cur_pos[0]] = 'o'
            return None, (cur_pos[0], cur_pos[1])
    except Exception as err:
        raise err


puzzle_input = open("day_14_data.txt").readlines()

x_max, y_max, x_min = 0, 0, 1000
for line in puzzle_input:
    points = line.split(' -> ')
    for point in points:
        x, y = map(int, point.split(','))

        # if x > x_max:
        #     x_max = x
        # if x < x_min:
        #     x_min = x

        if y > y_max:
            y_max = y

x_min = 500 - y_max - 5
x_max = 500 + y_max + 5
cave = [[' ']*(x_max-x_min+1+y_max) for i in range(y_max+3)]
puzzle_input.append(f'{x_min},{y_max+2} -> {len(cave[0])-1+x_min},{y_max+2}')
for line in puzzle_input:
    build_cave(line.strip())

sand_count = 0
falling_sand = True
while falling_sand:
    falling_sand = sand_drop((500-x_min, 0))
    sand_count += 1

print(sand_count-1)
