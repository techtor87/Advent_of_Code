def move_tail(rope):
    new_head = rope[0]
    old_tail = rope[-1]

    if new_head[0] == old_tail[0]:
        if abs(new_head[1]-old_tail[1]) > 1:
            if new_head[1] > old_tail[1]:
                new_y = old_tail[1]+1
            else:
                new_y = old_tail[1]-1
            rope[-1] = (old_tail[0], new_y)
    elif new_head[1] == old_tail[1]:
        if abs(new_head[0]-old_tail[0]) > 1:
            if new_head[0] > old_tail[0]:
                new_x = old_tail[0]+1
            else:
                new_x = old_tail[0]-1
            rope[-1] = (new_x, old_tail[1])
    else:
        if abs(new_head[0]-old_tail[0]) > 1 or abs(new_head[1]-old_tail[1]) > 1:
            if new_head[0] > old_tail[0]:
                new_x = old_tail[0]+1
            else:
                new_x = old_tail[0]-1

            if new_head[1] > old_tail[1]:
                new_y = old_tail[1]+1
            else:
                new_y = old_tail[1]-1

            rope[-1] = (new_x, new_y)

    return rope


def move_long_tail(rope):
    for i in range(len(rope)-1):
        _, rope[i+1] = move_tail([rope[i], rope[i+1]])

    return rope


def print_coords(coords):
    x_lst = [i for i,j in coords]
    y_lst = [j for i,j in coords]

    x_lst.sort()
    y_lst.sort()

    x_min = x_lst[0]
    x_max = x_lst[-1]
    y_min = y_lst[0]
    y_max = y_lst[-1]

    plot = [['.']*(x_max-x_min+1) for i in range(y_max-y_min+1)]
    for xy in coords:
        newX = xy[0]-x_min
        newY = xy[1]-y_min
        plot[newY][newX] = '#'

    for row in reversed(plot):
        print(''.join(row))


puzzle_input = open("day_9_data.txt").read().strip()
puzzle_rows = puzzle_input.splitlines()

whole_rope = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]

tail_positions = set()

for row in puzzle_rows:
    dir, move_num = row.split(" ")
    for i in range(int(move_num)):
        match dir:
            case 'L':
                whole_rope[0] = (whole_rope[0][0]-1, whole_rope[0][1])
            case 'R':
                whole_rope[0] = (whole_rope[0][0]+1, whole_rope[0][1])
            case 'D':
                whole_rope[0] = (whole_rope[0][0], whole_rope[0][1]-1)
            case 'U':
                whole_rope[0] = (whole_rope[0][0], whole_rope[0][1]+1)

        whole_rope = move_long_tail(whole_rope)
        tail_positions.add(whole_rope[-1])

print_coords(list(tail_positions))
print(len(tail_positions))
