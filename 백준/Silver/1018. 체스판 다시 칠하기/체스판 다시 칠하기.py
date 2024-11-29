N, M = map(int, input().split())
board = [input() for _ in range(N)]

pattern1 = ["WBWBWBWB", "BWBWBWBW"] * 4
pattern2 = ["BWBWBWBW", "WBWBWBWB"] * 4

def count_paint(x, y, pattern):
    count = 0
    for i in range(8):
        for j in range(8):
            if board[x + i][y + j] != pattern[i][j]:
                count += 1
    return count

min_paint = float('inf')

for i in range(N - 7):
    for j in range(M - 7):
        paint1 = count_paint(i, j, pattern1)
        paint2 = count_paint(i, j, pattern2)
        min_paint = min(min_paint, paint1, paint2)

print(min_paint)