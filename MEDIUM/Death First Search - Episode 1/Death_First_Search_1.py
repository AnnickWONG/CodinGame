def bfs(adj_list, start_node, target_node):
    visited = set()
    Q = list()
    queue = Q.insert(0,start_node)
    visited.add(start_node)
    parent = dict()
    parent[start_node] = None

    while len(Q)!=0:
        current_node = Q[0]
        del Q[0]
        if current_node == target_node:
            break
        for next_node in adj_list[current_node]:
            if next_node not in visited:
                Q.insert(0, next_node)
                parent[next_node] = current_node
                visited.add(next_node)
    path = []
    path.append(target_node)
    while parent[target_node] is not None:
        path.append(parent[target_node])
        target_node = parent[target_node]
    return path

def getBest(adj_list, start_nodes, target_node):
    for s in start_nodes:
        if s in adj_list[target_node]:
            return [s, target_node]
    
    path = []
    for s in start_nodes:
        path.append(bfs(adj_list, s, target_node))
    min_path = min(path)
    n1,n2 = min_path[-2:]
    return [n1,n2]


n, l, e = [int(i) for i in input().split()]
adj_list = {node: [] for node in range(n)}
gate_way = list()
for i in range(l):
    n1, n2 = [int(j) for j in input().split()]
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)
for i in range(e):
    gate_way.append(int(input())) 

# game loop
while True:
    si = int(input()) 

    n1, n2 = getBest(adj_list, gate_way, si)    
    adj_list[n1].remove(n2)
    adj_list[n2].remove(n1)
    for ei in gate_way:
        if len(adj_list[ei]) == 0:
            gate_way.remove(ei)
    print(f"{n1} {n2}")
