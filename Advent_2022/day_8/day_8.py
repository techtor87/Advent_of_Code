def print_forest(vis_table):
    for row in vis_table:
        print(''.join(row))
    print("")


puzzle_input = open("day_8_data.txt").read().strip()

puzzle_rows = puzzle_input.splitlines()

is_visible = [[' ']*len(puzzle_rows[0]) for i in range(len(puzzle_rows))]

vis_count = 0

# From Top Left
for x in range(len(puzzle_rows)):
    max_height = 0
    for y in range(len(puzzle_rows[x])):
        if int(puzzle_rows[x][y]) > max_height:
            max_height = int(puzzle_rows[x][y])
            if puzzle_rows[x][y] != 'v':
                is_visible[x][y] = 'v'
                vis_count += 1
print_forest(is_visible)

# From Top Right
for x in range(len(puzzle_rows)):
    max_height = 0
    for y in range(len(puzzle_rows[x])-1, 0, -1):
        if int(puzzle_rows[x][y]) > max_height:
            max_height = int(puzzle_rows[x][y])
            if puzzle_rows[x][y] != 'v':
                is_visible[x][y] = 'v'
                vis_count += 1
print_forest(is_visible)

# From Bottom Left
for x in range(len(puzzle_rows)):
    max_height = 0
    for y in range(len(puzzle_rows[x])):
        if int(puzzle_rows[y][x]) > max_height:
            max_height = int(puzzle_rows[y][x])
            if puzzle_rows[y][x] != 'v':
                is_visible[y][x] = 'v'
                vis_count += 1
print_forest(is_visible)

# From Bottom Right
for x in range(len(puzzle_rows)):
    max_height = 0
    for y in range(len(puzzle_rows[x])-1, 0, -1):
        if int(puzzle_rows[y][x]) > max_height:
            max_height = int(puzzle_rows[y][x])
            if puzzle_rows[y][x] != 'v':
                is_visible[y][x] = 'v'
                vis_count += 1
print_forest(is_visible)

double_check = 0
for x in range(len(puzzle_rows)):
    for y in range(len(puzzle_rows)):
        if is_visible[y][x] == 'v':
            double_check += 1

print(vis_count)


d=[x.strip()for x in open('day_8_data.txt').readlines()]
r,v=99+98+98+97,0
m=[(-1,0),(1,0),(0,-1),(0,1)]
for p in [0,1]:
 for i in range(1,len(d)-1):
  for j in range(1,len(d)-1):
   s=1
   for k in m:
    c,x,y=0,i+k[0],j+k[1]
    while 0<x<len(d)-1>y>0 and d[i][j]>d[x][y]and p==0:x,y=x+k[0],y+k[1]
    if d[i][j]>d[x][y]and(x==0 or x==len(d)-1 or y==0 or y==len(d)-1)and p==0:r+=1;break
    while 0<=x<=len(d)-1>=y>=0<p:
     c+=1
     if d[i][j]<=d[x][y]:break
     x,y=x+k[0],y+k[1]
    s*=c
   v=max(v,s)
print(r,v)
