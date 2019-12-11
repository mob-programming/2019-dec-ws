import math


class Puzzle:

    @staticmethod
    def calculate_fuel(mass: int) -> int:
        return math.floor(mass / 3) - 2

    @staticmethod
    def calculate_total_fuel(masses: list) -> int:
        return sum([Puzzle.calculate_fuel(mass) for mass in masses])
