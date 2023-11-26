matrix = [[0,5,1],
          [4,9,0],
          [0,6,0]]
"print(matrix[1][1])"
print()

count = 0
for i in range(len(matrix)):
    for j in range(len(matrix)):
        "print(matrix[i][j] * 2 , end=" ")"
        if matrix[i][j] == 0 :
           count+= 1
        
print(count)

