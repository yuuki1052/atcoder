def resolve():
    N,M=map(int,input().split())
    S=input()
    T=input()
    S_check=T.find(S)
    S_rcheck=T.rfind(S)
    if S_check==-1:
        print("3")
    elif S_check==0:
        if S_rcheck+len(S)==len(T):
            print("0")
        else :
            print("1")
    elif S_rcheck+len(S)==len(T):
        print("2")
    else:
        print("3")

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
        input = """3 7
abc
abcdefg"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 4
abc
aabc"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 3
abc
xyz"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """3 3
aaa
aaa"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
