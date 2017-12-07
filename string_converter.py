def answer(n):
    count = 0
    x = len(n)
    if x == 0:
        return count
    else:
        for y in range(1,x):
            a = list(map(''.join, zip(*[iter(n)]*y)))
            print(a)
            if len(set(a)) == 1:
                count = len(a)
                print(count,a)
                return count
    return count
answer('abab')
