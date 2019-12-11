import math


class Puzzle:

    @staticmethod
    def calculate_fuel(mass: int) -> int:
        return math.floor(mass / 3) - 2
