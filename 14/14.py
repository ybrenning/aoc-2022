#!usr/bin/env python3


def part_one() -> None:
    with open("input.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    lines = [line.split(" -> ") for line in lines]

    rocks = set()
    for line in lines:
        coords = []

        for coord in line:
            x, y = map(int, coord.split(","))
            coords.append((x, y))

        for i in range(0, len(coords) - 1):
            x, y = coords[i]
            xn, yn = coords[i + 1]

            # x coord is changing
            if y == yn:
                for j in range(0, abs(xn - x) + 1):
                    rocks.add((x + j if xn - x > 0 else x - j, y))
            # y coord is changing
            elif x == xn:
                for j in range(0, abs(yn - y) + 1):
                    rocks.add((x, y + j if yn - y > 0 else y - j))

    floor = max([y for _, y in list(rocks)])

    sand = set()
    flag = True
    while flag:
        # Simulate new unit
        cx, cy = 500, 0
        while cy < floor:
            # Check if space is blocked
            if (cx, cy + 1) not in rocks | sand:
                cy += 1
                continue
            elif (cx - 1, cy + 1) not in rocks | sand:
                cx -= 1
                cy += 1
                continue
            elif (cx + 1, cy + 1) not in rocks | sand:
                cx += 1
                cy += 1
                continue

            # Unit comes to rest
            sand.add((cx, cy))
            flag = True
            break
        else:
            flag = False

    print(len(sand))


def main() -> None:
    part_one()


if __name__ == "__main__":
    main()
