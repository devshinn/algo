
w, m, k = map(int, input().split())
answer = 0
while ((w >= 2) & (m >= 1)):
    w -= 2
    m -= 1
    if (w + m >= k):
        answer += 1
    else:
        print(answer)
print(answer)


# print(min((w+m-k)//3, w//2, m))

