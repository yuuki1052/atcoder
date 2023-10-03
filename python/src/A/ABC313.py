def resolve():
    N=int(input())
    P=list(map(int,input().split()))
    num=P.pop(0)
    if(N==1):
        print(0)
    elif num > max(P):
        print(0)
    else :
        print(max(P)+1-num)

import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """4
5 15 2 10"""
        output = """11"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
15 5 2 10"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
100 100 100"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
