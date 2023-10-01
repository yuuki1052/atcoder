# TLE

def resolve():
    N,M=map(int,input().split())
    A=list(map(int,input().split()))
    for i in range(1,N+1):
        if min(A)-i==0:
            print("0")
            A.pop(0)
        else :
            print(min(A)-i)

        
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
        input = """3 2
2 3"""
        output = """1
0
0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8 5
1 3 4 7 8"""
        output = """0
1
0
0
2
1
0
0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
