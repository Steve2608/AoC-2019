from aoc_util import Timing, get_data


class Program:
    def __init__(self, data: list[int]):
        self.data = data.copy()
        self.ip = 0
        self.diagnostic_codes = []

    def parse_instruction(self, instruction: int) -> tuple[int, tuple[int, int, int]]:
        op = instruction % 100
        modes = (instruction // 100 % 10, instruction // 1000 % 10, instruction // 10000 % 10)
        return op, modes

    def run(self, input_value: int) -> int:
        while (instr := self.data[self.ip]) != 99:
            op, modes = self.parse_instruction(instr)

            match op:
                case 1:
                    p1 = (
                        self.data[self.data[self.ip + 1]]
                        if modes[0] == 0
                        else self.data[self.ip + 1]
                    )
                    p2 = (
                        self.data[self.data[self.ip + 2]]
                        if modes[1] == 0
                        else self.data[self.ip + 2]
                    )
                    self.data[self.data[self.ip + 3]] = p1 + p2
                    self.ip += 4
                case 2:
                    p1 = (
                        self.data[self.data[self.ip + 1]]
                        if modes[0] == 0
                        else self.data[self.ip + 1]
                    )
                    p2 = (
                        self.data[self.data[self.ip + 2]]
                        if modes[1] == 0
                        else self.data[self.ip + 2]
                    )
                    self.data[self.data[self.ip + 3]] = p1 * p2
                    self.ip += 4
                case 3:
                    self.data[self.data[self.ip + 1]] = input_value
                    self.ip += 2
                case 4:
                    p1 = (
                        self.data[self.data[self.ip + 1]]
                        if modes[0] == 0
                        else self.data[self.ip + 1]
                    )
                    self.diagnostic_codes.append(p1)
                    self.ip += 2
                case 5:
                    p1 = (
                        self.data[self.data[self.ip + 1]]
                        if modes[0] == 0
                        else self.data[self.ip + 1]
                    )
                    p2 = (
                        self.data[self.data[self.ip + 2]]
                        if modes[1] == 0
                        else self.data[self.ip + 2]
                    )
                    if p1 != 0:
                        self.ip = p2
                    else:
                        self.ip += 3
                case 6:
                    p1 = (
                        self.data[self.data[self.ip + 1]]
                        if modes[0] == 0
                        else self.data[self.ip + 1]
                    )
                    p2 = (
                        self.data[self.data[self.ip + 2]]
                        if modes[1] == 0
                        else self.data[self.ip + 2]
                    )
                    if p1 == 0:
                        self.ip = p2
                    else:
                        self.ip += 3
                case 7:
                    p1 = (
                        self.data[self.data[self.ip + 1]]
                        if modes[0] == 0
                        else self.data[self.ip + 1]
                    )
                    p2 = (
                        self.data[self.data[self.ip + 2]]
                        if modes[1] == 0
                        else self.data[self.ip + 2]
                    )
                    self.data[self.data[self.ip + 3]] = int(p1 < p2)
                    self.ip += 4
                case 8:
                    p1 = (
                        self.data[self.data[self.ip + 1]]
                        if modes[0] == 0
                        else self.data[self.ip + 1]
                    )
                    p2 = (
                        self.data[self.data[self.ip + 2]]
                        if modes[1] == 0
                        else self.data[self.ip + 2]
                    )
                    self.data[self.data[self.ip + 3]] = int(p1 == p2)
                    self.ip += 4
                case _:
                    raise ValueError(f"Invalid opcode: {op}")

        if all(d == 0 for d in self.diagnostic_codes[:-1]):
            return self.diagnostic_codes[-1]
        raise ValueError("No output found")


def parse_data(content: str) -> list[int]:
    return list(map(int, content.strip().split(",")))


def part1(data: list[int]) -> int:
    prog = Program(data)
    return prog.run(input_value=1)


def part2(data: list[int]) -> int:
    prog = Program(data)
    return prog.run(input_value=5)


if __name__ == "__main__":
    with Timing():
        content: str = get_data("inputs/day05.txt")
        data: list[int] = parse_data(content)

        print(f"part1: {part1(data)}")
        print(f"part2: {part2(data)}")
