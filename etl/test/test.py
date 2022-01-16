import unittest

from app.calculations import _calculate_mean_break_length_in_minutes, _calculate_mean_shift_cost, \
    _calculate_max_allowance_cost_14d, _calculate_max_break_free_shift_period_in_days, \
    _calculate_min_shift_length_in_hours, _calculate_total_number_of_paid_breaks
from test.data import CASE1, CASE2, CASE3, CASE4, CASE5


class TestCalculationMethods(unittest.TestCase):


    def setUp(self) -> None:
        self.case1 = CASE1
        self.case2 = CASE2
        self.case3 = CASE3
        self.case4 = CASE4
        self.case5 = CASE5


    def test_case1(self):
        self.assertEqual(_calculate_mean_break_length_in_minutes(self.case1.results), (1609502400000 / 1000 / 60 - 1609498800000 / 1000 / 60))
        self.assertEqual(_calculate_mean_shift_cost(self.case1.results), 12)
        self.assertEqual(_calculate_max_allowance_cost_14d(self.case1.results), 0)
        self.assertEqual(_calculate_max_break_free_shift_period_in_days(self.case1.results), 0)
        self.assertEqual(_calculate_min_shift_length_in_hours(self.case1.results), 1609527600000 / 1000 / 60 / 60 - 1609484400000 / 1000 / 60 / 60)
        self.assertEqual(_calculate_total_number_of_paid_breaks(self.case1.results), 0)


    def test_case2(self):
        self.assertEqual(_calculate_mean_break_length_in_minutes(self.case2.results), (((1609502490000 - 1609498810000) + (1609502450000 - 1609498830000) + (1609502480000 - 1609498890000)) / 3 + 1609502400000 - 1609498800000) / 2 / 1000 / 60)
        self.assertEqual(_calculate_mean_shift_cost(self.case2.results), 11.5)
        self.assertEqual(_calculate_max_allowance_cost_14d(self.case2.results), 15.0)
        self.assertEqual(_calculate_max_break_free_shift_period_in_days(self.case2.results), 0)
        self.assertEqual(_calculate_min_shift_length_in_hours(self.case2.results), 1609522000000 / 1000 / 60 / 60 - 1609484200000 / 1000 / 60 / 60)
        self.assertEqual(_calculate_total_number_of_paid_breaks(self.case2.results), 3)


    def test_case3(self):
        self.assertEqual(_calculate_mean_break_length_in_minutes(self.case3.results), 0)
        self.assertEqual(_calculate_mean_shift_cost(self.case3.results), 0)
        self.assertEqual(_calculate_max_allowance_cost_14d(self.case3.results), 0)
        self.assertEqual(_calculate_max_break_free_shift_period_in_days(self.case3.results), 0)
        self.assertEqual(_calculate_min_shift_length_in_hours(self.case3.results), 0)
        self.assertEqual(_calculate_total_number_of_paid_breaks(self.case3.results), 0)


    def test_case4(self):
        self.assertEqual(_calculate_mean_break_length_in_minutes(self.case4.results), 0)
        self.assertEqual(_calculate_mean_shift_cost(self.case4.results), 0)
        self.assertEqual(_calculate_max_allowance_cost_14d(self.case4.results), 0)
        self.assertEqual(_calculate_max_break_free_shift_period_in_days(self.case4.results), 365)
        self.assertEqual(_calculate_min_shift_length_in_hours(self.case4.results), 1609522000000 / 1000 / 60 / 60 - 1609484200000 / 1000 / 60 / 60)
        self.assertEqual(_calculate_total_number_of_paid_breaks(self.case4.results), 0)


    def test_case5(self):
        self.assertEqual(_calculate_mean_break_length_in_minutes(self.case5.results), 0)
        self.assertEqual(_calculate_mean_shift_cost(self.case5.results), 0)
        self.assertEqual(_calculate_max_allowance_cost_14d(self.case5.results), 0)
        self.assertEqual(_calculate_max_break_free_shift_period_in_days(self.case5.results), 418)
        self.assertEqual(_calculate_min_shift_length_in_hours(self.case5.results), 1609522000000 / 1000 / 60 / 60 - 1609484200000 / 1000 / 60 / 60)
        self.assertEqual(_calculate_total_number_of_paid_breaks(self.case5.results), 2)


if __name__ == '__main__':
    unittest.main()
