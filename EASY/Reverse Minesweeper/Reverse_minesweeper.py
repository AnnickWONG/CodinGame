w = int(input())
h = int(input())
input_grid=[]
for i in range(h):
    input_grid.append(list(input()))

output_grid = []
for i in range(h):
    output_grid.append([0 for i in range(w)])

for r in range(h):
    for c in range(w):
        if input_grid[r][c] == 'x':
            output_grid[r][c] = -1
            for i in range(r-1,r+2):
                for j in range(c-1,c+2):
                    if not (i==r and j==c):
                        if (i>=0 and i<h) and (j>=0 and j<w) :
                            if output_grid[i][j] != -1:
                                output_grid[i][j] += 1

for i in range(h):              
    stro = "".join('%s' %id for id in output_grid[i])
    stro = stro.replace('0','.')
    stro = stro.replace('-1','.')
    print(stro)
