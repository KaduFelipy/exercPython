def fatorial (n, show = False):
    f = 1
    if n == 0 or n == 1:
        f = 1
    for i in range(n,0,-1):
        f *= i
        if show:
            if i > 1:
                print(f'{i}x', end = ' ')
            else:
                print(f'{i}=', end = ' ')
    return f

print(fatorial(5))
