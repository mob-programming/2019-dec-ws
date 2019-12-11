import math


class Puzzle:
    masses = list()

    @staticmethod
    def calculate_fuel(mass: int) -> int:
        return math.floor(mass / 3) - 2

    @staticmethod
    def calculate_total_fuel(masses: list) -> int:
        return sum([Puzzle.calculate_fuel(mass) for mass in masses])

    @staticmethod
    def read_file() -> int:
        with open('./input_data.txt') as file:
            return Puzzle.calculate_total_fuel(list(map(lambda x: int(x.split('\n')[0]), file)))
