#!/usr/bin/env python3

from collections import defaultdict


def part_one() -> None:
    with open("input.txt") as f:
        lines = []
        for line in f.readlines():
            lines.append(line.strip().split())

        signals = defaultdict(int)
        cycle, x = 0, 1
        for line in lines:
            if line[0] == "noop":
                cycle += 1
                if cycle == 20 or (20 + cycle) % 40 == 0:
                    signals[(20 + cycle)] = cycle * x
            elif line[0] == "addx":
                for _ in range(0, 2):
                    cycle += 1
                    if cycle == 20 or (20 + cycle) % 40 == 0:
                        signals[(20 + cycle)] = cycle * x

                x += int(line[1])

    print(sum(signals.values()))


def part_two() -> None:
    with open("input.txt") as f:
        lines = []
        for line in f.readlines():
            lines.append(line.strip().split())

    img: list[list[str]] = [[] for _ in range(0, 6)]
    cycle, spritepos = 0, 1

    row = 0
    for line in lines:
        if line[0] == "noop":
            cycle += 1

            crt_pos = (cycle - 1) - (row * 40)
            if crt_pos in range(spritepos - 1, spritepos + 2):
                img[row].append("#")
            else:
                img[row].append(".")

            # Go to new line
            if cycle % 40 == 0:
                row += 1
        elif line[0] == "addx":
            for _ in range(0, 2):
                cycle += 1

                crt_pos = (cycle - 1) - (row * 40)
                if crt_pos in range(spritepos - 1, spritepos + 2):
                    img[row].append("#")
                else:
                    img[row].append(".")

                # Go to new line
                if cycle % 40 == 0:
                    row += 1

            spritepos += int(line[1])

    for i in range(0, len(img)):
        for j in range(0, len(img[i])):
            print(img[i][j], end="")
        print("")


def main() -> None:
    part_one()
    part_two()


if __name__ == "__main__":
    main()
