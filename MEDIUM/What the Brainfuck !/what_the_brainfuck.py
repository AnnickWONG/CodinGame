
def createmap(code):
    global normal
    temp_brace = []
    bracemap =  {}
    for position, command in enumerate(code):
        if command == "[": temp_brace.append(position)
        if command == "]":
            try:
                start = temp_brace.pop()
            except IndexError:
                print("SYNTAX ERROR")
                FLAG = False
            bracemap[start] = position
            bracemap[position] = start
    if len(temp_brace) >0:
        print("SYNTAX ERROR")
        FLAG = False
    return bracemap

l, s, n = [int(i) for i in input().split()]

array = [0 for i in range(s)]
int_list = []
line=''

for i in range(l):
    line += ''.join(filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], [x for x in input()]))
for i in range(n):
    int_list.append( int(input()) )

FLAG = True   # FLAG to capture error
int_idx = 0   # indicate the index in the integer list
pointer = 0   # indicate the position on the input line
idx = 0       # indicate the poisition on the array

bracemap = createmap(line)

while pointer < len(line) and FLAG:
    comment = line[pointer]        
    if comment == '<':
        if idx == 0:
            print("POINTER OUT OF BOUNDS")
            FLAG = False
        else: idx -= 1
    elif comment == '>':
        if idx == s-1:
            print("POINTER OUT OF BOUNDS")
            FLAG = False
        else: idx += 1
    elif comment == '+':
        array[idx] += 1
        if array[idx] > 255: 
            print("INCORRECT VALUE")
            FLAG = False
    elif comment == '-':
        array[idx] -= 1
        if array[idx] < 0: 
            print("INCORRECT VALUE")
            FLAG = False
    elif comment == '.':
        print(chr(array[idx]), end='')
    elif comment == ',':
        array[idx] += int_list[int_idx]
        int_idx += 1
        if array[idx] > 255: 
            print("INCORRECT VALUE")
            FLAG = False
    elif comment == '[' and array[idx] == 0:
        pointer = bracemap[pointer]
    elif comment == ']' and array[idx] != 0:
        pointer = bracemap[pointer]

    pointer += 1
 

