from unittest import TestCase

from day01.puzzle import Puzzle




class TestPuzzle(TestCase):

    def test_calculate_fuel_requirement_for_module(self):
        puzzle = Puzzle()
        mass = 12
        fuel = 2
        self.assertEqual(fuel, puzzle.calculate_fuel(mass))


# For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
# For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
# For a mass of 1969, the fuel required is 654.
# For a mass of 100756, the fuel required is 33583.