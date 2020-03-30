"""Main solve
n = int(input())

for i in range(n):
    cn = input().split()
    o = 1
    e = 0
    if(cn[0] == 'odd'):
        for j in range(int(cn[1])):
            print(o)
            o+=2

    else:
        for j in range(int(cn[1])):
            print(e)
            e+=2
"""
class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


def print_from_stream(n, stream= None):
    if stream is None:
        stream = EvenStream()
    for i in range(n):
        print(stream.get_next())

queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n,EvenStream())
    else:
        print_from_stream(n, OddStream())
