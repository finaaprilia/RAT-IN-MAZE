maze = [...]
path = matriks kosong
backtrack = 0

def solve(x, y):

    if x di luar batas atau y di luar batas:
        return False

    if maze[x][y] == tembok atau path[x][y] sudah dikunjungi:
        return False

    path[x][y] = 1
    tampilkan_maze()

    if (x, y) == tujuan:
        return True

    if solve(x, y+1):
        return True

    if solve(x+1, y):
        return True

    if solve(x-1, y):
        return True

    if solve(x, y-1):
        return True

    path[x][y] = 2
    backtrack += 1
    tampilkan_maze()

    return False

solve(0, 0)
