path = "/home/samuel/Documents/ufmt/sudoku/sudoku.txt"
arquivo = open(path).read()

aux = []
sudoku = []
for i in range(0, len(arquivo)):
    aux.append(int(arquivo[i]))
    if len(aux) == 9:
        sudoku.append(aux)
        aux = []

def possible(y, x, n):
    global sudoku
    for i in range(0, 9):
        if sudoku[y][i] == n:
            return False
    for i in range(0, 9):
        if sudoku[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku[y0+i][x0+j] == n:
                return False
    return True

def solve():
    global sudoku
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        sudoku[y][x] = n
                        solve()
                        sudoku[y][x] = 0
                return     
    print(sudoku)

solve()