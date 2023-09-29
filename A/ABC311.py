def resolve():
    N=int(input())
    S=input()
    print(max(S.find("A"),S.find("B"),S.find("C"))+1)

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
        input = """5
ACABB"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
CABC"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """30
AABABBBABABBABABCABACAABCBACCA"""
        output = """17"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
