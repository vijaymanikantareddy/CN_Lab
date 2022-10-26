# IMPLEMENTATION OF DISTANCE VECTOR:
INFINITY = 10000
length = [[0 for _ in range(10)] for _ in range(10)]
path = [[0 for _ in range(10)] for _ in range(10)]
se = [0] * 10
adj = []
s = c = 0
n = int(input("Enter No of Routers: "))
print("Enter Adjacency Matrix")
for i in range(n):
    adj.append(list(map(int, input().split())))
# Initialization Part
for i in range(n):
    for j in range(n):
        if adj[i][j] == 0 and i != j:
            length[i][j] = INFINITY
            path[i][j] = 0
        else:
            length[i][j] = adj[i][j]
            path[i][j] = j
        if i == j:
            path[i][j] = 30
# Iteration Part
c = 1
while c:
    c = 0
    for s in range(n):
        for j in range(n):
            if adj[s][j]:
                for i in range(n):
                    if (length[s][j] + length[j][i]) <length[s][i]:
                        length[s][i] = length[s][j] +length[j][i]
                        path[s][i] = j
for s in range(n):
    for i in range(n):
        if length[s][i] == INFINITY:
            c += 1
print("\nRouting table\n\n")
for i in range(65, 65 + n):
    print(" ", chr(i), " ", end=' ')
print("\n--------------------------------------")
for i in range(n):
    print(chr(i + 65), end=' ')
    for s in range(n):
        print(" %3d%3c |" % (length[s][i], path[s][i] + 65),end='')
    print()