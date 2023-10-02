def resolve():
            N=int(input())
            if N%5>=3:
                print((N//5+1)*5)
            else:
                print((N//5)*5)
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
        input = """53"""
        output = """55"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """21"""
        output = """20"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100"""
        output = """100"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
