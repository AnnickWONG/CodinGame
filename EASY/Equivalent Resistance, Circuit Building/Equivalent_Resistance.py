n = int(input())

R_tbl = dict()  # Create a dictionary to store the resitor

for i in range(n):
    name, r = input().split()
    R_tbl[name] = int(r)

circuit = input().split(" ")

list = []
for c in circuit:
  if c == ')':
    i = list.index('(')
    r = sum(R_tbl[x] for x in list[0:i])
    del list[0:i+1]
    R_tbl[r]=r
    list.insert(0,r)
  elif c == ']':
    i = list.index('[')
    r = 1/sum(1/R_tbl[x] for x in list[0:i])
    del list[0:i+1]
    R_tbl[r]=r
    list.insert(0,r)
  else:
    list.insert(0,c)

print("%.1f" % list[0])
