from aoc_util import Timing, get_data

Direction = tuple[str, int]
Coordinate = tuple[int, int]


def parse_data(content: str) -> list[list[Direction]]:
    return [
        list(map(lambda x: (x[0], int(x[1:])), line.split(",")))
        for line in content.splitlines()
    ]


def part1(data: list[list[Direction]]) -> int:
    def manhattan_distance_origin(c: Coordinate) -> int:
        return abs(c[0]) + abs(c[1])

    wires = []
    origin = (0, 0)

    for wire in data:
        coordinates: set[Coordinate] = set()
        x, y = origin
        for direction, steps in wire:
            match direction:
                case "U":
                    coordinates.update(((x, y + offset) for offset in range(steps)))
                    y += steps
                case "D":
                    coordinates.update(((x, y - offset) for offset in range(steps)))
                    y -= steps
                case "L":
                    coordinates.update(((x - offset, y) for offset in range(steps)))
                    x -= steps
                case "R":
                    coordinates.update(((x + offset, y) for offset in range(steps)))
                    x += steps

        wires.append(coordinates)

    wire_a, wire_b = wires
    intersections = wire_a & wire_b
    # ignore origin
    intersections.remove(origin)

    return min(map(manhattan_distance_origin, intersections))


def part2(data: list[list[Direction]]) -> int:
    def shortest_path_length(c: Coordinate) -> int:
        return wire_a[c] + wire_b[c]

    wires = []
    origin = (0, 0)

    for wire in data:
        wire_coordinates: dict[Coordinate, int] = {}
        x, y = origin
        step_count = 0
        for direction, steps in wire:
            match direction:
                case "U":
                    wire_coordinates.update(
                        {(x, y + offset): step_count + offset for offset in range(steps)}
                    )
                    y += steps
                    step_count += steps
                case "D":
                    wire_coordinates.update(
                        {(x, y - offset): step_count + offset for offset in range(steps)}
                    )
                    y -= steps
                    step_count += steps
                case "L":
                    wire_coordinates.update(
                        {(x - offset, y): step_count + offset for offset in range(steps)}
                    )
                    x -= steps
                    step_count += steps
                case "R":
                    wire_coordinates.update(
                        {(x + offset, y): step_count + offset for offset in range(steps)}
                    )
                    x += steps
                    step_count += steps

        wires.append(wire_coordinates)

    wire_a, wire_b = wires
    intersections = wire_a.keys() & wire_b.keys()
    # ignore origin
    intersections.remove(origin)

    return min(map(shortest_path_length, intersections))


if __name__ == "__main__":
    with Timing():
        content: str = get_data("inputs/day03.txt")
        data: list[list[int]] = parse_data(content)

        print(f"part1: {part1(data)}")
        print(f"part2: {part2(data)}")
