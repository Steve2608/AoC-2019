from collections import defaultdict, deque

from aoc_util import Timing, get_data

Orbit = tuple[str, str]


def parse_data(content: str) -> list[Orbit]:
    return [tuple(line.split(")")) for line in content.strip().splitlines()]


def part1(data: list[Orbit]) -> int:
    def count_orbits(center: str) -> int:
        shortest_paths = {center: 0}

        queue = deque([center])
        while queue:
            planet = queue.popleft()
            for satellite in system[planet]:
                shortest_paths[satellite] = shortest_paths[planet] + 1
                queue.append(satellite)

        return sum(shortest_paths.values())

    system = defaultdict(list)
    for center, satellite in data:
        system[center].append(satellite)

    return count_orbits("COM")


def part2(data: list[Orbit]) -> int:
    def path_to_center(planet: str) -> set[str]:
        path = set()
        while planet in system:
            planet = system[planet]
            path.add(planet)
        return path

    system = {}
    for center, satellite in data:
        system[satellite] = center

    you = path_to_center("YOU")
    santa = path_to_center("SAN")

    return len(you.symmetric_difference(santa))


if __name__ == "__main__":
    with Timing():
        content: str = get_data("inputs/day06.txt")
        data: list[Orbit] = parse_data(content)

        print(f"part1: {part1(data)}")
        print(f"part2: {part2(data)}")
