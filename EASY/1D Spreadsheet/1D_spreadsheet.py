# The function to find the value for the i-th cell in 1D spreadsheet
def findValue(i):
    op, arg_1, arg_2 = input_list[i]
    # print(input_list[i])
    if arg_1[0] == '$':
        if spreadsheet[int(arg_1[1:])] == None:
            return None
        else: val_1 = spreadsheet[int(arg_1[1:])]
    else: val_1 = int(arg_1)

    if op == 'VALUE':
        return val_1

    if arg_2[0] == '$':
        if spreadsheet[int(arg_2[1:])] == None:
            return None
        else: val_2 = spreadsheet[int(arg_2[1:])]
    else: val_2 = int(arg_2)

    if op == 'ADD':
        return val_1 + val_2
    elif op == 'SUB':
        return val_1 - val_2
    elif op == 'MULT':
        return val_1 * val_2
    else: return None

n = int(input())

input_list = [ [] for i in range(n)]
spreadsheet = [ None for i in range(n)]

for i in range(n):
    operation, arg_1, arg_2 = input().split()
    input_list[i] = [operation, arg_1, arg_2]

while None in spreadsheet:
    for i in range(n):
        if spreadsheet[i] == None:
            spreadsheet[i] = findValue(i)
 
for i in range(n):
    print(spreadsheet[i])
