# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

max_x = w - 1
max_y = h - 1

min_x = 0
min_y = 0

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    print(bomb_dir, file=sys.stderr, flush=True)

    if 'U' in bomb_dir:
        max_y = y0 - 1
    elif 'D' in bomb_dir:
        min_y = y0 + 1
    
    if 'R' in bomb_dir:
        min_x = x0 + 1
    elif 'L' in bomb_dir:
        max_x = x0 - 1
    
    x0 = int(min_x + (max_x - min_x)/2)
    y0 = int(min_y + (max_y - min_y)/2)
    
    print(f'{x0} {y0}')
