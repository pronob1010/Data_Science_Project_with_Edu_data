n = int(input())
for i in range(n):
    x, k = map(int, input().split())

    print("{} {}".format(k - x % k, x % k))