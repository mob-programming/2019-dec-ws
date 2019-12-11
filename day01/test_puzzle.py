from unittest import TestCase

from day01.puzzle import Puzzle


class TestPuzzle(TestCase):

    def test_calculate_fuel_requirement_for_module(self):
        self.assertEqual(2, Puzzle.calculate_fuel(12))
        self.assertEqual(2, Puzzle.calculate_fuel(14))
        self.assertEqual(654, Puzzle.calculate_fuel(1969))
        self.assertEqual(33583, Puzzle.calculate_fuel(100756))

    def test_sum_of_fuel(self):
        self.assertEqual(34241, Puzzle.calculate_total_fuel([12, 14, 1969, 100756]))
        self.assertEqual(414, Puzzle.calculate_total_fuel([12, 1244]))

# For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
# For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
# For a mass of 1969, the fuel required is 654.
# For a mass of 100756, the fuel required is 33583.