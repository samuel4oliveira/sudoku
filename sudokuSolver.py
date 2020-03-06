PATH = "sudoku.txt"
file = open(PATH).read()

sudoku = [[int(char) for char in file[i:i+9]] for i in range(0,len(file), 9)]

def is_possible(y, x, n):
    global sudoku

    # verificamos se n nao esta na linha ou na coluna especificada
    if n in sudoku[y] or n in [row[x] for row in sudoku]:
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
                    if is_possible(y, x, n):
                        sudoku[y][x] = n
                        solve()
                        sudoku[y][x] = 0
                return
                
    print(sudoku)

solve()