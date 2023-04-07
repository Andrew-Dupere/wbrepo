from whiteboard import solution
from unittest import TestCase


class TestHillsAndValleys(TestCase):
    def test_one_valley(self):
        steps = 8
        path = "DDUUUUDD"
        self.assertEqual(solution(steps, path), 1)

    def test_two_valleys(self):
        steps = 12
        path = "UDDDUDUUDDUU"
        self.assertEqual(solution(steps, path), 2)

    def test_no_valleys(self):
        steps = 10
        path = "UUDDUUDDUU"
        self.assertEqual(solution(steps, path), 0)