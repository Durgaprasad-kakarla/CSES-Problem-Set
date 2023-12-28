def solve():
    n = int(input())
    a = []
    b = []
    p = []

    for _ in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)

    a.sort()
    b.sort()

    mx = 0
    c = 0
    x = 0
    y = 0

    while x < n:
        if a[x] < b[y]:
            c += 1
            x += 1
        else:
            c -= 1
            y += 1
        mx = max(mx, c)

    print(mx)


solve()
''' Time Complexity--O(nlogn)
    Space Complexity--O(n)'''