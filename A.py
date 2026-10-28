BUT = [[1, 2, 3],
       [8, 0, 4],
       [7, 6, 5]]

#dictionary of the positions of the numbers in the goal state
POS = {}
for a in range(3):
    for b in range(3):
        POS[BUT[a][b]] = (a, b)


def h(M):
    total = 0
    for i in range(3):
        for j in range(3):
            a, b = POS[M[i][j]]
            total += abs(i - a) + abs(j - b)
    return total

def inversions(M):
    t = [x for ligne in M for x in ligne if x != 0]
    n = 0
    for i in range(len(t)):
        for j in range(i + 1, len(t)):
            if t[i] > t[j]:
                n += 1
    return n
 
 
def resoluble(M):
    return inversions(M) % 2 == inversions(BUT) % 2 # la meme pariti que le but 

def astar(A):
    if A == BUT:
        return 0, 0                         # g, f
    if not resoluble(A):
        return None                         # can't be resolved                
 # initialize 
    Open = [(h(A), 0, A)]                   # records: (f, g, matrix)
    Closed = []
    etape = 0                               

    while Open:
        Open.sort(key=lambda x: x[0])                       #  smallest f first
        f, g, S = Open.pop(0)# take Open[0] and remove it
    
      
        etape += 1
        print("Step", etape, "  g =", g, "  h =", h(S), "  f =", f)

        for ligne in S:
            print(*ligne)
          
        if S == BUT:                        
            return g, f                     

        Closed.append(S)

        # find the  index of 0
        for i in range(3):
            for j in range(3):
                if S[i][j] == 0:
                    zi, zj = i, j

        # 4 moves: left, right, up, down
        for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            ni, nj = zi + di, zj + dj
            if 0 <= ni < 3 and 0 <= nj < 3:            
                N = [ligne[:] for ligne in S]           # copy
                N[zi][zj], N[ni][nj] = N[ni][nj], N[zi][zj]   # swap
                if N not in Closed and all(item[2] != N for item in Open): #not in closed and not in open
                    Open.append((g + 1 + h(N), g + 1, N))     # insert (f, g, N)

    return None