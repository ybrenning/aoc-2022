#!/usr/bin/env python3

from functools import cmp_to_key
from itertools import zip_longest


def part_one() -> None:
    with open("input.txt") as f:
        lines = f.readlines()

    packets = [eval(line) for line in lines if len(line.strip()) != 0]

    indices = []
    for i in range(0, len(packets), 2):
        if compare(packets[i], packets[i + 1]) == -1:
            indices.append((i + 1) // 2 + 1)

    print(sum(indices))


def part_two() -> None:
    with open("input.txt") as f:
        lines = f.readlines()

    packets = [eval(line) for line in lines if len(line.strip()) != 0]

    packets.extend(([[2]], [[6]]))

    sorted_packets = sorted(packets, key=cmp_to_key(compare))

    print((sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1))


def compare(fst, snd):
    if fst is None:
        return -1
    elif snd is None:
        return 1

    if isinstance(fst, int) and isinstance(snd, int):
        if fst > snd:
            return 1
        elif fst < snd:
            return -1
        else:
            return 0
    elif isinstance(fst, list) and isinstance(snd, list):
        for f, s in zip_longest(fst, snd):
            if (result := compare(f, s)) != 0:
                return result
        return 0
    else:
        if isinstance(fst, list) and isinstance(snd, int):
            snd = [snd]
        elif isinstance(fst, int) and isinstance(snd, list):
            fst = [fst]
        return compare(fst, snd)


def main() -> None:
    part_one()
    part_two()


if __name__ == "__main__":
    main()
