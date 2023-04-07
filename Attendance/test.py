from whiteboard import solution
from unittest import TestCase


class TestAttendance(TestCase):

    def test_eligible_student(self):
        self.assertTrue(solution("PPALLP"))

    def test_ineligible_student(self):
        self.assertFalse(solution("PPALLL"))

    def test_present_student(self):
        self.assertTrue(solution("PPPP"))

    def test_single_day_absent(self):
        self.assertTrue(solution("PPALL"))

    def test_two_days_absent(self):
        self.assertFalse(solution("PPAAL"))

    def test_two_days_absent_one_late(self):
        self.assertFalse(solution("PPAALL"))

    def test_three_days_late(self):
        self.assertFalse(solution("LLLPP"))
