tc = int(input())

def ggt(a, b):
    if b == 0:
        return a
    return ggt(b, a % b)

for t in range(1, tc + 1):
    n, l = map(int, input().split())
    ls = list(map(int, input().split()))

    orig = [-1] * (l + 1)
    for i in range(l - 1):
        if ls[i] != ls[i + 1]:
            orig[i + 1] = ggt(ls[i], ls[i + 1])
            a = i
            while a >= 0:
                orig[a] = ls[a] // orig[a + 1]
                a -= 1
            a = i + 2
            while a < len(orig):
                orig[a] = ls[a - 1] // orig[a - 1]
                a += 1
            break

    primes = sorted(list(set(orig)))
    res = ""
    for num in orig:
        o = primes.index(num)
        res += chr(ord('A') + o)
    print("Case #%d: %s" % (t, res))