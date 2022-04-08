# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    delta_y = light_y - initial_ty
    delta_x = light_x - initial_tx
    
    if remaining_turns > 0:
        while delta_y!=0 or delta_x!=0:
            if delta_y>0:
                D_y = 'S'
                delta_y-=1
            elif delta_y<0:
                D_y = 'N'
                delta_y+=1
            else:
                D_y=''

            if delta_x>0:
                D_x = 'E'
                delta_x-=1
            elif delta_x<0:
                D_x = 'W'
                delta_x+=1
            else:
                D_x=''

            D = D_y + D_x
            print(D)
