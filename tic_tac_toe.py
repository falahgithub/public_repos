# tic-tac-toe

import numpy as np

from prettytable.colortable import ColorTable, Themes


x = ColorTable(theme=Themes.OCEAN)

board = [["", "", ""],["", "", ""],["", "", ""]]

# Initializing board

x.field_names= ["Tic", "Tac", "Toe"]
x.add_rows(board)
print(x)

def boardchange(r, c, code= "p2"):
    if code == "p1":
        board[r][c] = "X"
        x.clear_rows()
        x.add_rows(board)
        print(x)
    else:
        board[r][c] = "O"
        x.clear_rows()
        x.add_rows(board)
        print(x)



r = int()
c = int()
arr = np.zeros(shape=(3,3))


def checkresult(r, c, code):
    global arr

    boardchange(r, c, code)
    if code=="p1":
        arr[r][c] = 1
    else:
        arr[r][c] = -1
    colsum = np.sum(arr, axis=0)
    rowsum = np.sum(arr, axis=1)
    diagsum = np.trace(arr)
    antidiagsum = np.trace(np.fliplr(arr))

    if 3 in colsum or 3 in rowsum or diagsum==3 or antidiagsum==3:
        win = True
        print("Player X won")
        return win
    elif -3 in colsum or -3 in rowsum or diagsum==-3 or antidiagsum==-3:
        win = True
        print("Player O won")
        return win
    return False

allowed_rc = [[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]

def is_val_allow(r,c):
    global allowed_rc
    if [r,c] in allowed_rc:
        allowed_rc.remove([r,c])
        return True


def mm():
    winner = False
    cond = True
    condB = True

    while (cond == True) and (len(allowed_rc)!= 0) and not winner:

        code = "p1"
        try:
            r = int(input("player X : row no.")) - 1
            c = int(input("player X : col no.")) - 1

        except:
            print("Pressed Wrong Key.")
            continue

        else:
            if is_val_allow(r,c):
                winner = checkresult(r,c,code)
            else:
                if len(allowed_rc) == 0:
                    print("All positions are filled. GAME OVER - NOBODY WINS")
                    continue
                else:
                    print("You've entered wrong row and col numbers combination.")
                    continue

            condB = True
            while condB == True and (len(allowed_rc)!= 0) and not winner:
                code = "p2"
                try:
                    r = int(input("player O: row no.")) - 1
                    c = int(input("player O : col no.")) - 1
                except:
                    print("Pressed Wrong Key.")
                    continue
                else:
                    if is_val_allow(r, c):
                        winner = checkresult(r, c, code)
                        condB = False

                    else:
                        if len(allowed_rc) == 0:
                            print("All positions are filled. GAME OVER - NOBODY WINS")
                            continue
                        else:
                            print("You've entered wrong row and col numbers combination.")
                            continue


# Running the app
mm()
