## P1
carte = [ ]
for ligne in open('input.txt','r').read().splitlines():
    current_line = []
    for char in ligne:
        current_line.append(char)
    carte.append(current_line)

n = len(carte)
m = len(carte[0])

departs = []
for i in range(n):
    for j in range(m):
        if carte[i][j] == '0':
            departs.append((i,j))


def voisins(coord):
    i,j = coord
    pot = [ (i-1,j), (i+1,j), (i,j-1), (i,j+1)    ]
    return [ (x,y) for (x,y) in pot if x>=0 and y>=0 and x<n and y<m and int(carte[x][y]) ==  int(carte[i][j]) + 1  ]

# Parcours en largeur avec calcul de distance
def distlarg(root):
    vus = {root}
    dist = { }
    file = [root]
    dist[root] = 0

    while len(file)>0:
        cour = file.pop(0)  # on défile (à gauche, donc)
        for s in voisins(cour):  # pour tous les voisins de cour (le défilé)
            if s not in vus:
                vus.add(s)
                file.append(s)  #on l'a vu et on l'enfile
                dist[s]=dist[cour]+1

    return dist

P1 = 0
for root in departs:
    d = distlarg(root)
    for x in d.values():
        if x == 9:
            P1 += 1
print('Part 1 :', P1)

## P2
def DFS(start, end, vus, path):
    if start == end:
        yield path

    for v in voisins(start):
        if v not in vus:
            vus2 = vus.copy()
            vus2.add(v)
            yield from DFS(v, end, vus2, path + [v])

N = 0
for root in departs:
    d = distlarg(root)
    for target,dist in d.items():
        if dist == 9:
            N += len(list(DFS(root,target,{root},[root])))

print('Part 2 :', N)

