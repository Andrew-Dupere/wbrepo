import unittest
from whiteboard import solution
from unittest import TestCase


class TestConsecutiveOnes(TestCase):

    def test_all_zeros(self):
        nums = [0, 0, 0, 0]
        self.assertEqual(solution(nums), 0)

    def test_all_ones(self):
        nums = [1, 1, 1, 1, 1]
        self.assertEqual(solution(nums), 5)

    def test_single_one(self):
        nums = [0, 0, 0, 1, 0]
        self.assertEqual(solution(nums), 1)


    def test_alternating_zeros_ones(self):
        nums = [0, 1, 0, 1, 0, 1, 0]
        self.assertEqual(solution(nums), 1)
