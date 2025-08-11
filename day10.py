import itertools as it
import math
from collections import deque

from aoc_util import Timing, get_data

Coordinate = tuple[int, int]
PolarCoordinate = tuple[float, float]


def parse_data(content: str) -> list[Coordinate]:
    return [
        (x, y)
        for y, line in enumerate(content.splitlines())
        for x, point in enumerate(line)
        if point == "#"
    ]


def angle(src: Coordinate, dst: Coordinate) -> float:
    d_x, d_y = dst[0] - src[0], dst[1] - src[1]
    # flipping y direction since we're "growing" downwards
    return math.atan2(-d_y, d_x)


def part1(data: list[Coordinate]):
    return max(
        len(
            set(
                map(
                    lambda other: angle(monitor, other),
                    (other for other in data if other != monitor),
                )
            )
        )
        for monitor in data
    )


def part2(data: list[Coordinate], n: int = 200):
    def polar(dst: Coordinate) -> PolarCoordinate:
        d_x, d_y = dst[0] - monitor[0], dst[1] - monitor[1]

        r = math.hypot(d_x, d_y)
        # flipping y direction since we're "growing" downwards
        theta = (math.pi / 2 - math.atan2(-d_y, d_x)) % (2 * math.pi)

        return r, theta

    if n >= len(data):
        raise ValueError(f"{n=}, is >= to the number of asteroids ({len(data)})")

    monitor = max(
        data,
        key=lambda monitor: len(
            set(
                map(
                    lambda other: angle(monitor, other),
                    (other for other in data if other != monitor),
                )
            )
        ),
    )

    polar_coord = {polar(other): other for other in data if other != monitor}
    groups = {
        k: deque(v)
        for k, v in it.groupby(
            sorted(polar_coord, key=lambda r_theta: (r_theta[1], r_theta[0])),
            key=lambda r_theta: r_theta[1],
        )
    }
    for i, ang in enumerate(it.cycle(groups), 1):
        if distances := groups[ang]:
            curr = distances.popleft()
            if i == n:
                x, y = polar_coord[curr]
                return x * 100 + y


if __name__ == "__main__":
    with Timing():
        content: str = get_data("inputs/day10.txt")
        data: list[Coordinate] = parse_data(content)

        print(f"part1: {part1(data)}")
        print(f"part2: {part2(data)}")
