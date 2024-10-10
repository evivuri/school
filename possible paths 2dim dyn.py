def paths(n, m, x, y):
    dp = [[0] * m for _ in range(n)]


    for i in range(y):
        for j in range(x):
            if i == 0 and j == 0:
                dp[i][j] = 0
            elif i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]


    fin = [[0] * (m - x + 1) for _ in range(n - y + 1)]


    for i in range(n - y + 1):
        for j in range(m - x + 1):
            if i == 0 and j == 0:
                fin[i][j] = 0
            elif i == 0 or j == 0:
                fin[i][j] = 1
            else:
                fin[i][j] = fin[i - 1][j] + fin[i][j - 1]



    print(dp[y - 1][x - 1] * fin[-1][-1])


n, m = map(int, input().split())
y, x = map(int,input().split())
paths(n, m, x, y)