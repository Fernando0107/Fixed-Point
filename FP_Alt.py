def fixed_point(a):
    l=0
    u = 0, len(a)

    while l <= u:
        m = (l + u) // 2
        if m == a[m]:
            return m
        elif m > a[m]:
            l = m + 1
        else:
            u = m - 1

    return -1


print(fixed_point([-10, -5, -2, 2, 3, 5, 7, 10, 15, 25, 35, 78, 129]))
