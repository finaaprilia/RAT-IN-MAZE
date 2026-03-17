ALGORITMA RAT IN A MAZE (BACKTRACKING)

START
    Input maze (matriks N x N, 1 = jalan, 0 = tembok)
    Inisialisasi path[N][N] dengan nilai 0
    Tentukan START = (0,0) dan END = (N-1, N-1)

FUNCTION Solve(x, y)

    IF (x == N-1 AND y == N-1) THEN
        path[x][y] ← 1
        Tampilkan maze
        RETURN True
    ENDIF

    IF (x, y) berada dalam batas maze
       AND maze[x][y] == 1
       AND path[x][y] == 0 THEN

        path[x][y] ← 1
        Tampilkan maze

        IF Solve(x+1, y) THEN RETURN True   // bawah
        IF Solve(x, y+1) THEN RETURN True   // kanan
        IF Solve(x-1, y) THEN RETURN True   // atas
        IF Solve(x, y-1) THEN RETURN True   // kiri

        path[x][y] ← 0   // backtracking
        Tampilkan maze
    ENDIF

    RETURN False
END FUNCTION

Panggil Solve(0, 0)

IF hasil False THEN
    Tampilkan "Tidak ada jalur ditemukan"
ENDIF

END