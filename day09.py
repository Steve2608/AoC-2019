from collections import defaultdict

from aoc_util import Timing, get_data


class Program:
    def __init__(self, data: list[int]):
        self.data = defaultdict(int, enumerate(data))
        self.ip = 0
        self.relative_base = 0

    def parse_instruction(self, instruction: int) -> tuple[int, tuple[int, int, int]]:
        op = instruction % 100
        modes = (instruction // 100 % 10, instruction // 1000 % 10, instruction // 10000 % 10)
        return op, modes

    def run(self, input_value: int) -> int:
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
                            self.data[self.data[self.ip + 1]] = input_value
                        case 2:
                            self.data[self.relative_base + self.data[self.ip + 1]] = input_value
                    self.ip += 2
                case 4:
                    match modes[0]:
                        case 0:
                            p1 = self.data[self.data[self.ip + 1]]
                        case 1:
                            p1 = self.data[self.ip + 1]
                        case 2:
                            p1 = self.data[self.relative_base + self.data[self.ip + 1]]
                    output = p1
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

        return output


def parse_data(content: str) -> list[int]:
    return list(map(int, content.split(",")))


def part1(data: list[int]):
    program = Program(data)
    return program.run(1)


def part2(data: list[int]):
    program = Program(data)
    return program.run(2)


if __name__ == "__main__":
    with Timing():
        content: str = get_data("inputs/day09.txt")
        data: list[int] = parse_data(content)

        print(f"part1: {part1(data)}")
        print(f"part2: {part2(data)}")
