n = int(input())
v = int(input())
m = int(input())
tree = dict()
parent = []
for i in range(m):
    p, l, r = [int(j) for j in input().split()]
    tree[p] = [l,r]
    parent.append(p)
   
current = parent[0]

tree_path = []
l = "Left"
r = "Right"
previous = []
seen = set()

while current != v:
    if current in parent:
        lchild = tree[current][0]
        rchild = tree[current][1]
        if lchild in seen and rchild in seen:
            seen.add(current)
            current = previous.pop()
            tree_path.pop()
        elif lchild in seen:
            previous.append(current)
            current = rchild
            tree_path.append(r)
        else:
            previous.append(current)
            current = lchild
            tree_path.append(l)
    else:
        seen.add(current)
        current = previous.pop()
        tree_path.pop()
        
if len(tree_path) == 0:
    print("Root")
else:
    print(' '.join(i for i in tree_path))
