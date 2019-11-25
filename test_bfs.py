import unittest
from bfs import Graph


class MyTestCase(unittest.TestCase):
    def test_simple(self):
        g = Graph(3)
        self.assertEqual(g.find_all_distances(0), [-1, -1])
        g.connect(0, 1)
        self.assertEqual(g.find_all_distances(1), [6, -1])

    def test_failing(self):
        g = Graph(4)
        g.connect(3, 1)
        g.connect(0, 1)
        g.connect(0, 2)
        self.assertEqual(g.find_all_distances(0), [6, 6, 12])


if __name__ == '__main__':
    unittest.main()
