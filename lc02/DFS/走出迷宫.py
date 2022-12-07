def dfs(i, j, arr, is_visited):
    global flag
    is_visited[i][j] = 1
    if arr[i][j] == 'E':
        flag = 1
    for x, y in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
        if 0 <= x < n and 0 <= y < m and arr[x][y] != '#' and is_visited[x][y] == 0:
            dfs(x, y, arr, is_visited)

while True:
    try:
        flag = 0
        n, m = map(int, input().split())
        Arr = []
        is_visited = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            Arr.append(list(input()))
        for i in range(n):
            for j in range(m):
                if Arr[i][j] == 'S':
                    dfs(i, j, Arr, is_visited)
        if flag == 1:
            print("Yes")
        else:
            print("No")
    except:
        break
