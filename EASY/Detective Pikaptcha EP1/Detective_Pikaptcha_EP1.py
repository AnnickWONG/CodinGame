width, height = [int(i) for i in input().split()]
input_grid = []
for i in range(height):
    line = input()
    input_grid.append(list(line))

output_grid = []
for i in range(height):
    output_grid.append([-1 for i in range(width)])

for h in range(height):
    for w in range(width):
        if input_grid[h][w] != '#':
            count = 0
            for i in [h-1,h+1]:
                if (i>=0 and i<height) and input_grid[i][w] != '#':
                    count += 1
            for j in [w-1,w+1]:
                if (j>=0 and j<width) and input_grid[h][j] != '#':
                    count += 1
            output_grid[h][w] = count

for h in range(height):
    stro = "".join('%s' %id for id in output_grid[h])
    stro = stro.replace('-1','#')
    print(stro)
