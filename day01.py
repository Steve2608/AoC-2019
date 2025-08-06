from aoc_util import Timing, get_data


def parse_data(content: str) -> list[int]:
    return list(map(int, content.splitlines()))


def part1(data: list[int]) -> int:
    def fuel_for_mass(mass: int) -> int:
        return mass // 3 - 2

    return sum(map(fuel_for_mass, data))


def part2(data: list[int]) -> int:
    def fuel_for_mass(mass: int) -> int:
        if (fuel := mass // 3 - 2) <= 0:
            return 0
        return fuel + fuel_for_mass(fuel)

    return sum(map(fuel_for_mass, data))


if __name__ == "__main__":
    with Timing():
        content: str = get_data("inputs/day01.txt")
        data: list[int] = parse_data(content)

        print(f"part1: {part1(data)}")
        print(f"part2: {part2(data)}")
