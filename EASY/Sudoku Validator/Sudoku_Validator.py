def check_row(g):
    for i in range(9):
        if len(set(g[i])) != 9 :
            return False
    return True

def check_col(g):
    for i in range(8):
        if len(set(g[j][i] for j in range(9))) !=9:
            return False
    return True

def check_sub(g):
    for i in (0,3,6):
        for j in (0,3,6):
            if len(set(g[m][n] for m in range(i, i+3) for n in range(j, j+3))) !=9:
                return False
    return True

grid = []
for i in range(9):
    grid.append([int(x) for x in input().split()])

if not check_row(grid):
    print("false")
elif not check_col(grid):
    print("false")
elif not check_sub(grid):
    print("false")
else:
    print("true")
