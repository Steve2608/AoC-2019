import itertools as it
import math
import re

from aoc_util import Timing, get_data

Position = tuple[int, int, int]


def parse_data(content: str) -> list[Position]:
    return [tuple(map(int, re.findall(r"-?\d+", line))) for line in content.splitlines()]


def sign(x: int) -> int:
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0


def part1(data: list[Position], epochs: int = 1000) -> int:
    moons, vels = data.copy(), [[0] * len(data[0]) for _ in range(len(data))]
    for _ in range(epochs):
        for i, moon in enumerate(moons):
            for j, other in enumerate(moons):
                if i != j:
                    for dim in range(len(moon)):
                        vels[i][dim] = vels[i][dim] + sign(other[dim] - moon[dim])

        for i, (moon, vel) in enumerate(zip(moons, vels)):
            moons[i] = tuple(moon[i] + vel[i] for i in range(len(moon)))

    return sum(sum(map(abs, moon)) * sum(map(abs, vel)) for moon, vel in zip(moons, vels))


def part2(data: list[Position]) -> int:
    def axis_period(pos: list[int]) -> int:
        p0, v0, vel = pos.copy(), [0] * len(pos), [0] * len(pos)
        for epoch in it.count(1):
            for i, pos_i in enumerate(pos):
                for j, pos_j in enumerate(pos):
                    if i != j:
                        vel[i] += sign(pos_j - pos_i)

            for i, v_i in enumerate(vel):
                pos[i] += v_i

            if pos == p0 and vel == v0:
                return epoch

    return math.lcm(*(axis_period([moon[i] for moon in data]) for i in range(len(data[0]))))


if __name__ == "__main__":
    with Timing():
        content: str = get_data("inputs/day12.txt")
        data: list[Position] = parse_data(content)

        print(f"part1: {part1(data)}")
        print(f"part2: {part2(data)}")
