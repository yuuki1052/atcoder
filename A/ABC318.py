def resolve():
    n,m,p=map(int,input().split())
    count=(n-m)//p+1
    print(count)
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
        input = """13 3 5"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 6 6"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """200000 314 318"""
        output = """628"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
