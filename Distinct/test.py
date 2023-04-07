import unittest
from whiteboard import solution
from unittest import TestCase


class TestDuplicates(TestCase):

    def test_no_duplicates(self):
        self.assertEqual(solution("abcde"), 0)

    def test_one_duplicate(self):
        self.assertEqual(solution("indivisibility"), 1)

    def test_multiple_duplicates1(self):
        self.assertEqual(solution("aabbcde"), 2)
    
    def test_multiple_duplicates2(self):
        self.assertEqual(solution("aabBcde"), 2)

    def test_multiple_duplicates3(self):
        self.assertEqual(solution("aA11"), 2)

    def test_multiple_duplicates4(self):
        self.assertEqual(solution("ABBA"), 2)
