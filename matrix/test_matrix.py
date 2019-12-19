import unittest
from matrix import matrix


class MyTestCase(unittest.TestCase):
    def test_input(self):
        with open("input00.txt") as file:
            N, M = [int(i) for i in file.readline().split()]
            r = [next(file).rstrip("\n") for _ in range(N)]
            answer = matrix(M, N, r)
        with open("output00.txt") as file:
            correct = file.read()
        self.assertEqual(answer, correct)


if __name__ == '__main__':
    unittest.main()
