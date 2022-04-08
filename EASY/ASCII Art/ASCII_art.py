l = int(input())
h = int(input())
t = input()
c=list()
for i in range(h):
    row = input()
    c.append(row)

i_list=list()
for letter in t:
    index = ord(letter)
    if 65<=index<=90:
        index = index - 65
    elif 97<=index<=122:
        index = index - 97
    else:
        index = 26
    i_list.append(index)

for i in range(h):
    row=''
    for j in i_list:
        row = row + c[i][j*l:(j+1)*l]
    print(row)
