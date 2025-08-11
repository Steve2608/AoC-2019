import asyncio
from collections import defaultdict, deque

from aoc_util import Timing, get_data

Coordinate = tuple[int, int]


class Program:
    def __init__(self, data: list[int]):
        self.data = defaultdict(int, enumerate(data))
        self.ip = 0
        self.relative_base = 0

    def parse_instruction(self, instruction: int) -> tuple[int, tuple[int, int, int]]:
        op = instruction % 100
        modes = (instruction // 100 % 10, instruction // 1000 % 10, instruction // 10000 % 10)
        return op, modes

    async def run(self):
        outputs = deque([None, None])
        while (instr := self.data[self.ip]) != 99:
            op, modes = self.parse_instruction(instr)

            match op:
                case 1:
                    match modes[0]:
                        case 0:
                            p1 = self.data[self.data[self.ip + 1]]
                        case 1:
                            p1 = self.data[self.ip + 1]
                        case 2:
                            p1 = self.data[self.relative_base + self.data[self.ip + 1]]
                    match modes[1]:
                        case 0:
                            p2 = self.data[self.data[self.ip + 2]]
                        case 1:
                            p2 = self.data[self.ip + 2]
                        case 2:
                            p2 = self.data[self.relative_base + self.data[self.ip + 2]]
                    match modes[2]:
                        case 0:
                            self.data[self.data[self.ip + 3]] = p1 + p2
                        case 2:
                            self.data[self.relative_base + self.data[self.ip + 3]] = p1 + p2
                    self.ip += 4
                case 2:
                    match modes[0]:
                        case 0:
                            p1 = self.data[self.data[self.ip + 1]]
                        case 1:
                            p1 = self.data[self.ip + 1]
                        case 2:
                            p1 = self.data[self.relative_base + self.data[self.ip + 1]]
                    match modes[1]:
                        case 0:
                            p2 = self.data[self.data[self.ip + 2]]
                        case 1:
                            p2 = self.data[self.ip + 2]
                        case 2:
                            p2 = self.data[self.relative_base + self.data[self.ip + 2]]
                    match modes[2]:
                        case 0:
                            self.data[self.data[self.ip + 3]] = p1 * p2
                        case 2:
                            self.data[self.relative_base + self.data[self.ip + 3]] = p1 * p2
                    self.ip += 4
                case 3:
                    match modes[0]:
                        case 0:
                            self.data[self.data[self.ip + 1]] = (
                                yield outputs.popleft(),
                                outputs.popleft(),
                            )
                        case 2:
                            self.data[self.relative_base + self.data[self.ip + 1]] = (
                                yield outputs.popleft(),
                                outputs.popleft(),
                            )
                    self.ip += 2
                case 4:
                    match modes[0]:
                        case 0:
                            p1 = self.data[self.data[self.ip + 1]]
                        case 1:
                            p1 = self.data[self.ip + 1]
                        case 2:
                            p1 = self.data[self.relative_base + self.data[self.ip + 1]]
                    outputs.append(p1)
                    self.ip += 2
                case 5:
                    match modes[0]:
                        case 0:
                            p1 = self.data[self.data[self.ip + 1]]
                        case 1:
                            p1 = self.data[self.ip + 1]
                        case 2:
                            p1 = self.data[self.relative_base + self.data[self.ip + 1]]
                    match modes[1]:
                        case 0:
                            p2 = self.data[self.data[self.ip + 2]]
                        case 1:
                            p2 = self.data[self.ip + 2]
                        case 2:
                            p2 = self.data[self.relative_base + self.data[self.ip + 2]]
                    if p1 != 0:
                        self.ip = p2
                    else:
                        self.ip += 3
                case 6:
                    match modes[0]:
                        case 0:
                            p1 = self.data[self.data[self.ip + 1]]
                        case 1:
                            p1 = self.data[self.ip + 1]
                        case 2:
                            p1 = self.data[self.relative_base + self.data[self.ip + 1]]
                    match modes[1]:
                        case 0:
                            p2 = self.data[self.data[self.ip + 2]]
                        case 1:
                            p2 = self.data[self.ip + 2]
                        case 2:
                            p2 = self.data[self.relative_base + self.data[self.ip + 2]]
                    if p1 == 0:
                        self.ip = p2
                    else:
                        self.ip += 3
                case 7:
                    match modes[0]:
                        case 0:
                            p1 = self.data[self.data[self.ip + 1]]
                        case 1:
                            p1 = self.data[self.ip + 1]
                        case 2:
                            p1 = self.data[self.relative_base + self.data[self.ip + 1]]
                    match modes[1]:
                        case 0:
                            p2 = self.data[self.data[self.ip + 2]]
                        case 1:
                            p2 = self.data[self.ip + 2]
                        case 2:
                            p2 = self.data[self.relative_base + self.data[self.ip + 2]]
                    match modes[2]:
                        case 0:
                            self.data[self.data[self.ip + 3]] = int(p1 < p2)
                        case 2:
                            self.data[self.relative_base + self.data[self.ip + 3]] = int(p1 < p2)
                    self.ip += 4
                case 8:
                    match modes[0]:
                        case 0:
                            p1 = self.data[self.data[self.ip + 1]]
                        case 1:
                            p1 = self.data[self.ip + 1]
                        case 2:
                            p1 = self.data[self.relative_base + self.data[self.ip + 1]]
                    match modes[1]:
                        case 0:
                            p2 = self.data[self.data[self.ip + 2]]
                        case 1:
                            p2 = self.data[self.ip + 2]
                        case 2:
                            p2 = self.data[self.relative_base + self.data[self.ip + 2]]
                    match modes[2]:
                        case 0:
                            self.data[self.data[self.ip + 3]] = int(p1 == p2)
                        case 2:
                            self.data[self.relative_base + self.data[self.ip + 3]] = int(p1 == p2)
                    self.ip += 4
                case 9:
                    match modes[0]:
                        case 0:
                            p1 = self.data[self.data[self.ip + 1]]
                        case 1:
                            p1 = self.data[self.ip + 1]
                        case 2:
                            p1 = self.data[self.relative_base + self.data[self.ip + 1]]
                    self.relative_base += p1
                    self.ip += 2
                case _:
                    raise ValueError(f"Invalid opcode: {op}")


def parse_data(data: str) -> list[int]:
    return list(map(int, data.split(",")))


async def run_robot(data: list[int], starting_color: int) -> dict[Coordinate, int]:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    painted = {}
    x, y = 0, 0
    direction = 0
    curr_color = starting_color

    robot = Program(data).run()
    await robot.asend(None)

    while True:
        try:
            color, rotation = await robot.asend(curr_color)
        except StopAsyncIteration:
            # how many panels were painted at least once?
            return painted

        painted[(x, y)] = color

        if rotation == 0:
            rotation = -1
        direction = (direction + rotation) % 4

        x += directions[direction][0]
        y += directions[direction][1]

        curr_color = painted.get((x, y), 0)


def part1(data: list[int]) -> int:
    colors = asyncio.run(run_robot(data, 0))
    return len(colors)


def part2(data: list[int]) -> str:
    def int_to_char(color: int) -> str:
        return "#" if color == 1 else " "

    colors = asyncio.run(run_robot(data, 1))

    top = max((coord[1] for coord in colors.keys()))
    bottom = min((coord[1] for coord in colors.keys()))

    left = min((coord[0] for coord in colors.keys()))
    right = max((coord[0] for coord in colors.keys()))

    return "\n" + "\n".join(
        "".join(int_to_char(colors.get((x, y), 0)) for x in range(left, right + 1))
        for y in range(top, bottom - 1, -1)
    )


if __name__ == "__main__":
    with Timing():
        content: str = get_data("inputs/day11.txt")
        data: list[int] = parse_data(content)

        print(f"part1: {part1(data)}")
        print(f"part2: {part2(data)}")
