from aoc_util import Timing, get_data


def parse_data(content: str) -> list[int]:
    return list(map(int, content.strip().split(",")))


def init(data: list[int], a: int, b: int) -> list[int]:
    data = data.copy()

    data[1] = a
    data[2] = b

    return data


def run_intcode(data: list[int]) -> int:
    ip = 0
    while (op := data[ip]) != 99:
        match op:
            case 1:
                data[data[ip + 3]] = data[data[ip + 1]] + data[data[ip + 2]]
            case 2:
                data[data[ip + 3]] = data[data[ip + 1]] * data[data[ip + 2]]
            case _:
                raise ValueError(f"Invalid opcode: {op}")
        ip += 4
    return data[0]


def part1(data: list[int]) -> int:
    return run_intcode(init(data, 12, 2))


def part2(data: list[int]) -> int:
    for noun in range(100):
        for verb in range(100):
            if run_intcode(init(data, noun, verb)) == 19690720:
                return 100 * noun + verb
    raise ValueError("No solution found")


if __name__ == "__main__":
    with Timing():
        content: str = get_data("inputs/day02.txt")
        data: list[int] = parse_data(content)

        print(f"part1: {part1(data)}")
        print(f"part2: {part2(data)}")
