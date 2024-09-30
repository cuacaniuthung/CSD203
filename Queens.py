n = int(input())

free = [[True for i in range(n)] for i in range(n)]
locations = [None for i in range(n)]

def Try(x):
    for y in range(n):
        if free[x][y]:
            locations[x] = y
            # Danh dau phan tu hien tai
            free[x][y] = False

            # Danh dau hang doc
            for i in range(x, n):
                free[i][y] = False
 
            main_dig = x-y
            sub_dig = x+y

            # Danh dau theo duong cheo chinh
            for i in range(x+1, n):
                j = i-main_dig

                if j<n:
                    free[i][j] = False
                else:
                    break
            # Danh dau theo duong cheo PHU
            for i in range(x+1, n):
                j = sub_dig-i

                if j>=0:
                    free[i][j] = False
                else:
                    break

            # Neu la phan tu cuoi thi in ra
            if(x==n-1):
                # for i, j in enumerate(locations):
                #     print(f'({i+1},{j+1})', end=' ')
                # print()
                pass
            else:
                Try(x+1)

            # Xoa cac phan tu duoc danh dau
            free[x][y] = True

            for i in range(x, n):
                free[i][y] = True
 
            main_dig = x-y
            sub_dig = x+y

            for i in range(x+1, n):
                j = i-main_dig

                if j<n:
                    free[i][j] = True
                else:
                    break

            for i in range(x+1, n):
                j = sub_dig-i

                if j>=0:
                    free[i][j] = True
                else:
                    break
def print_chessboard_with_queens(locations):
    n = len(locations)

    for i in range(n):
        for j in range(n):
            if locations[i] == j:
                print('q', end=' ')
            else:
                print('.', end=' ')
        print()
    
Try(0)
print_chessboard_with_queens(locations)