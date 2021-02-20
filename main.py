
def doesCircleExist(paths):
    arr = []

    for i in range(paths):
        if(isCyclic(paths[i]) == True):
            arr.append('Y')
        else:
            arr.append('N')
    return arr


def isCyclic(path):
    res = False

    N = 0
    E = 1
    S = 2
    W = 3

    # start point
    x = 0
    y = 0
    dir = N

    # Traverse path
    for i in range(len(path)):

        # Find current move
        move = path[i]

        # Update current direction
        if move == 'R':
            dir = (dir + 1) % 4
        elif move == 'L':
            dir = (4 + dir - 1) % 4

        # If move is Go, then change x or y according to
        # current direction
        else:  # if move == 'G'
            if dir == N:
                y += 1
            elif dir == E:
                x += 1
            elif dir == S:
                y -= 1
            else:
                x -= 1

    # if return to original start point must be cyclic
    if x== 0 and y== 0:
        res = True

    return res

