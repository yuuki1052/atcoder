def resolve():
    n=int(input())
    print(checknum(n))
def checknum(a):
    a_str=str(abs(a))
    check=0
    b="True"
    if a<10:
        return "Yes"
    for i in range(len(a_str)-1):
        if int(a_str[i])<=int(a_str[i+1]):
            return "No"
    return "Yes"


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
        input = """321"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """123"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """86411"""
        output = """No"""
        self.assertIO(input, output)



if __name__ == "__main__":
    unittest.main()
