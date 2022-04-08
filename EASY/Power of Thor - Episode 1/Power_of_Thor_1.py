light_x, light_y, current_tx, current_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input()) 
    Direction = ''
    
    if remaining_turns > 0:
        if light_y > current_ty:
            Direction += 'S'
            current_ty += 1
        elif light_y < current_ty:
            Direction += 'N'
            current_ty -= 1

        if light_x > current_tx:
            Direction += 'E'
            current_tx += 1
        elif light_x < current_tx:
            Direction += 'W'
            current_tx -= 1

        print(Direction)
