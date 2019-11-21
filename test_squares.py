import unittest

from squares import max_sum


class MyTestCase(unittest.TestCase):
    def test_failure(self):
        answer = max_sum(998, [[67828645, 425092764, 242723908, 669696211, 501122842, 438815206], [625649397, 295060482, 262686951, 815352670], [100876777, 196900030, 523615865]])
        self.assertEqual(answer, 974)


if __name__ == '__main__':
    unittest.main()
