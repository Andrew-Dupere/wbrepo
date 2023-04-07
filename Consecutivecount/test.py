import unittest
from whiteboard import solution
from unittest import TestCase


class TestPairZeros(TestCase):

    def test_solution1(self):
        assert solution([0, 1, 0, 2]) == [0, 1, 2]

    def test_solution2(self):
        assert solution([0, 1, 0, 0]) == [0, 1, 0]

    def test_solution3(self):
        assert solution([1, 0, 1, 0, 2, 0, 0, 3, 0]) == [1, 0, 1, 2, 0, 3, 0]

    def test_solution4(self):
        assert solution([1, 0, 1, 0, 2, 0, 0, 3, 0]) == [1, 0, 1, 2, 0, 3, 0]

    def test_solution6(self):
        assert solution([1, 2, 3]) == [1, 2, 3]
