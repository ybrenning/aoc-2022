def part_one() -> None:
    with open("input.txt") as f:
        lines = f.readlines()

    count = 0
    for line in lines:
        ranges = line.split(",")

        fst = range(int(ranges[0].split("-")[0]), int(ranges[0].split("-")[1]))
        snd = range(int(ranges[1].split("-")[0]), int(ranges[1].split("-")[1]))

        if fst.start >= snd.start and fst.stop <= snd.stop:
            count += 1
        elif snd.start >= fst.start and snd.stop <= fst.stop:
            count += 1

    print(count)


def part_two() -> None:
    with open("input.txt") as f:
        lines = f.readlines()

    count = 0
    for line in lines:
        ranges = line.split(",")

        fst = range(int(ranges[0].split("-")[0]), int(ranges[0].split("-")[1]))
        snd = range(int(ranges[1].split("-")[0]), int(ranges[1].split("-")[1]))

        if fst.start <= snd.stop and fst.stop >= snd.start:
            count += 1

    print(count)


def main() -> None:
    part_one()
    part_two()


if __name__ == "__main__":
    main()
