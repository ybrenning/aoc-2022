#!/usr/bin/env python3

from collections import defaultdict


def part_one() -> None:
    with open("input.txt") as f:
        lines = f.readlines()

    sizes: dict[str, int] = defaultdict(int)
    filepath: list[str] = []

    for line in lines:
        if line.startswith("$ cd"):
            dir = line.split()[-1]
            if dir == "..":
                filepath.pop()
            else:
                filepath.append(dir)
        elif line.startswith("$ ls"):
            continue
        else:
            if line.split()[0].isdigit():
                size = int(line.split()[0])
                for i in range(0, len(filepath)):
                    sizes["/".join(filepath[: i + 1])] += size

    print(sum([size for size in sizes.values() if size <= 100_000]))


def part_two() -> None:
    with open("input.txt") as f:
        lines = f.readlines()

    sizes: dict[str, int] = defaultdict(int)
    filepath: list[str] = []

    for line in lines:
        if line.startswith("$ cd"):
            dir = line.split()[-1]
            if dir == "..":
                filepath.pop()
            else:
                filepath.append(dir)
        elif line.startswith("$ ls"):
            continue
        else:
            if line.split()[0].isdigit():
                size = int(line.split()[0])
                for i in range(0, len(filepath)):
                    sizes["/".join(filepath[: i + 1])] += size

    max_space = 70_000_000 - 30_000_000
    need_to_free = sizes["/"] - max_space

    ans = 1e9
    for size in sizes.values():
        if size >= need_to_free:
            ans = min(ans, size)

    print(ans)


def main() -> None:
    part_one()
    part_two()


if __name__ == "__main__":
    main()
