import asyncio
import itertools as it

from aoc_util import Timing, get_data


class Program:
    def __init__(self, data: list[int], inputs: asyncio.Queue, outputs: asyncio.Queue):
        self.data = data.copy()
        self.ip = 0
        self.diagnostic_codes = []
        self.inputs = inputs
        self.outputs = outputs

    def parse_instruction(self, instruction: int) -> tuple[int, tuple[int, int, int]]:
        op = instruction % 100
        modes = (instruction // 100 % 10, instruction // 1000 % 10, instruction // 10000 % 10)
        return op, modes

    async def input(self, *inputs: int) -> int:
        for input in inputs:
            await self.inputs.put(input)

    async def output(self) -> int:
        return await self.outputs.get()

    async def run(self) -> int:
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
                    self.data[self.data[self.ip + 1]] = await self.inputs.get()
                    self.ip += 2
                case 4:
                    p1 = (
                        self.data[self.data[self.ip + 1]]
                        if modes[0] == 0
                        else self.data[self.ip + 1]
                    )
                    await self.outputs.put(p1)
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


def parse_data(content: str) -> list[int]:
    return list(map(int, content.split(",")))


def part1(data: list[int]) -> int:
    async def part1(data: list[int]) -> int:
        async def run(phase_settings: list[int]) -> int:
            pa, pb, pc, pd, pe = phase_settings

            a_inputs = asyncio.Queue()
            a_to_b = asyncio.Queue()
            b_to_c = asyncio.Queue()
            c_to_d = asyncio.Queue()
            d_to_e = asyncio.Queue()
            e_outputs = asyncio.Queue()

            amp_a = Program(data, a_inputs, a_to_b)
            amp_b = Program(data, a_to_b, b_to_c)
            amp_c = Program(data, b_to_c, c_to_d)
            amp_d = Program(data, c_to_d, d_to_e)
            amp_e = Program(data, d_to_e, e_outputs)

            await amp_a.input(pa)
            await amp_b.input(pb)
            await amp_c.input(pc)
            await amp_d.input(pd)
            await amp_e.input(pe)

            await amp_a.input(0)
            await asyncio.gather(
                amp_a.run(),
                amp_b.run(),
                amp_c.run(),
                amp_d.run(),
                amp_e.run(),
            )

            return await amp_e.output()

        return max(await asyncio.gather(*map(run, it.permutations(range(5)))))

    return asyncio.run(part1(data))


def part2(data: list[int]) -> int:
    async def part2(data: list[int]) -> int:
        async def run(phase_settings: list[int]) -> int:
            pa, pb, pc, pd, pe = phase_settings

            a_to_b = asyncio.Queue()
            b_to_c = asyncio.Queue()
            c_to_d = asyncio.Queue()
            d_to_e = asyncio.Queue()
            e_to_a = asyncio.Queue()

            amp_a = Program(data, e_to_a, a_to_b)
            amp_b = Program(data, a_to_b, b_to_c)
            amp_c = Program(data, b_to_c, c_to_d)
            amp_d = Program(data, c_to_d, d_to_e)
            amp_e = Program(data, d_to_e, e_to_a)

            await amp_a.input(pa)
            await amp_b.input(pb)
            await amp_c.input(pc)
            await amp_d.input(pd)
            await amp_e.input(pe)

            await amp_a.input(0)
            await asyncio.gather(
                amp_a.run(),
                amp_b.run(),
                amp_c.run(),
                amp_d.run(),
                amp_e.run(),
            )

            return await amp_e.output()

        return max(await asyncio.gather(*map(run, it.permutations(range(5, 10)))))

    return asyncio.run(part2(data))


if __name__ == "__main__":
    with Timing():
        content: str = get_data("inputs/day07.txt")
        data: list[int] = parse_data(content)

        print(f"part1: {part1(data)}")
        print(f"part2: {part2(data)}")
