import itertools as it

from aoc_util import Timing, get_data

BLACK = 0
WHITE = 1
TRANSPARENT = 2


def parse_data(content: str) -> list[int]:
    return list(map(int, content))


def part1(data: list[int], width: int = 25, height: int = 6) -> int:
    layer = min(it.batched(data, width * height), key=lambda layer: layer.count(BLACK))
    return layer.count(WHITE) * layer.count(TRANSPARENT)


def part2(data: list[int], width: int = 25, height: int = 6) -> str:
    decoded = [TRANSPARENT] * (width * height)

    layers = it.batched(data, width * height)
    for layer in layers:
        for i, pixel in enumerate(layer):
            if decoded[i] == TRANSPARENT:
                decoded[i] = pixel

    decoded = list(map({BLACK: " ", WHITE: "#", TRANSPARENT: " "}.get, decoded))
    return "\n" + "\n".join("".join(decoded) for decoded in it.batched(decoded, width))


if __name__ == "__main__":
    with Timing():
        content: str = get_data("inputs/day08.txt")
        data: list[int] = parse_data(content)

        print(f"part1: {part1(data)}")
        print(f"part2: {part2(data)}")
