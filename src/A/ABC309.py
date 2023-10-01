def resolve():
    tail=[
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]
    A,B=map(int,input().split())
    check="False"
    for i in range (3):
        # print(tail[i][0])
        if tail[i][0]==A and tail[i][1]==B:
            check="True"

        elif tail[i][1]==A and tail[i][2]==B:
            check="True"
    print("Yes") if check=="True" else print("No")
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
        input = """7 8"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 9"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 4"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
