budget = []

n = int(input())
c = int(input())

for i in range(n):
    budget.append( int(input()) )
budget.sort()

if sum(budget) < c:
    print("IMPOSSIBLE")
else:
    for i in range(n):
        avg = int(c / (n-i))
        min_value = min(budget[i], avg)
        c -= min_value
        print(min_value)
