import time
import sys

maze = [
    [1,1,0,1,1,1,0,1],
    [1,0,0,1,0,1,0,1],
    [1,1,1,1,0,1,1,1],
    [0,0,0,1,0,0,0,1],
    [1,1,1,1,1,1,0,1],
    [1,0,1,0,0,0,0,1],
    [1,1,1,1,0,1,1,1],
    [0,0,0,1,0,0,0,1]
]

N = len(maze)
path = [[0]*N for _ in range(N)]
backtrack = 0


def print_maze(x, y, info=""):
    sys.stdout.write("\033[H")

    print("RAT IN A MAZE (BACKTRACKING)\n")
    print(info)

    print("🧱" * (N + 2))
    for i in range(N):
        print("🧱", end="")
        for j in range(N):
            if i == x and j == y:
                print("🐭", end="")
            elif i == N-1 and j == N-1:
                print("🧀", end="")
            elif maze[i][j] == 0:
                print("🟥", end="")
            elif path[i][j] == 1:
                print("🟩", end="")
            elif path[i][j] == 2:
                print("⬜", end="")
            else:
                print("  ", end="")
        print("🧱")
    print("🧱" * (N + 2))

    print(f"\n📊 Backtracking: {backtrack}")
    time.sleep(0.2)


def solve(x, y):
    global backtrack

    # batas & validasi
    if not (0 <= x < N and 0 <= y < N):
        return False
    if maze[x][y] == 0 or path[x][y] != 0:
        return False

    # tandai jalan
    path[x][y] = 1
    print_maze(x, y, f"🐭 Jalan ke ({x},{y})")

    # tujuan
    if x == N-1 and y == N-1:
        print_maze(x, y, "🎉 Sampai tujuan!")
        return True

    # coba arah
    if solve(x, y+1): return True  # kanan
    if solve(x+1, y): return True  # bawah
    if solve(x-1, y): return True  # atas
    if solve(x, y-1): return True  # kiri

    # backtracking
    path[x][y] = 2
    backtrack += 1
    print_maze(x, y, f"❌ Buntu di ({x},{y}) → Mundur")

    return False


if __name__ == "__main__":
    print("\033[2J")
    solve(0, 0)
    print("\nSelesai!")
