from collections import Counter

from aoc_util import Timing, get_data

Range = tuple[int, int]


def parse_data(content: str) -> Range:
    return tuple(map(int, content.split("-")))


# password is 6 digits long ("rule1") is trivially true
# password is within range ("rule2") is trivially true


def rule_3(pw: str) -> bool:
    return any(a == b for a, b in zip(pw, pw[1:]))


def rule_4(pw: str) -> bool:
    return all(a <= b for a, b in zip(pw, pw[1:]))


def rule_5(pw: str) -> bool:
    return any(count == 2 for count in Counter(pw).values())


def part1(data: Range) -> int:
    def is_valid_password(password: int) -> bool:
        pw = str(password)
        return rule_3(pw) and rule_4(pw)

    start, stop = data
    return sum(is_valid_password(password) for password in range(start, stop + 1))


def part2(data: Range) -> int:
    def is_valid_password(password: int) -> bool:
        pw = str(password)
        return rule_3(pw) and rule_4(pw) and rule_5(pw)

    start, stop = data
    return sum(is_valid_password(password) for password in range(start, stop + 1))


if __name__ == "__main__":
    with Timing():
        content: str = get_data("inputs/day04.txt")
        data: tuple[int, int] = parse_data(content)

        print(f"part1: {part1(data)}")
        print(f"part2: {part2(data)}")
