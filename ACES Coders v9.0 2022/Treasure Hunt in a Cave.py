MAX_VAL = 2*10**6

[ROWS, COLS] = list(map(int, input().split()))

ROWS+=2
COLS+=2

x = [[1]*COLS for _ in range(ROWS)]

for i in range(ROWS-2):
    dat = list(map(int, input().split()))
    for j in range(COLS-2):
        x[i+1][j+1] = dat[j]
        
STOP = list(map(int, input().split()))
        
for r in range(ROWS):
    for c in range(COLS):
        x[r][c] = -100 if x[r][c]==1 else MAX_VAL

que = []

x[STOP[0]][STOP[1]] = 0
que.append(STOP)

while len(que) > 0:
    curr = que.pop(0)
    r = curr[0]
    c = curr[1]

    if x[r-1][c] == MAX_VAL:
        x[r-1][c] = x[r][c]+1
        que.append((r-1,c))
    
    if x[r+1][c] == MAX_VAL:
        x[r+1][c] = x[r][c]+1
        que.append((r+1,c))

    if x[r][c-1] == MAX_VAL:
        x[r][c-1] = x[r][c]+1
        que.append((r,c-1))

    if x[r][c+1] == MAX_VAL:
        x[r][c+1] = x[r][c]+1
        que.append((r,c+1))
    
N = int(input())

explorers = []

for _ in range(N):
    explorers.append(tuple(map(int, input().split())))

for explorer in explorers:
    r = explorer[0]
    c = explorer[1]
    
    if x[r][c]==MAX_VAL:
        print("IMPOSSIBLE")
        continue

    sol = ""
    
    while x[r][c]!=0:
        
        if x[r][c+1]==x[r][c]-1:
            c = c+1
            sol += "E"
            continue
            
        if x[r-1][c]==x[r][c]-1:
            r = r-1
            sol += "N"
            continue
            
        if x[r+1][c]==x[r][c]-1:
            r = r+1
            sol += "S"
            continue
            
        if x[r][c-1]==x[r][c]-1:
            c = c-1
            sol += "W"
            continue
            
    print(sol)
    