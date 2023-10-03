def resolve():
    N=int(input())
    S=input()
    check=0
    for i in range (0,N-2):
        if S[i]=='A'and S[i+1]=='B'and S[i+2]=='C':
            check=i+1
            break
    if check==0:
        print(-1)
    else :
        print(check)

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
        input = """8
ABABCABC"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
ACB"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """20
BBAAABBACAACABCBABAB"""
        output = """13"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
