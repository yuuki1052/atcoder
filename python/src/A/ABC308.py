def resolve():
    S=list(map(int,input().split()))
    check_S=sorted(S)
    check="True"
    check_num=0
    for i in range (len(S)):
        if check_num<=S[i] and 100<=S[i]<=675 and S[i]%25==0:
            check_num=S[i]
            
        else:
            check="False"
    if check=="True":
        print("Yes")
    else:
        print("No")
        
        
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
        input = """125 175 250 300 400 525 600 650"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100 250 300 400 325 575 625 675"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """0 23 24 145 301 413 631 632"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
