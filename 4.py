n = int(input())
s = [int(input()) for _ in range(n)]
minL = [0]
maxL = [0]
ans = [0]
for i in range(1, n):
    if s[i] < s[minL[-1]]:
        minL.append(i)
    else:
        minL.append(minL[-1])

for i in range(1, n):
    if s[i] > s[maxL[-1]]:
        maxL.append(i)
    else:
        maxL.append(maxL[-1])

for i in range(1, n - 1):
    if s[minL[i - 1]] < s[i] < s[maxL[i + 1]]:
        ans = [minL[i - 1] + 1, i + 1, maxL[i + 1] + 1]
        
print(*ans)