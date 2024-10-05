def solution(m, n, puddles):
    paths = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if (i, j) == (0,0):
                paths[i][j] = 1
            elif [j+1, i+1] in puddles:
                paths[i][j] = 0
            else:
                paths[i][j] = paths[i-1][j] + paths[i][j-1]

    return paths[n-1][m-1] % 1000000007