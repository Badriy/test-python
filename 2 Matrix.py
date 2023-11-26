matrix1 = [[0,5,1],
          [4,9,0],
          [0,6,0]] 

matrix2 = [[5,5,1],
          [5,8,1],
          [9,2,6]]

def add_matrix(mtx1,mtx2):
    new_matrix = []
    for row in range(len(mtx1)):
        rows = []
        for cln in range(len(mtx2)):
            rows.append(mtx1[row][cln] + mtx2[row][cln])
        new_matrix.append(rows)
    print(new_matrix)
add_matrix(matrix1,matrix2)                         